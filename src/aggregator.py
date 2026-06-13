"""Aggregate parsed Zerodha sections into ITR-ready figures.

v1 design choice: charges are pulled from the summary "Equity and Non Equity"
sheet as a single aggregate (option B). CA applies them at filing time. STT is
listed separately because it is NOT deductible against capital gains under
Sections 111A / 112A.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from .parser import ParsedTaxFile

SUMMARY_SHEET = "Equity and Non Equity"

LTCG_EXEMPTION_LIMIT = 125_000

DEDUCTIBLE_CHARGE_LABELS = {
    "exchange transaction charges",
    "integrated gst",
    "central gst",
    "state gst",
    "sebi turnover fees",
    "stamp duty",
    "brokerage",
    "ipft",
    "clearing charges",
}

NON_DEDUCTIBLE_LABELS = {"securities transaction tax"}


@dataclass
class SectionAggregate:
    section: str
    trade_count: int
    total_buy_value: float
    total_sell_value: float
    gross_profit: float
    taxable_profit: float
    turnover: float


@dataclass
class Charges:
    deductible_total: float
    stt_total: float
    breakdown: dict[str, float] = field(default_factory=dict)


@dataclass
class LTCGRow:
    symbol: str
    isin: str
    quantity: float
    sell_value: float
    buy_value: float
    fair_market_value: float
    cost_for_112a: float
    taxable_ltcg: float


@dataclass
class AggregatedResult:
    intraday: SectionAggregate
    short_term: SectionAggregate
    long_term: SectionAggregate
    ltcg_per_scrip: list[LTCGRow]
    charges: Charges
    ltcg_after_exemption: float
    notes: list[str] = field(default_factory=list)


def _aggregate_section(section_name: str, df: pd.DataFrame) -> SectionAggregate:
    if df.empty:
        return SectionAggregate(section_name, 0, 0.0, 0.0, 0.0, 0.0, 0.0)
    return SectionAggregate(
        section=section_name,
        trade_count=len(df),
        total_buy_value=float(df["Buy Value"].sum()),
        total_sell_value=float(df["Sell Value"].sum()),
        gross_profit=float(df["Profit"].sum()),
        taxable_profit=float(df["Taxable Profit"].sum()),
        turnover=float(df["Turnover"].sum()),
    )


def _read_charges(xlsx_path: str | Path) -> Charges:
    raw = pd.read_excel(xlsx_path, sheet_name=SUMMARY_SHEET, header=None)
    deductible = 0.0
    stt = 0.0
    breakdown: dict[str, float] = {}

    in_charges_section = False
    for i in range(len(raw)):
        label = raw.iat[i, 1]
        amount = raw.iat[i, 2] if raw.shape[1] > 2 else None
        if isinstance(label, str) and label.strip().lower() == "charges":
            in_charges_section = True
            continue
        if not in_charges_section or not isinstance(label, str):
            continue
        clean = label.strip().rstrip(" -Z").lower().replace(" - z", "").strip()
        if not pd.notna(amount) or not isinstance(amount, (int, float)):
            if isinstance(label, str) and label.strip().lower() == "other charges":
                break
            continue
        amt = float(amount)
        breakdown[clean] = breakdown.get(clean, 0.0) + amt
        if any(k in clean for k in DEDUCTIBLE_CHARGE_LABELS):
            deductible += amt
        elif any(k in clean for k in NON_DEDUCTIBLE_LABELS):
            stt += amt

    return Charges(deductible_total=deductible, stt_total=stt, breakdown=breakdown)


def _build_ltcg_per_scrip(df: pd.DataFrame) -> list[LTCGRow]:
    rows: list[LTCGRow] = []
    if df.empty:
        return rows
    for _, r in df.iterrows():
        buy = float(r["Buy Value"])
        fmv = float(r["Fair Market Value"]) if pd.notna(r["Fair Market Value"]) else 0.0
        sell = float(r["Sell Value"])
        cost = max(buy, fmv) if fmv > 0 else buy
        rows.append(LTCGRow(
            symbol=str(r["Symbol"]),
            isin=str(r["ISIN"]),
            quantity=float(r["Quantity"]),
            sell_value=sell,
            buy_value=buy,
            fair_market_value=fmv,
            cost_for_112a=cost,
            taxable_ltcg=float(r["Taxable Profit"]),
        ))
    return rows


def aggregate(parsed: ParsedTaxFile, xlsx_path: str | Path) -> AggregatedResult:
    sections = parsed.sections
    intraday = _aggregate_section("Equity - Intraday", sections["Equity - Intraday"])
    short_term = _aggregate_section("Equity - Short Term", sections["Equity - Short Term"])
    long_term = _aggregate_section("Equity - Long Term", sections["Equity - Long Term"])
    ltcg_rows = _build_ltcg_per_scrip(sections["Equity - Long Term"])
    charges = _read_charges(xlsx_path)

    ltcg_after_exemption = max(0.0, long_term.taxable_profit - LTCG_EXEMPTION_LIMIT)

    notes: list[str] = []
    notes.append(
        "Charges shown here are aggregate across equity segments. CA must apportion "
        "between intraday (business expense) and ST/LT (deduction from gains) at filing."
    )
    notes.append(
        "STT is NOT deductible against capital gains under Sections 111A and 112A."
    )
    notes.append(
        f"LTCG ₹1.25L exemption under Section 112A applied: gross "
        f"₹{long_term.taxable_profit:,.2f} → taxable ₹{ltcg_after_exemption:,.2f}"
    )

    return AggregatedResult(
        intraday=intraday,
        short_term=short_term,
        long_term=long_term,
        ltcg_per_scrip=ltcg_rows,
        charges=charges,
        ltcg_after_exemption=ltcg_after_exemption,
        notes=notes,
    )
