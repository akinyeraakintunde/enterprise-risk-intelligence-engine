# risk_score_engine.py
# Converts anomalies into risk scores and levels

from report_generator import ReportGenerator


class RiskScorer:
    def __init__(self):
        # Simple scoring weights; later we will refine with Busayo's inputs
        self.base_scores = {
            "privilege_escalation": 9,
            "data_export": 8,
            "suspicious_login": 7,
            "login": 4,
        }
        self.failed_bonus = 2

    def score_events(self, anomalies):
        scored = []

        for a in anomalies:
            event_type = a.get("event_type", "")
            status = a.get("status", "")

            score = self.base_scores.get(event_type, 5)

            if status == "failed":
                score += self.failed_bonus

            # Clamp score between 1 and 10
            score = max(1, min(score, 10))

            if score >= 9:
                level = "Critical"
            elif score >= 7:
                level = "High"
            elif score >= 4:
                level = "Medium"
            else:
                level = "Low"

            enriched = dict(a)
            enriched["score"] = score
            enriched["risk_level"] = level
            scored.append(enriched)

        return scored

    def generate_report(self, scored_events, output="risk_report.html"):
        generator = ReportGenerator()
        generator.create_html_report(scored_events, output=output)
