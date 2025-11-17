# risk_analyzer.py
# Main orchestrator for the risk intelligence engine

from anomaly_detector import AnomalyDetector
from risk_score_engine import RiskScorer


def run_risk_analysis():
    detector = AnomalyDetector()
    scorer = RiskScorer()

    logs = detector.load_logs("data/system_logs/")
    print(f"Loaded {len(logs)} log entries.")

    anomalies = detector.detect_anomalies(logs)
    print(f"Detected {len(anomalies)} anomalies.")

    scored = scorer.score_events(anomalies)
    scorer.generate_report(scored, output="risk_report.html")


if __name__ == "__main__":
    run_risk_analysis()
