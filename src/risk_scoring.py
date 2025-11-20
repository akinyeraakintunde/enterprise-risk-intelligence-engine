import json
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np

from .rules_engine import score_all_categories


class RiskEngine:
    """
    Hybrid risk engine combining rule-based scoring with an optional ML model.

    If an ML model is available, it should expose a predict_proba(X) method.
    For demonstration, this implementation expects a pickled model at
    models/risk_model.pkl but will fall back to rule-based scoring if
    no model is found.
    """

    def __init__(self, model: Optional[Any] = None):
        self.model = model

        # weights for each category in the rule-based score
        self.category_weights = {
            "financial": 0.3,
            "documentation": 0.2,
            "eligibility": 0.2,
            "compliance": 0.2,
            "behaviour": 0.1,
        }

        # weight given to ML score when present
        self.ml_weight = 0.4
        self.rules_weight = 0.6

    def compute_rule_based_score(self, category_scores: Dict[str, int]) -> float:
        weighted = 0.0
        total_weight = 0.0

        for cat, score in category_scores.items():
            w = self.category_weights.get(cat, 0.0)
            weighted += w * score
            total_weight += w

        if total_weight == 0:
            return 0.0

        return weighted / total_weight

    def ml_risk_score(self, profile: Dict[str, Any]) -> Optional[float]:
        if self.model is None:
            return None

        # This is a placeholder. In a real implementation you would extract
        # numerical feature vectors from the profile and pass them to the model.
        # Here we simply return a fixed mid-range value for demonstration.
        return 0.5

    def combine_scores(self, rule_score: float, ml_score: Optional[float]) -> float:
        # Convert rule-based trust score (0–100) into a risk score (0–1)
        rule_risk = 1.0 - (rule_score / 100.0)

        if ml_score is not None:
            combined = self.rules_weight * rule_risk + self.ml_weight * ml_score
        else:
            combined = rule_risk

        # convert to 0–100 for readability
        return float(round(combined * 100, 2))

    @staticmethod
    def band_from_score(risk_score: float) -> str:
        if risk_score >= 70:
            return "High"
        elif risk_score >= 40:
            return "Medium"
        else:
            return "Low"

    def score_profile(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        category_scores, notes = score_all_categories(profile)
        rule_based_score = self.compute_rule_based_score(category_scores)
        ml_score = self.ml_risk_score(profile)
        final_risk_score = self.combine_scores(rule_based_score, ml_score)
        risk_band = self.band_from_score(final_risk_score)

        flattened_notes = []
        for cat, items in notes.items():
            for n in items:
                flattened_notes.append(f"[{cat}] {n}")

        return {
            "rule_scores": category_scores,
            "rule_based_score": round(rule_based_score, 2),
            "ml_score": ml_score,
            "final_risk_score": final_risk_score,
            "risk_band": risk_band,
            "notes": flattened_notes,
        }


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Enterprise Risk Intelligence Engine demo.")
    parser.add_argument("input_json", type=str, help="Path to profile JSON file.")
    args = parser.parse_args()

    profile_path = Path(args.input_json)
    if not profile_path.exists():
        raise FileNotFoundError(f"Profile file not found: {profile_path}")

    profile = load_json(profile_path)

    engine = RiskEngine()
    result = engine.score_profile(profile)

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()