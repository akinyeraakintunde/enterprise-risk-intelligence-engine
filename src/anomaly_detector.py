# anomaly_detector.py
# Basic rule-based anomaly detection for enterprise logs

import csv
from pathlib import Path


class AnomalyDetector:
    """
    Loads enterprise log data and flags basic anomalies.

    Phase 1: simple rule-based detection
    Phase 2: can be extended with ML models.
    """

    def load_logs(self, path: str):
        csv_path = Path(path)
        if csv_path.is_dir():
            # default file
            csv_path = csv_path / "sample_logs.csv"

        logs = []
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                logs.append(row)
        return logs

    def detect_anomalies(self, logs):
        """
        Very simple heuristic rules:
        - Any event_type in high_risk_events is an anomaly
        - Any status == 'failed' is an anomaly
        """
        high_risk_events = {
            "privilege_escalation",
            "data_export",
            "suspicious_login",
        }

        anomalies = []

        for row in logs:
            event_type = row.get("event_type", "").lower()
            status = row.get("status", "").lower()

            is_anomaly = False
            reasons = []

            if event_type in high_risk_events:
                is_anomaly = True
                reasons.append(f"High-risk event type: {event_type}")

            if status == "failed":
                is_anomaly = True
                reasons.append("Failed action")

            if is_anomaly:
                anomalies.append(
                    {
                        "timestamp": row.get("timestamp"),
                        "user": row.get("user"),
                        "event_type": event_type,
                        "source_ip": row.get("source_ip"),
                        "status": status,
                        "reason": "; ".join(reasons),
                    }
                )

        return anomalies
