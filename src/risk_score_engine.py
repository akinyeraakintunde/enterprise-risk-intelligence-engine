# risk_score_engine.py
# Enterprise KRI–driven risk scoring engine
#
# Phase 2: reflects expert-defined KRIs and risk levels.
# (Based on inputs from the Technology Risk Analyst.)

from report_generator import ReportGenerator


class RiskScorer:
    """
    Converts detected anomalies into risk scores and levels, using
    enterprise-style KRIs and risk thresholds.

    Assumed KRIs:
    - KRI1: Repeated failed logins (possible brute force)
    - KRI2: Privilege escalation
    - KRI3: Data export from sensitive systems
    - KRI4: Suspicious login from unusual IP or pattern
    """

    def __init__(self):
        # Base scores per event type (1–10)
        self.base_scores = {
            "login": 3,
            "privilege_escalation": 9,  # KRI2
            "data_export": 8,           # KRI3
            "suspicious_login": 7,      # KRI4
        }

        # Extra weight for failures (KRI1)
        self.failed_bonus = 2

    def score_events(self, anomalies):
        """
        Input: list of anomaly dicts from AnomalyDetector.
        Output: same list enriched with numeric 'score' and textual 'risk_level'.
        """
        scored = []

        for a in anomalies:
            event_type = a.get("event_type", "").lower()
            status = a.get("status", "").lower()

            # Base score from event type; default to 5 (Medium) if unknown
            score = self.base_scores.get(event_type, 5)

            # KRI1: failed attempts are more risky
            if status == "failed":
                score += self.failed_bonus

            # Clamp to 1–10 range
            score = max(1, min(score, 10))

            # Map numeric score to enterprise risk level
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
        """
        Delegates to the ReportGenerator to produce an HTML report.
        """
        generator = ReportGenerator()
        generator.create_html_report(scored_events, output=output)
