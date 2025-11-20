# Enterprise Risk Intelligence Engine

Enterprise Risk Intelligence Engine is a production-style Python project for scoring, monitoring, and explaining enterprise-level risks for SMEs and digital businesses.

The system ingests structured risk data (controls, incidents, assets, financial and operational indicators), applies a configurable rules and scoring engine, and produces transparent risk scores and narrative reports that can be consumed by business stakeholders or integrated into dashboards.

The project was designed and implemented by Ibrahim Akintunde Akinyera (Founder, NxtAbroad) with strategic risk input from Busayo E. Odukoya (Senior Technology Risk Management Analyst, CME Group).

## 1. Why this project exists

Most SMEs do not have dedicated risk teams and typically rely on spreadsheets or inconsistent judgement. This results in:

- Inconsistent assessment of identical risks
- Poor visibility of aggregated exposure
- No clear audit trail for decisions
- Difficulty aligning technology risk with business, policy, and regulatory expectations

This engine solves these problems by providing:

- A repeatable and transparent scoring framework
- Explainable and traceable outputs
- A foundation for automation and continuous monitoring
- A governance-ready artefact for risk, audit, and compliance teams

## 2. High-level architecture

The engine follows a structured pipeline:

1. Input Layer  
   Structured CSV files or risk registers.

2. Feature Builder  
   Normalises raw fields, derives metrics, and encodes categorical inputs.

3. Rules and Scoring Engine  
   Applies deterministic rules, weightings, and thresholds per domain.

4. Risk Classifier  
   Converts numeric scores into qualitative bands (Low, Medium, High, Critical).

5. Reporting Layer  
   Generates detailed risk outputs for dashboards and BI tools.

Architecture diagrams are stored in:
docs/figures/

## 3. Key features

- Fully configurable risk rules via YAML
- Domain-based scoring (governance, technology, financial, compliance)
- Deterministic explainable scoring (no black-box ML)
- Clear separation of modules and logic
- CLI execution for business users
- Extensible into API and dashboard interfaces

## 4. Repository structure

enterprise-risk-intelligence-engine/
|
├── data/                     Example datasets
├── docs/figures/            Architecture diagrams
├── src/
│   ├── risk_engine/         Core scoring logic
│   ├── reporting/           Report generation
│   └── cli_main.py          CLI entrypoint
|
├── notebooks/               Exploratory analysis
├── tests/                   Optional unit tests
|
├── README.md
├── TECH_NATION_EVIDENCE.md
├── requirements.txt
└── LICENSE

## 5. Getting started

### 5.1 Installation

git clone https://github.com/akinyeraakintunde/enterprise-risk-intelligence-engine.git
cd enterprise-risk-intelligence-engine

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### 5.2 Run the engine

python -m src.cli_main --input data/sample_risk_register.csv --config configs/default_rules.yaml --output outputs/risk_scored.csv

Arguments:
--input: CSV dataset
--config: YAML config with rules and weights
--output: Path for the scored file

The output CSV contains:
- Final risk scores
- Risk band classification
- Domain sub-scores
- Flags and narrative notes

## 6. Configuration model (YAML)

Example rule configuration:

weights:
  governance: 0.25
  technology: 0.35
  financial: 0.20
  compliance: 0.20

thresholds:
  high_risk_score: 75
  critical_risk_score: 90

rules:
  - id: weak_password_policy
    domain: technology
    condition: "password_policy_strength == 'weak'"
    impact: +15
    message: "Weak password policy increases technology risk."

  - id: missing_audit_trail
    domain: governance
    condition: "has_audit_trail == 0"
    impact: +10
    message: "Absence of audit trail raises governance risk."

## 7. Development notes

- Python 3.10+
- Type hints used extensively
- Linting recommended (flake8 or ruff)
- Modular architecture

### Testing

pytest

Tests validate rule correctness, score aggregation, and edge cases.

## 8. Using this engine in real organisations

1. Define the risk entities (vendors, customers, systems, departments)
2. Map available data (KYC, due diligence, audit logs, controls)
3. Set domain weightings aligned to enterprise risk appetite
4. Translate policies into rule conditions
5. Calibrate using real historical assessments
6. Embed engine outputs into governance processes

## 9. UK Global Talent relevance

This repository supports Ibrahim Akintunde Akinyera’s Technical Contribution evidence for the UK Global Talent Visa (Digital Technology). It demonstrates:

- Full end-to-end engineering ownership
- Deep application of risk management domain knowledge
- Collaboration with a senior risk professional (Busayo Odukoya)
- Strong documentation, diagrams, and governance alignment
- A reusable engine for SMEs and startups requiring automated risk evaluation

Supporting evidence is detailed in:
TECH_NATION_EVIDENCE.md

## 10. Credits

Ibrahim Akintunde Akinyera – Architect and Lead Developer  
Busayo E. Odukoya – Risk Expertise and Validation

## 11. License

Released under the MIT License.