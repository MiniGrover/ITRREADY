"""Produce CA-facing CSV outputs from an AggregatedResult."""
from __future__ import annotations

import io
import zipfile

import pandas as pd

from .aggregator import AggregatedResult


def summary_dataframe(result: AggregatedResult) -> pd.DataFrame:
    rows = [
        ["Equity - Intraday (Speculative)", result.intraday.trade_count,
         result.intraday.total_buy_value, result.intraday.total_sell_value,
         result.intraday.gross_profit, result.intraday.turnover,
         "ITR-3 Schedule BP"],
        ["Equity - Short Term (Sec 111A)", result.short_term.trade_count,
         result.short_term.total_buy_value, result.short_term.total_sell_value,
         result.short_term.taxable_profit, result.short_term.turnover,
         "ITR-2 Schedule CG-A1"],
        ["Equity - Long Term (Sec 112A)", result.long_term.trade_count,
         result.long_term.total_buy_value, result.long_term.total_sell_value,
         result.long_term.taxable_profit, result.long_term.turnover,
         "ITR-2 Schedule CG-B1 (per-scrip)"],
    ]
    return pd.DataFrame(rows, columns=[
        "Section", "Trade Count", "Total Buy Value", "Total Sell Value",
        "Taxable / Gross Profit", "Turnover", "ITR Destination",
    ])


def charges_dataframe(result: AggregatedResult) -> pd.DataFrame:
    rows = [(k, v) for k, v in sorted(result.charges.breakdown.items())]
    rows.append(("__TOTAL_DEDUCTIBLE__", result.charges.deductible_total))
    rows.append(("__TOTAL_STT_NOT_DEDUCTIBLE__", result.charges.stt_total))
    return pd.DataFrame(rows, columns=["Charge", "Amount"])


def ltcg_per_scrip_dataframe(result: AggregatedResult) -> pd.DataFrame:
    if not result.ltcg_per_scrip:
        return pd.DataFrame(columns=[
            "Symbol", "ISIN", "Quantity", "Sale Value",
            "Buy Value", "Fair Market Value", "Cost for 112A", "Taxable LTCG",
        ])
    return pd.DataFrame([{
        "Symbol": r.symbol, "ISIN": r.isin, "Quantity": r.quantity,
        "Sale Value": r.sell_value, "Buy Value": r.buy_value,
        "Fair Market Value": r.fair_market_value,
        "Cost for 112A": r.cost_for_112a, "Taxable LTCG": r.taxable_ltcg,
    } for r in result.ltcg_per_scrip])


def build_zip_bundle(result: AggregatedResult, intraday_df: pd.DataFrame,
                     st_df: pd.DataFrame, lt_df: pd.DataFrame) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("01_summary.csv", summary_dataframe(result).to_csv(index=False))
        z.writestr("02_charges.csv", charges_dataframe(result).to_csv(index=False))
        z.writestr("03_ltcg_per_scrip_112A.csv",
                   ltcg_per_scrip_dataframe(result).to_csv(index=False))
        z.writestr("04_intraday_trades.csv", intraday_df.to_csv(index=False))
        z.writestr("05_short_term_trades.csv", st_df.to_csv(index=False))
        z.writestr("06_long_term_trades.csv", lt_df.to_csv(index=False))
        z.writestr("07_notes.txt", "\n".join(f"- {n}" for n in result.notes))
    buf.seek(0)
    return buf.read()
