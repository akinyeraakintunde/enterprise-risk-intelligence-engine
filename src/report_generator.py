# report_generator.py
# Generates a simple HTML risk report

from pathlib import Path
from datetime import datetime


class ReportGenerator:
    def create_html_report(self, events, output="risk_report.html"):
        output_path = Path(output)

        rows = []
        for e in events:
            rows.append(
                f"<tr>"
                f"<td>{e.get('timestamp','')}</td>"
                f"<td>{e.get('user','')}</td>"
                f"<td>{e.get('event_type','')}</td>"
                f"<td>{e.get('source_ip','')}</td>"
                f"<td>{e.get('status','')}</td>"
                f"<td>{e.get('score','')}</td>"
                f"<td>{e.get('risk_level','')}</td>"
                f"<td>{e.get('reason','')}</td>"
                f"</tr>"
            )

        html = f"""
        <html>
        <head>
            <title>Enterprise Risk Intelligence Report</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Enterprise Risk Intelligence Report</h1>
            <p>Generated at: {datetime.utcnow().isoformat()}Z</p>
            <table border="1" cellspacing="0" cellpadding="4">
                <thead>
                    <tr>
                        <th>Timestamp</th>
                        <th>User</th>
                        <th>Event Type</th>
                        <th>Source IP</th>
                        <th>Status</th>
                        <th>Score</th>
                        <th>Risk Level</th>
                        <th>Reason</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(rows)}
                </tbody>
            </table>
        </body>
        </html>
        """

        output_path.write_text(html, encoding="utf-8")
        print(f"Risk report written to: {output_path.resolve()}")
