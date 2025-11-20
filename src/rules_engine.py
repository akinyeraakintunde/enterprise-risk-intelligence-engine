from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class CategoryScore:
    name: str
    score: int
    notes: List[str]


def clamp(value: float, minimum: int = 0, maximum: int = 100) -> int:
    """Clamp any numeric value between 0 and 100."""
    return int(max(minimum, min(maximum, round(value))))


# ------------------------------------------------------------
# Financial Risk Scoring
# ------------------------------------------------------------
def score_financial(section: Dict[str, Any]) -> CategoryScore:
    notes = []
    score = 60

    balance = float(section.get("bank_balance", 0))
    required = float(section.get("minimum_required", 0))
    regular_income = bool(section.get("has_regular_income", False))
    unexplained_deposits = bool(section.get("recent_large_unexplained_deposits", False))

    # Ratio logic
    ratio = balance / required if required > 0 else 0

    if ratio >= 1.2:
        score += 20
        notes.append("Bank balance is comfortably above the required minimum.")
    elif ratio >= 1.0:
        score += 10
        notes.append("Bank balance meets the required minimum.")
    elif ratio >= 0.8:
        score -= 10
        notes.append("Bank balance is slightly below the required minimum.")
    else:
        score -= 25
        notes.append("Bank balance is significantly below the required minimum.")

    if regular_income:
        score += 10
        notes.append("Applicant has regular income.")
    else:
        notes.append("No regular income detected.")

    if unexplained_deposits:
        score -= 25
        notes.append("Large unexplained deposits detected.")

    return CategoryScore("financial", clamp(score), notes)


# ------------------------------------------------------------
# Documentation Scoring
# ------------------------------------------------------------
def score_documentation(section: Dict[str, Any]) -> CategoryScore:
    notes = []
    score = 70

    all_docs = bool(section.get("all_required_documents_provided", False))
    verified = bool(section.get("documents_verified", False))
    inconsistencies = int(section.get("inconsistencies_found", 0))

    if all_docs:
        score += 15
        notes.append("All required documents are provided.")
    else:
        score -= 30
        notes.append("Missing required documents.")

    if verified:
        score += 10
        notes.append("Documents successfully verified.")
    else:
        notes.append("Documents not fully verified.")

    if inconsistencies > 2:
        score -= 20
        notes.append("Multiple inconsistencies found.")
    elif inconsistencies > 0:
        score -= 10
        notes.append("Some inconsistencies detected.")

    return CategoryScore("documentation", clamp(score), notes)


# ------------------------------------------------------------
# Eligibility Scoring
# ------------------------------------------------------------
def score_eligibility(section: Dict[str, Any]) -> CategoryScore:
    notes = []
    score = 60

    meets_min = bool(section.get("meets_minimum_criteria", False))
    gpa = float(section.get("gpa", 0))
    required_gpa = float(section.get("required_gpa", 0))
    gap_years = float(section.get("gap_years", 0))

    if meets_min:
        score += 10
        notes.append("Meets minimum eligibility requirements.")
    else:
        score -= 30
        notes.append("Does not meet minimum eligibility requirements.")

    if required_gpa > 0:
        ratio = gpa / required_gpa
        if ratio >= 1.2:
            score += 20
            notes.append("Academic performance significantly above requirement.")
        elif ratio >= 1.0:
            score += 10
            notes.append("Academic performance meets requirement.")
        else:
            score -= 10
            notes.append("Academic performance below requirement.")

    if gap_years > 3:
        score -= 20
        notes.append("Large gap in study/work history.")
    elif gap_years > 1:
        score -= 10
        notes.append("Moderate gap in study/work history.")

    return CategoryScore("eligibility", clamp(score), notes)


# ------------------------------------------------------------
# Compliance Risk Scoring
# ------------------------------------------------------------
def score_compliance(section: Dict[str, Any]) -> CategoryScore:
    notes = []
    score = 100

    refusals = int(section.get("previous_visa_refusals", 0))
    adverse = bool(section.get("adverse_immigration_history", False))
    sanctions = bool(section.get("sanctions_or_watchlists", False))

    if refusals > 1:
        score -= 40
        notes.append("Multiple previous refusals recorded.")
    elif refusals == 1:
        score -= 20
        notes.append("Single previous refusal recorded.")

    if adverse:
        score -= 40
        notes.append("Adverse immigration history detected.")

    if sanctions:
        score -= 50
        notes.append("Applicant appears on sanctions or watchlists.")

    if score == 100:
        notes.append("No compliance issues detected.")

    return CategoryScore("compliance", clamp(score), notes)


# ------------------------------------------------------------
# Behaviour Scoring
# ------------------------------------------------------------
def score_behaviour(section: Dict[str, Any]) -> CategoryScore:
    notes = []
    score = 60

    consistency = float(section.get("response_consistency_score", 0.5))
    missed = int(section.get("missed_deadlines", 0))
    suspicious = bool(section.get("suspicious_communication", False))

    score += (consistency - 0.5) * 40

    if missed > 3:
        score -= 20
        notes.append("Multiple missed deadlines.")
    elif missed > 0:
        score -= 10
        notes.append("Some deadlines missed.")

    if suspicious:
        score -= 25
        notes.append("Suspicious communication patterns detected.")

    return CategoryScore("behaviour", clamp(score), notes)


# ------------------------------------------------------------
# Main scoring aggregator
# ------------------------------------------------------------
def score_all_categories(profile: Dict[str, Any]):
    financial = score_financial(profile.get("financial", {}))
    documentation = score_documentation(profile.get("documentation", {}))
    eligibility = score_eligibility(profile.get("eligibility", {}))
    compliance = score_compliance(profile.get("compliance", {}))
    behaviour = score_behaviour(profile.get("behaviour", {}))

    scores = {
        "financial": financial.score,
        "documentation": documentation.score,
        "eligibility": eligibility.score,
        "compliance": compliance.score,
        "behaviour": behaviour.score,
    }

    notes = {
        "financial": financial.notes,
        "documentation": documentation.notes,
        "eligibility": eligibility.notes,
        "compliance": compliance.notes,
        "behaviour": behaviour.notes,
    }

    return scores, notes