# Enterprise Risk Intelligence Engine

The Enterprise Risk Intelligence Engine is a Python-based system for assessing, scoring, and explaining enterprise risks by analysing logs, detecting anomalies, and applying a structured KRI-driven scoring model. It is designed for SMEs, cybersecurity teams, and digital organisations that require automated, transparent, and repeatable risk evaluation.

The system was architected and implemented by Ibrahim Akintunde Akinyera, with risk-domain review by Busayo Ezra Odukoya (Senior Technology Risk Management Analyst, CME Group). It forms a core part of the Technical Contribution evidence for the UK Global Talent Visa (Digital Technology).

------------------------------------------------------------
## 1. Why This Project Exists

Most organisations rely on spreadsheets and subjective judgement when assessing operational or technology risk. This leads to:

- inconsistent assessments across teams
- no traceability or justification behind decisions
- no automation or repeatability
- limited visibility into anomalous behaviour
- weak governance, oversight, and accountability

This engine provides a structured and automated alternative through:

- anomaly detection using Isolation Forest
- KRI-based quantitative scoring
- automated narrative reporting
- clear architecture and documentation
- reproducible, extensible engineering patterns

------------------------------------------------------------
## 2. Key Features

- Anomaly Detection  
  Detects unusual log patterns using Isolation Forest.

- KRI-Based Risk Scoring  
  Scores anomaly severity, login risk, error spikes, rare events, and log volume variation.

- Explainable Outputs  
  Generates narrative notes explaining each risk factor.

- Automated Reporting  
  Produces text or HTML risk reports.

- Modular Architecture  
  Separate modules for ML detection, scoring, analysis, and reporting.

- Tech Nation Evidence Ready  
  Includes documentation, diagrams, and the full Evidence PDF.

------------------------------------------------------------
## 3. System Architecture

A full system architecture diagram is available under:
docs/figures/architecture_diagram.png

High-level flow:
1. Raw logs ingested
2. Normalisation and feature extraction
3. Isolation Forest anomaly detection
4. KRI computation
5. Weighted risk scoring
6. Risk band classification
7. Narrative report generation

------------------------------------------------------------
## 4. Repository Structure

enterprise-risk-intelligence-engine/
|
├── data/                     Sample log input files
├── docs/
│   └── figures/              Architecture and scoring diagrams
├── src/
│   ├── anomaly_detector.py   ML-based anomaly detection
│   ├── risk_score_engine.py  KRI-based scoring logic
│   ├── risk_analyzer.py      Full pipeline orchestrator
│   ├── report_generator.py   Text and HTML reporting
│   └── utils.py              Helper utilities
|
├── outputs/                  Generated risk reports
├── tests/                    Unit tests (optional)
|
├── Evidence_4_Enterprise_Risk_Intelligence_Engine_Ibrahim_Akinyera.pdf
├── TECH_NATION_EVIDENCE.md
├── requirements.txt
└── README.md

------------------------------------------------------------
## 5. Installation

Clone the repo:

git clone https://github.com/akinyeraakintunde/enterprise-risk-intelligence-engine.git
cd enterprise-risk-intelligence-engine

Install dependencies:

pip install -r requirements.txt

------------------------------------------------------------
## 6. Running the Engine

Default run:

python src/risk_analyzer.py

Default inputs:
data/system_logs/sample_logs.csv

Default outputs:
outputs/risk_report.txt

Custom paths:

python src/risk_analyzer.py --input data/my_logs.csv --output reports/my_report.txt

------------------------------------------------------------
## 7. Scoring Logic (KRI Model)

def calculate_risk_score(kri_scores):
    weights = {
        "anomaly_severity": 0.30,
        "log_volume_variation": 0.20,
        "failed_login_rate": 0.20,
        "error_spike_index": 0.20,
        "rare_event_density": 0.10
    }

    final_score = 0
    for kri, value in kri_scores.items():
        final_score += weights.get(kri, 0) * value

    return round(final_score, 2)

Higher scores indicate higher risk.

------------------------------------------------------------
## 8. Outputs

The generated report includes:

- Overall risk score (0–100)
- Risk band (Low, Medium, High)
- KRI breakdown
- Anomaly summary
- Narrative explanation
- Recommended next steps

Sample output diagram:
docs/figures/risk_report_sample.png

## 🔴 Live Demo
A tiny Streamlit demo: upload CSV logs → risk score → narrative report.

- Demo: (add your Render URL)
- What it shows: Upload → KRIs → anomaly estimate → risk score → downloadable report

------------------------------------------------------------
## 9. UK Global Talent Evidence

This repository underpins the submission:

Evidence 4: Enterprise Risk Intelligence Engine  
by Ibrahim Akintunde Akinyera

Included:

- Full Evidence PDF
- Technical documentation
- Architecture diagrams
- Scoring logic diagrams
- Code showing ML + risk analytics engineering

Reviewed by:
Busayo Ezra Odukoya  
Senior Technology Risk Management Analyst  
CME Group

------------------------------------------------------------
## 10. Credits

Ibrahim Akintunde Akinyera – System Architect and Lead Engineer  
Busayo Ezra Odukoya – Risk-domain reviewer and technical validation

------------------------------------------------------------
## 11. License

MIT License
