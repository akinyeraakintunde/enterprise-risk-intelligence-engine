import argparse
from pathlib import Path
import json

from risk_engine.risk_scoring import RiskEngine, load_json, save_json


def main():
    parser = argparse.ArgumentParser(
        description="Enterprise Risk Intelligence Engine – CLI Runner"
    )

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to input JSON file containing the risk profile."
    )

    parser.add_argument(
        "--output",
        type=str,
        required=False,
        help="Optional output JSON path to save the risk scoring result."
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    profile = load_json(input_path)

    engine = RiskEngine()
    result = engine.score_profile(profile)

    if args.output:
        save_json(result, Path(args.output))
        print(f"Risk scoring saved to {args.output}")
    else:
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()