import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONDS = ["R0A", "R0B", "R1", "R2"]

def load(condition):
    path = ROOT / "results" / f"results_{condition}.json"
    if not path.exists():
        raise FileNotFoundError(path)
    rows = json.loads(path.read_text(encoding="utf-8"))
    out = {}
    for row in rows:
        winner = row.get("winner")
        confidence = row.get("confidence")
        if winner not in ("A", "B", "TIE"):
            raise ValueError(f"{condition}: invalid winner in {row}")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            raise ValueError(f"{condition}: invalid confidence in {row}")
        prompt_id = row["evaluation_id"].split("-")[0]
        if prompt_id in out:
            raise ValueError(f"{condition}: duplicate {prompt_id}")
        out[prompt_id] = row
    if len(out) != 20:
        raise ValueError(f"{condition}: expected 20 results, got {len(out)}")
    return out

R = {c: load(c) for c in CONDS}
M = {x["evaluation_id"]: x for x in json.loads((ROOT / "mapping.json").read_text(encoding="utf-8"))["mapping"]}

def disagreement(a, b):
    return sum(R[a][p]["winner"] != R[b][p]["winner"] for p in R[a])

def model_winner(condition, prompt_id):
    winner = R[condition][prompt_id]["winner"]
    if winner == "TIE":
        return "TIE"
    return M[f"{prompt_id}-EC-{condition}"][winner + "_model"]

summary = {"n": 20, "disagreement": {}, "conditions": {}, "classifications": {}, "changed_prompt_ids": {}}

for c in ("R0B", "R1", "R2"):
    n = disagreement("R0A", c)
    summary["disagreement"][f"{c}_vs_R0A"] = {"count": n, "proportion": n / 20}

control = summary["disagreement"]["R0B_vs_R0A"]["proportion"]
for c in ("R1", "R2"):
    summary["disagreement"][f"{c}_vs_R0A"]["descriptive_excess_over_control"] = summary["disagreement"][f"{c}_vs_R0A"]["proportion"] - control

for c in CONDS:
    wins = [R[c][p]["winner"] for p in sorted(R[c])]
    confidences = [R[c][p]["confidence"] for p in sorted(R[c])]
    model_wins = [model_winner(c, p) for p in sorted(R[c])]
    summary["conditions"][c] = {
        "A": wins.count("A"), "B": wins.count("B"), "TIE": wins.count("TIE"),
        "confidence_mean": statistics.mean(confidences),
        "confidence_median": statistics.median(confidences),
        "qwen_wins": model_wins.count("qwen"), "k2_wins": model_wins.count("k2"), "ties": model_wins.count("TIE")
    }

for prompt_id in sorted(R["R0A"]):
    values = {c: R[c][prompt_id]["winner"] for c in CONDS}
    if values["R0A"] != values["R0B"]:
        classification = "CONTROL_UNSTABLE"
    elif len(set(values.values())) == 1:
        classification = "STABLE_ACROSS_TESTED_RUBRICS"
    else:
        classification = "RUBRIC_SENSITIVE"
    summary["classifications"][prompt_id] = {"classification": classification, **values}

for c in ("R1", "R2"):
    summary["changed_prompt_ids"][c] = [p for p in sorted(R["R0A"]) if R[c][p]["winner"] != R["R0A"][p]["winner"]]

(ROOT / "analysis_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print("Wrote analysis_summary.json")
