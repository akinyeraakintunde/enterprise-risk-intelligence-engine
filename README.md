Enterprise Risk Intelligence Engine
AI-Powered Technology Risk & Threat Detection Engine
A collaborative project by Ibrahim Akinyera (AI/ML Engineering Lead) and Busayo Odukoya (Senior Technology Risk Analyst, CME Group).

Overview
The Enterprise Risk Intelligence Engine is an AI-powered system designed to detect anomalies in enterprise technology environments, identify potential threats, and generate structured risk intelligence reports.
This project combines:
	•	Ibrahim Akinyera’s expertise in AI/ML engineering
	•	Busayo Odukoya’s expertise in enterprise Technology Risk Management

together delivering a practical, innovative approach to intelligent risk analytics.

Objectives
	•	Build a machine-learning anomaly detection model for enterprise log ecosystems
	•	Implement expert-defined KRIs (Key Risk Indicators)
	•	Develop a risk scoring engine (Low → Critical)
	•	Generate automated HTML/PDF risk intelligence reports
	•	Demonstrate cross-functional collaboration for Global Talent (Tech Nation) evidence

Key Features

AI Anomaly Detection
Detects suspicious events across:
	•	Authentication logs
	•	Network activity
	•	Application events
	•	API request behaviour

Risk Scoring Engine
Risk levels determined by:
	•	Event severity
	•	Frequency
	•	Business impact
	•	Expert-defined KRIs

Automated Reporting
Generates enterprise-ready risk reports summarising:
	•	Critical anomalies
	•	Risk clusters
	•	Impact assessment
	•	Recommended actions

Modular Architecture
Designed for extensibility:
	•	Add new ML models
	•	Integrate cloud log sources
	•	Extend to SIEM pipelines

System Architecture
Architecture diagram located in:
/diagrams/architecture.png

Repository Structure
enterprise-risk-intelligence-engine/
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

How It Works
1. Log Ingestion
Loads enterprise event logs from /data/system_logs/.

2. ML Anomaly Detection
Flags patterns deviating from normal behaviour.

3. Risk Scoring
Applies expert-defined scoring to classify events from Low → Critical.

4. Automated Reporting
Produces clear, structured reports for risk teams and decision makers.

Getting Started

Clone the repository
git clone https://github.com/akinyeraakintunde/enterprise-risk-intelligence-engine.git
Install dependencies
pip install -r requirements.txt
Run the analyzer
python src/risk_analyzer.py

Collaborators
Ibrahim Akinyera
AI/ML Engineer • Data Scientist
GitHub: https://github.com/akinyeraakintunde

Busayo Odukoya
Senior Technology Risk Analyst (CME Group)
Expert in enterprise risk, KRIs, operational controls & threat intelligence.

Relevance to Tech Nation
This project demonstrates:
	•	Technical leadership in AI/ML engineering
	•	Industry collaboration with a recognised Technology Risk specialist
	•	Innovation in cybersecurity automation
	•	Impact and value in enterprise risk intelligence

License
Released under the MIT License.