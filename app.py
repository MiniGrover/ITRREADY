"""Streamlit entry point for the broker tax tool v1."""
from __future__ import annotations

import os
import tempfile

import streamlit as st

from src.aggregator import aggregate
from src.output import (
    build_zip_bundle, charges_dataframe, ltcg_per_scrip_dataframe,
    summary_dataframe,
)
from src.parser import parse_zerodha_xlsx

st.set_page_config(page_title="ITRReady", page_icon="📊", layout="wide")

FEEDBACK_EMAIL = os.environ.get("FEEDBACK_EMAIL", "minikochar8@gmail.com")

st.title("ITRReady")
st.caption(
    "Zerodha Tax P&L XLSX → ITR-ready capital-gains figures. "
    "Equity intraday, short term (Sec 111A), and long term (Sec 112A). "
    "v1 — F&O, currency, commodity, and mutual funds not yet supported."
)

st.info(
    "**Free beta for the first 50 CAs.** No signup, no payment. "
    "All we ask: after you try it, email one line of feedback to "
    f"[{FEEDBACK_EMAIL}](mailto:{FEEDBACK_EMAIL}?subject=ITRReady%20feedback) — "
    "what worked, what broke, what you wish it did."
)

uploaded = st.file_uploader(
    "Zerodha Tax P&L (.xlsx)",
    type=["xlsx"],
    help="Console → Reports → Tax P&L → download the XLSX for the relevant FY",
)

if not uploaded:
    st.info("Drop your Tax P&L XLSX above to begin. Nothing is stored — file lives in memory only.")
    st.stop()

with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
    tmp.write(uploaded.read())
    tmp_path = tmp.name

try:
    parsed = parse_zerodha_xlsx(tmp_path)
    result = aggregate(parsed, tmp_path)
except Exception as exc:
    st.error(f"Could not parse file: {exc}")
    st.exception(exc)
    st.stop()

st.success(f"Parsed: {parsed.client_name or 'Unknown'} — {parsed.period_label or 'period unknown'}")

st.subheader("Summary")
st.dataframe(summary_dataframe(result), use_container_width=True, hide_index=True)

col1, col2, col3 = st.columns(3)
col1.metric("Intraday Profit (Speculative)", f"₹{result.intraday.gross_profit:,.2f}")
col2.metric("Short-Term Capital Gain", f"₹{result.short_term.taxable_profit:,.2f}")
col3.metric("Long-Term (after ₹1.25L exempt)", f"₹{result.ltcg_after_exemption:,.2f}")

st.subheader("Charges (aggregate)")
st.dataframe(charges_dataframe(result), use_container_width=True, hide_index=True)
st.caption(
    f"Deductible against gains: ₹{result.charges.deductible_total:,.2f} • "
    f"STT (not deductible): ₹{result.charges.stt_total:,.2f}"
)

if result.ltcg_per_scrip:
    st.subheader("LTCG per scrip (for ITR-2 Schedule CG-B1)")
    st.dataframe(ltcg_per_scrip_dataframe(result), use_container_width=True, hide_index=True)

with st.expander("Notes for the CA"):
    for n in result.notes:
        st.markdown(f"- {n}")

st.divider()
st.subheader("Download ITR-ready CSVs")

intraday_df = parsed.sections["Equity - Intraday"]
st_df = parsed.sections["Equity - Short Term"]
lt_df = parsed.sections["Equity - Long Term"]
bundle = build_zip_bundle(result, intraday_df, st_df, lt_df)
st.download_button(
    "Download tax-bundle.zip",
    data=bundle,
    file_name=f"tax-bundle-{parsed.client_id or 'client'}.zip",
    mime="application/zip",
    type="primary",
)
st.caption(
    f"After you try it: one line of feedback to "
    f"[{FEEDBACK_EMAIL}](mailto:{FEEDBACK_EMAIL}?subject=ITRReady%20feedback) "
    "is what keeps this free."
)

try:
    os.unlink(tmp_path)
except OSError:
    pass
