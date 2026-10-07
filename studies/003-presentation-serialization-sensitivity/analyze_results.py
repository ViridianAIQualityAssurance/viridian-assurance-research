import json
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONDS = ["P0", "PA", "PB", "PAB"]

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

def model_winner(condition, prompt_id):
    winner = R[condition][prompt_id]["winner"]
    if winner == "TIE":
        return "TIE"
    return M[f"{prompt_id}-PS-{condition}"][winner + "_model"]

summary = {"n": 20, "disagreement": {}, "conditions": {}, "classifications": {}, "changed_prompt_ids": {}}

for c in ("PA", "PB", "PAB"):
    changed = [p for p in sorted(R["P0"]) if R[c][p]["winner"] != R["P0"][p]["winner"]]
    summary["disagreement"][f"{c}_vs_P0"] = {"count": len(changed), "proportion": len(changed) / 20}
    summary["changed_prompt_ids"][c] = changed

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

for prompt_id in sorted(R["P0"]):
    values = {c: R[c][prompt_id]["winner"] for c in CONDS}
    if values["PAB"] != values["P0"]:
        classification = "COMMON_WRAPPER_OR_REPEAT_UNSTABLE"
    elif values["PA"] == "A" and values["PB"] == "B":
        classification = "WRAPPER_ATTRACTION_PATTERN"
    elif values["PA"] == "B" and values["PB"] == "A":
        classification = "WRAPPER_AVERSION_PATTERN"
    elif values["P0"] == values["PA"] == values["PB"]:
        classification = "CONTENT_STABLE"
    else:
        classification = "MIXED_OR_TIE"
    summary["classifications"][prompt_id] = {"classification": classification, **values}

(ROOT / "analysis_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print("Wrote analysis_summary.json")
