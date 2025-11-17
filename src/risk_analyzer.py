# risk_analyzer.py
# Placeholder: Main orchestrator for the risk intelligence engine

from anomaly_detector import AnomalyDetector
from risk_score_engine import RiskScorer

def run_risk_analysis():
    detector = AnomalyDetector()
    scorer = RiskScorer()

    logs = detector.load_logs("data/system_logs/")
    anomalies = detector.detect_anomalies(logs)
    scores = scorer.score_events(anomalies)

    scorer.generate_report(scores)

if __name__ == "__main__":
    run_risk_analysis()
