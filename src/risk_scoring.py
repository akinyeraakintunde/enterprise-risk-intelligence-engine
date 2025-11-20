import json
from pathlib import Path
from typing import Dict, Any, Optional

from .rules_engine import score_all_categories


class RiskEngine:
    """
    Hybrid risk engine that combines rule-based scoring with an optional ML component.
    If an ML model is provided, its probability score is blended with the rule-based
    trust score to produce a final risk score.
    """

    def __init__(self, model: Optional[Any] = None):
        self.model = model

        # Weight for each risk category in the rule-based score
        self.category_weights = {
            "financial": 0.30,
            "documentation": 0.20,
            "eligibility": 0.20,
            "compliance": 0.20,
            "behaviour": 0.10,
        }

        # Final score blending
        self.rule_weight = 0.60
        self.ml_weight = 0.40

    # ------------------------------------------------------------
    # Computes weighted rule score between 0 – 100
    # ------------------------------------------------------------
    def compute_rule_score(self, category_scores: Dict[str, int]) -> float:
        total_weighted = 0.0
        total_weight = 0.0

        for domain, score in category_scores.items():
            w = self.category_weights.get(domain, 0)
            total_weighted += w * score
            total_weight += w

        if total_weight == 0:
            return 0.0

        return total_weighted / total_weight

    # ------------------------------------------------------------
    # Optional ML model risk score (0–1)
    # ------------------------------------------------------------
    def compute_ml_score(self, profile: Dict[str, Any]) -> Optional[float]:
        if self.model is None:
            return None

        # Placeholder — in real usage you would extract structured features
        # and feed them into the ML classifier.
        # Example: self.model.predict_proba([[feature_vector]])[0][1]
        return 0.50  # Neutral placeholder

    # ------------------------------------------------------------
    # Combine rule-based score and ML score into final risk score (0–100)
    # ------------------------------------------------------------
    def combine_scores(self, rule_score: float, ml_score: Optional[float]) -> float:
        rule_risk = 1.0 - (rule_score / 100.0)  # Higher risk when rule score is low

        if ml_score is not None:
            combined_risk = (self.rule_weight * rule_risk) + (self.ml_weight * ml_score)
        else:
            combined_risk = rule_risk

        return round(combined_risk * 100, 2)

    # ------------------------------------------------------------
    # Risk band based on final risk score
    # ------------------------------------------------------------
    @staticmethod
    def risk_band(score: float) -> str:
        if score >= 70:
            return "High"
        elif score >= 40:
            return "Medium"
        return "Low"

    # ------------------------------------------------------------
    # Main scoring workflow
    # ------------------------------------------------------------
    def score_profile(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        category_scores, notes = score_all_categories(profile)
        rule_score = self.compute_rule_score(category_scores)
        ml_score = self.compute_ml_score(profile)
        final_score = self.combine_scores(rule_score, ml_score)
        band = self.risk_band(final_score)

        combined_notes = []
        for cat, n_list in notes.items():
            for n in n_list:
                combined_notes.append(f"[{cat}] {n}")

        return {
            "rule_scores": category_scores,
            "rule_based_score": round(rule_score, 2),
            "ml_score": ml_score,
            "final_risk_score": final_score,
            "risk_band": band,
            "notes": combined_notes,
        }


# ------------------------------------------------------------
# Helpers for CLI usage
# ------------------------------------------------------------
def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: Dict[str, Any], path: Path):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# ------------------------------------------------------------
# CLI entry point
# ------------------------------------------------------------
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Enterprise Risk Intelligence Engine")
    parser.add_argument("input", type=str, help="Path to input JSON profile.")
    parser.add_argument("--output", type=str, help="Optional output JSON file.")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input profile not found: {input_path}")

    profile = load_json(input_path)

    engine = RiskEngine()
    result = engine.score_profile(profile)

    if args.output:
        save_json(result, Path(args.output))
        print(f"Risk results saved to {args.output}")
    else:
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()