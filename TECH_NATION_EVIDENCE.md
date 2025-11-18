<section style="font-family: Arial, sans-serif; line-height: 1.6;">

<h1>Enterprise Risk Intelligence Engine</h1>
<h3>AI-Powered Log Analysis • Anomaly Detection • Risk Scoring • Automated Reporting</h3>

<p>
This project is an <b>AI-powered enterprise risk intelligence system</b> that ingests organisational logs,
detects anomalies using machine learning, scores risks using Key Risk Indicators (KRIs),
and automatically generates structured risk reports for cybersecurity, audit, and governance teams.
</p>

<p>
It demonstrates advanced capabilities in:
</p>

<ul>
  <li>Machine learning (Isolation Forest anomaly detection)</li>
  <li>Cybersecurity engineering</li>
  <li>Enterprise risk modelling</li>
  <li>Python software architecture</li>
  <li>Automated reporting workflows</li>
  <li>Collaboration with a Senior Technology Risk Analyst (CME Group)</li>
</ul>

<hr/>

<h2>🚀 Project Overview</h2>

<p>
Most enterprise risk teams rely on slow, manual log-review processes, inconsistent spreadsheets,
and limited visibility into abnormal behaviour. This system automates the entire workflow:
</p>

<ul>
  <li>✔ Log ingestion</li>
  <li>✔ Machine-learning anomaly detection</li>
  <li>✔ KRI-based risk scoring</li>
  <li>✔ Automated, exportable risk reports</li>
</ul>

<p>
This enables <b>faster insights, more accurate detection, and scalable security intelligence</b>.
</p>

<hr/>

<h2>🧠 System Architecture</h2>

<pre><code>/src
 ├── anomaly_detector.py         # ML-based anomaly detection
 ├── risk_score_engine.py        # KRI-based scoring logic
 ├── risk_analyzer.py            # Pipeline orchestration
 └── report_generator.py         # Automated risk report generation
</code></pre>

<h3>Architecture Diagram</h3>
<p><img src="docs/figures/architecture_diagram.png" alt="Architecture Diagram" style="max-width: 100%;"></p>

<hr/>

<h2>🔍 Key Features</h2>

<h3>1. Machine Learning Anomaly Detection</h3>
<ul>
  <li>Isolation Forest model</li>
  <li>Detects abnormal log behaviour</li>
  <li>Supports semi-supervised learning</li>
  <li>Configurable thresholds</li>
</ul>

<h3>2. Enterprise Risk Scoring Engine</h3>
<p>This module transforms anomalies into structured enterprise risk scores using:</p>
<ul>
  <li>Weighted KRIs</li>
  <li>Threshold-based scoring</li>
  <li>Low / Medium / High severity levels</li>
  <li>Modular scoring logic</li>
</ul>

<h3>3. Automated Risk Report Generation</h3>
<p>Produces formatted reports containing:</p>
<ul>
  <li>Risk summary</li>
  <li>Anomaly details</li>
  <li>KRI contributions</li>
  <li>Scoring breakdown</li>
  <li>Recommended actions</li>
</ul>

<hr/>

<h2>👤 Industry Collaboration — Mr. Busayo Odukoya (Senior Technology Risk Analyst, CME Group)</h2>

<p>
This project was developed with the professional guidance and domain expertise of 
<b>Mr. Busayo Odukoya</b>, a <b>Senior Technology Risk Analyst at CME Group</b>,
one of the world’s largest and most respected financial exchanges.
</p>

<h3>📚 Long-Term Mentor Since 2012</h3>

<p>
I have known and worked with Busayo since <b>2012</b>, during our time at 
<b>Fountain University, Osogbo</b> where:
</p>

<ul>
  <li>He was a 300-level Computer Science student</li>
  <li>I was a 100-level Computer Science student</li>
  <li>He mentored me academically, technically, and professionally</li>
</ul>

<p>
Throughout university and after graduation, he played a consistent role in shaping my growth:
</p>

<ul>
  <li>Software engineering discipline</li>
  <li>Cybersecurity awareness</li>
  <li>Professional ethics & risk thinking</li>
  <li>Career path guidance</li>
  <li>Understanding corporate governance & controls</li>
</ul>

<h3>🎯 His Enterprise Contribution to This Project</h3>

<ul>
  <li>Validation of Key Risk Indicators (KRIs)</li>
  <li>Definition of enterprise risk thresholds</li>
  <li>Review of scoring logic and weighting</li>
  <li>Financial-sector compliant risk taxonomy</li>
  <li>Ensuring alignment with actual enterprise controls</li>
  <li>Providing practical audit and governance insights</li>
</ul>

<p>
His involvement elevates the system to <b>enterprise-grade quality</b> and adds 
substantial credibility to the project.
</p>

<hr/>

<h2>🧩 Example Code Snippets</h2>

<h3>Isolation Forest Anomaly Detection</h3>
<pre><code>from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(features)
predictions = model.predict(features)
</code></pre>

<h3>Risk Scoring Logic</h3>
<pre><code>def calculate_risk(log):
    score = 0

    if log["failed_logins"] > 3:
        score += 20

    if log["ip_reputation"] == "malicious":
        score += 40

    if log["anomaly_detected"]:
        score += 30

    return score
</code></pre>

<hr/>

<h2>📂 Repository Structure</h2>

<pre><code>.
├── README.md
├── TECH_NATION_EVIDENCE.md
├── Evidence_4_Enterprise_Risk_Intelligence_Engine_Ibrahim_Akinyera.pdf
├── src/
│   ├── anomaly_detector.py
│   ├── risk_score_engine.py
│   ├── risk_analyzer.py
│   └── report_generator.py
├── docs/
│   └── figures/
│       ├── architecture_diagram.png
│       ├── risk_report_sample.png
│       ├── anomaly_flow.png
│       └── scoring_logic.png
└── tests/
</code></pre>

<hr/>

<h2>📄 Evidence Document (Tech Nation)</h2>

<p>
Download the full evidence submitted for my UK Global Talent Visa application:
</p>

<p>
  👉 <a href="Evidence_4_Enterprise_Risk_Intelligence_Engine_Ibrahim_Akinyera.pdf">
  Evidence_4_Enterprise_Risk_Intelligence_Engine_Ibrahim_Akinyera.pdf
  </a>
</p>

<hr/>

<h2>🇬🇧 Tech Nation Relevance</h2>

<p>See: <a href="TECH_NATION_EVIDENCE.md">TECH_NATION_EVIDENCE.md</a></p>

<ul>
  <li>Proven exceptional technical expertise</li>
  <li>Real cybersecurity + AI engineering</li>
  <li>Enterprise risk modelling</li>
  <li>Collaboration with a Senior Risk Analyst in a global institution</li>
  <li>Ability to design complex digital systems end-to-end</li>
</ul>

<hr/>

<h2>🧑‍💻 Author</h2>
<p>
<b>Ibrahim Akintunde Akinyera</b><br/>
AI/ML Engineer • Data Scientist • Cybersecurity Contributor<br/>
Founder – NxtAbroad AI<br/>
GitHub: <a href="https://github.com/akinyeraakintunde">akinyeraakintunde</a>
</p>

<hr/>

<h2>⭐ How to Run</h2>

<h3>1. Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>2. Run risk pipeline</h3>
<pre><code>python src/risk_analyzer.py</code></pre>

<h3>3. View report</h3>
<p>Reports appear in <code>.txt</code> or <code>.html</code> formats.</p>

<hr/>

<h2>🧭 Future Improvements</h2>

<ul>
  <li>Real-time log streaming</li>
  <li>Autoencoder / Transformer anomaly detection</li>
  <li>Dashboard visualisation (Streamlit / Grafana)</li>
  <li>SIEM integration</li>
</ul>

</section>