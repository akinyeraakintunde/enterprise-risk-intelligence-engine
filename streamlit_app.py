from __future__ import annotations

import io
import json
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Optional

import pandas as pd
import streamlit as st

# -----------------------------
# Configuration (edit if needed)
# -----------------------------
DEFAULT_TIME_COLS = ["timestamp", "time", "event_time", "created_at", "date"]
DEFAULT_MESSAGE_COLS = ["message", "event", "log", "description"]
DEFAULT_NUMERIC_COLS_HINT = ["latency_ms", "duration_ms", "error_count", "requests", "status_code"]

# -----------------------------
# Core demo logic (simple + safe)
# -----------------------------
@dataclass
class RiskResult:
    anomaly_rate: float
    risk_score: float
    kris: Dict[str, float]
    narrative: str
    meta: Dict[str, Any]


def _pick_first_existing(columns, candidates) -> Optional[str]:
    lower_map = {c.lower(): c for c in columns}
    for cand in candidates:
        if cand.lower() in lower_map:
            return lower_map[cand.lower()]
    return None


def compute_kris(df: pd.DataFrame) -> Dict[str, float]:
    """
    Tiny KRI set that works for many log-like CSVs.
    You can replace this later with your real KRIs.
    """
    cols = df.columns

    time_col = _pick_first_existing(cols, DEFAULT_TIME_COLS)
    msg_col = _pick_first_existing(cols, DEFAULT_MESSAGE_COLS)

    # 1) Error rate (based on message keywords or status_code if present)
    error_rate = 0.0
    if "status_code" in [c.lower() for c in cols]:
        status_col = _pick_first_existing(cols, ["status_code"])
        # treat 4xx/5xx as errors
        s = pd.to_numeric(df[status_col], errors="coerce")
        error_rate = float((s >= 400).fillna(False).mean())
    elif msg_col:
        m = df[msg_col].astype(str).str.lower()
        error_rate = float(m.str.contains("error|failed|exception|timeout").mean())

    # 2) Volume spike proxy (rows per hour vs average) if time exists
    volume_spike = 0.0
    if time_col:
        t = pd.to_datetime(df[time_col], errors="coerce", utc=True)
        temp = df.copy()
        temp["_t"] = t
        temp = temp.dropna(subset=["_t"])
        if not temp.empty:
            per_hour = temp.set_index("_t").resample("1H").size()
            if len(per_hour) >= 3:
                avg = per_hour.mean()
                mx = per_hour.max()
                volume_spike = float((mx / avg) if avg > 0 else 0.0)

    # 3) Missingness (data quality risk)
    missingness = float(df.isna().mean().mean())

    # 4) Numeric outlier intensity (quick z-score-ish proxy)
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if not numeric_cols:
        # try to coerce hinted numeric columns
        for h in DEFAULT_NUMERIC_COLS_HINT:
            if h in [c.lower() for c in cols]:
                real = _pick_first_existing(cols, [h])
                df[real] = pd.to_numeric(df[real], errors="coerce")
        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()

    outlier_intensity = 0.0
    if numeric_cols:
        num = df[numeric_cols].copy()
        num = num.replace([float("inf"), float("-inf")], pd.NA)
        num = num.dropna()
        if not num.empty:
            # ratio of values beyond 3 std dev (rough)
            z = (num - num.mean()) / (num.std(ddof=0) + 1e-9)
            outlier_intensity = float((z.abs() > 3).mean().mean())

    return {
        "error_rate": round(error_rate, 4),
        "volume_spike_ratio": round(volume_spike, 4),
        "missingness": round(missingness, 4),
        "numeric_outlier_intensity": round(outlier_intensity, 4),
    }


def compute_anomaly_rate(df: pd.DataFrame) -> float:
    """
    Tiny heuristic anomaly: if error keywords OR high outlier intensity OR missingness high.
    Replace later with your IsolationForest outputs if you like.
    """
    kris = compute_kris(df)
    flags = 0
    if kris["error_rate"] > 0.05:
        flags += 1
    if kris["numeric_outlier_intensity"] > 0.02:
        flags += 1
    if kris["missingness"] > 0.15:
        flags += 1

    # map flags -> pseudo anomaly rate
    return {0: 0.01, 1: 0.05, 2: 0.15, 3: 0.30}.get(flags, 0.10)


def compute_risk_score(kris: Dict[str, float], anomaly_rate: float) -> float:
    """
    Weighted score 0..100. Tune weights later.
    """
    score_0_1 = (
        0.40 * min(1.0, kris["error_rate"] / 0.20) +
        0.25 * min(1.0, kris["numeric_outlier_intensity"] / 0.10) +
        0.20 * min(1.0, kris["missingness"] / 0.30) +
        0.15 * min(1.0, anomaly_rate / 0.30)
    )
    return round(float(score_0_1 * 100.0), 2)


def build_narrative(kris: Dict[str, float], anomaly_rate: float, risk_score: float) -> str:
    level = "LOW"
    if risk_score >= 70:
        level = "HIGH"
    elif risk_score >= 40:
        level = "MEDIUM"

    drivers = []
    if kris["error_rate"] > 0.05:
        drivers.append(f"elevated error rate ({kris['error_rate']*100:.1f}%)")
    if kris["volume_spike_ratio"] > 1.5:
        drivers.append(f"traffic/volume spike (x{kris['volume_spike_ratio']:.2f})")
    if kris["numeric_outlier_intensity"] > 0.02:
        drivers.append(f"unusual numeric outliers ({kris['numeric_outlier_intensity']*100:.1f}%)")
    if kris["missingness"] > 0.15:
        drivers.append(f"data-quality issues (missingness {kris['missingness']*100:.1f}%)")

    driver_text = "No dominant risk drivers detected." if not drivers else "Key drivers: " + ", ".join(drivers) + "."

    return (
        f"Overall risk level: {level} (score={risk_score}/100). "
        f"Estimated anomaly rate: {anomaly_rate*100:.1f}%. "
        f"{driver_text} "
        f"Recommended next step: validate top anomalies, confirm expected traffic patterns, and review recent changes/releases."
    )


def make_report(df: pd.DataFrame, result: RiskResult) -> str:
    # Plain text report (super simple + downloadable)
    lines = []
    lines.append("ENTERPRISE RISK INTELLIGENCE — DEMO REPORT")
    lines.append("=" * 44)
    lines.append(f"Generated: {datetime.utcnow().isoformat()}Z")
    lines.append(f"Rows analysed: {len(df):,}")
    lines.append("")
    lines.append(f"Risk score: {result.risk_score}/100")
    lines.append(f"Anomaly rate (est.): {result.anomaly_rate*100:.1f}%")
    lines.append("")
    lines.append("KRIs")
    for k, v in result.kris.items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("Narrative")
    lines.append(result.narrative)
    lines.append("")
    lines.append("Meta")
    lines.append(json.dumps(result.meta, indent=2))
    return "\n".join(lines)


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Risk Intelligence Engine — Live Demo", layout="wide")

st.title("Enterprise Risk Intelligence Engine — Live Demo")
st.caption("Upload a CSV of logs/events → KRIs + anomaly estimate → risk score → narrative report")

with st.sidebar:
    st.header("Upload")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    st.markdown("---")
    st.header("Scoring")
    st.write("This demo uses lightweight heuristics so it runs anywhere.")
    st.write("You can swap in IsolationForest later without changing the UI.")

if not uploaded:
    st.info("Upload a CSV to get started.")
    st.stop()

# Read CSV safely
try:
    df = pd.read_csv(uploaded)
except Exception:
    uploaded.seek(0)
    df = pd.read_csv(uploaded, encoding="latin-1")

st.subheader("Preview")
st.dataframe(df.head(20), use_container_width=True)

st.subheader("Risk Results")
kris = compute_kris(df)
anomaly_rate = compute_anomaly_rate(df)
risk_score = compute_risk_score(kris, anomaly_rate)
narrative = build_narrative(kris, anomaly_rate, risk_score)

result = RiskResult(
    anomaly_rate=anomaly_rate,
    risk_score=risk_score,
    kris=kris,
    narrative=narrative,
    meta={"columns": list(df.columns), "shape": list(df.shape)},
)

col1, col2, col3 = st.columns(3)
col1.metric("Risk score", f"{risk_score}/100")
col2.metric("Anomaly rate (est.)", f"{anomaly_rate*100:.1f}%")
col3.metric("Rows analysed", f"{len(df):,}")

st.markdown("### KRIs")
st.json(kris)

st.markdown("### Narrative")
st.write(narrative)

report_text = make_report(df, result)
st.markdown("### Download report")
st.download_button(
    label="Download report (TXT)",
    data=report_text.encode("utf-8"),
    file_name="risk_report.txt",
    mime="text/plain",
)