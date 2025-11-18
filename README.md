<h1>Enterprise Risk Intelligence Engine</h1>
<h2>AI-Powered Technology Risk &amp; Threat Detection Engine</h2>
<p><em>A collaborative project by <strong>Ibrahim Akinyera (AI/ML Engineering Lead)</strong> and <strong>Busayo Odukoya (Senior Technology Risk Analyst, CME Group)</strong>.</em></p>

<hr>

<h2>Overview</h2>
<p>
The <strong>Enterprise Risk Intelligence Engine</strong> is an AI-powered system designed to detect anomalies in enterprise technology environments, 
identify potential threats, and generate structured risk intelligence reports.
</p>
<p>
This project combines:
</p>
<ul>
  <li><strong>Ibrahim Akinyera’s</strong> expertise in AI/ML engineering</li>
  <li><strong>Busayo Odukoya’s</strong> expertise in enterprise Technology Risk Management</li>
</ul>
<p>
to deliver a practical, innovative approach to intelligent risk analytics.
</p>

<h2>Objectives</h2>
<ul>
  <li>Build a machine-learning anomaly detection model for enterprise log ecosystems</li>
  <li>Implement expert-defined KRIs (Key Risk Indicators)</li>
  <li>Develop a risk scoring engine (Low to Critical)</li>
  <li>Generate automated HTML/PDF risk intelligence reports</li>
  <li>Demonstrate cross-functional collaboration for Global Talent (Tech Nation) evidence</li>
</ul>

<h2>Key Features</h2>

<h3>AI Anomaly Detection</h3>
<p>Detects suspicious events across:</p>
<ul>
  <li>Authentication logs</li>
  <li>Network activity</li>
  <li>Application events</li>
  <li>API request behaviour</li>
</ul>

<h3>Risk Scoring Engine</h3>
<p>Risk levels determined by:</p>
<ul>
  <li>Event severity</li>
  <li>Frequency</li>
  <li>Business impact</li>
  <li>Expert-defined KRIs</li>
</ul>

<h3>Automated Reporting</h3>
<p>Generates enterprise-ready risk reports summarising:</p>
<ul>
  <li>Critical anomalies</li>
  <li>Risk clusters</li>
  <li>Impact assessment</li>
  <li>Recommended actions</li>
</ul>

<h3>Modular Architecture</h3>
<p>Designed for extensibility:</p>
<ul>
  <li>Add new machine learning models</li>
  <li>Integrate cloud log sources</li>
  <li>Extend to SIEM pipelines</li>
</ul>

<h2>System Architecture</h2>
<p><em>Architecture diagram located in:</em> <code>/diagrams/architecture.png</code></p>

<h2>Repository Structure</h2>
<pre><code>enterprise-risk-intelligence-engine/
│
├── data/
│   └── system_logs/
│
├── diagrams/
│   └── architecture.png
│
├── src/
│   ├── anomaly_detector.py
│   ├── risk_score_engine.py
│   ├── risk_analyzer.py
│   └── report_generator.py
│
└── README.md
</code></pre>

## Enterprise KRIs and Risk Model (Expert Input)

The risk scoring engine is based on enterprise-style Key Risk Indicators (KRIs)
provided by the Technology Risk expert:

| KRI ID | Description                                            | Mapped Event Type        | Typical Risk Range |
|-------|--------------------------------------------------------|--------------------------|--------------------|
| KRI1  | Repeated failed login attempts (possible brute force)  | `login` with status=fail | Medium to High     |
| KRI2  | Privilege escalation to admin or elevated privileges   | `privilege_escalation`   | High to Critical   |
| KRI3  | Data export from sensitive systems or locations        | `data_export`            | High to Critical   |
| KRI4  | Suspicious login pattern or unusual IP/location        | `suspicious_login`       | Medium to High     |

These KRIs are encoded in the `RiskScorer` class, which assigns a numeric score
(1–10) and maps it to an enterprise risk level (Low, Medium, High, Critical).

<h2>How It Works</h2>

<h3>1. Log Ingestion</h3>
<p>Loads enterprise event logs from <code>/data/system_logs/</code>.</p>

<h3>2. Machine Learning Anomaly Detection</h3>
<p>Flags patterns deviating from normal behaviour.</p>

<h3>3. Risk Scoring</h3>
<p>Applies expert-defined scoring to classify events from Low to Critical.</p>

<h3>4. Automated Reporting</h3>
<p>Produces clear, structured reports for risk teams and decision makers.</p>

<h2>Getting Started</h2>

<h3>Clone the repository</h3>
<pre><code>git clone https://github.com/akinyeraakintunde/enterprise-risk-intelligence-engine.git
</code></pre>

<h3>Install dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>Run the analyzer</h3>
<pre><code>python src/risk_analyzer.py
</code></pre>

<h2>Collaborators</h2>

<h3>Ibrahim Akinyera</h3>
<p>AI/ML Engineer • Data Scientist<br>
GitHub: <a href="https://github.com/akinyeraakintunde">https://github.com/akinyeraakintunde</a></p>

<h3>Busayo Odukoya</h3>
<p>Senior Technology Risk Analyst (CME Group)<br>
Expert in enterprise risk, KRIs, operational controls and threat intelligence.</p>

<h2>Relevance to Tech Nation</h2>
<p>This project demonstrates:</p>
<ul>
  <li>Technical leadership in AI/ML engineering</li>
  <li>Industry collaboration with a recognised Technology Risk specialist</li>
  <li>Innovation in cybersecurity automation</li>
  <li>Impact and value in enterprise risk intelligence</li>
</ul>

<h2>License</h2>
<p>Released under the <strong>MIT License</strong>.</p>
