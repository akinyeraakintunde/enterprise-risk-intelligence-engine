# TECH NATION EVIDENCE – Enterprise Risk Intelligence Engine

## Evidence Type
Technical Contribution – Applied AI, Cybersecurity Analytics, Risk Engineering

## Applicant
Ibrahim Akintunde Akinyera

------------------------------------------------------------
## 1. Overview

The Enterprise Risk Intelligence Engine is a Python-based system designed to analyse organisational log data, detect anomalies, score key risk indicators (KRIs), and generate explainable risk reports. It demonstrates strong engineering capability across machine learning, cybersecurity analytics, log processing, risk scoring, and automated reporting.

The system was architected and implemented by Ibrahim Akintunde Akinyera.  
Risk-domain validation was provided by **Busayo E. Odukoya**, Senior Technology Risk Management Analyst at CME Group, one of the world’s largest financial market infrastructure organisations.

This project is submitted as part of Ibrahim’s Technical Contribution evidence for the UK Global Talent Visa (Digital Technology).

------------------------------------------------------------
## 2. Problem & Motivation

Many SMEs lack the resources to run full cybersecurity or technology risk teams. Operational and cybersecurity risks are often assessed manually using spreadsheets or informal judgment. This leads to:

- inconsistent analysis across teams
- no repeatability or automation
- limited visibility into high-risk behaviours
- no structured prioritisation of risk events
- lack of transparency for audits and governance reviews

This project addresses these gaps by providing an automated and explainable risk scoring system.

------------------------------------------------------------
## 3. Technical Contribution Summary

### 3.1 System Architecture (Designed by Ibrahim Akinyera)
The system is composed of:

- **Log Ingestion Layer** – loads CSV log files and normalises fields.
- **Anomaly Detection Engine** – identifies unusual log behaviour using Isolation Forest.
- **KRI Scoring Engine** – computes weighted risk attributes (failed logins, error spikes, rare events, etc.).
- **Risk Aggregation Engine** – combines KRIs into a final risk score (0–100).
- **Risk Band Classifier** – maps scores to Low, Medium, or High.
- **Reporting Engine** – generates human-readable risk reports with narrative explanations.
- **Evidence and documentation** – diagrams, scoring logic, and architectural explanation.

### 3.2 Code Contributions (Fully implemented by Ibrahim)
Key modules:

- `src/anomaly_detector.py`  
- `src/risk_score_engine.py`  
- `src/risk_analyzer.py`  
- `src/report_generator.py`  
- `src/utils.py`

These modules contain:
- Data parsing and feature extraction
- ML-based anomaly scoring
- Deterministic KRI scoring logic
- Weight-based risk aggregation
- Automated generation of narrative text reports
- Flexible CLI-driven orchestration

### 3.3 Documentation & Evidence
Ibrahim produced full documentation:

- README.md – system overview, architecture, examples, run instructions
- Architecture diagrams (in docs/figures/)
- Scoring flow diagrams
- Sample generated reports
- Evidence_4_Enterprise_Risk_Intelligence_Engine_Ibrahim_Akinyera.pdf

------------------------------------------------------------
## 4. Role of External Reviewer

The scoring model, KRIs, thresholds, and governance relevance were **reviewed by Busayo E. Odukoya**, Senior Technology Risk Management Analyst at CME Group.

Busayo provided:
- validation of risk domains and KRIs  
- review of scoring thresholds and weights  
- alignment with enterprise governance practice  
- confirmation of the project’s real-world relevance  

All engineering, coding, design, and implementation work were done independently by Ibrahim.

------------------------------------------------------------
## 5. Impact

The system provides:

- consistent and automated risk evaluation  
- ML-driven anomaly detection for logs  
- explainable narrative risk reports  
- auditable scoring frameworks  
- governance-friendly outputs  
- an extendable design suitable for:
  - cybersecurity operations
  - EdTech or SME governance
  - internal audit support
  - fraud and anomaly analysis
  - IT incident monitoring

The engine demonstrates Ibrahim’s ability to design and build digital systems that combine machine learning, risk analytics, and enterprise governance concepts.

------------------------------------------------------------
## 6. Evidence Contained in This Repository

- Complete source code for the anomaly detection and risk scoring engine  
- Architecture diagram  
- Scoring logic diagram  
- Example risk reports  
- Input log data samples  
- Full README documentation  
- Full Evidence PDF  
- External technical validation (see recommendation letter from Busayo Odukoya)  

------------------------------------------------------------
## 7. Why This Meets Tech Nation’s Technical Contribution Criterion

- Clear demonstration of deep technical expertise  
- End-to-end ownership of a multi-component risk system  
- Strong real-world relevance (cybersecurity, compliance, log analytics)  
- Collaboration with a senior external reviewer  
- Production-style structure, documentation, and engineering maturity  
- Evidence of impact and future scalability

------------------------------------------------------------
## 8. Contact

Ibrahim Akintunde Akinyera  
Website: https://akinyeraakintunde.github.io  
GitHub: https://github.com/akinyeraakintunde  
Email: [your email here]