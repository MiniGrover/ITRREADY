"""Parse Zerodha Tax P&L XLSX into per-section DataFrames."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

TRADEWISE_SHEET_PREFIX = "Tradewise Exits"

SECTIONS_OF_INTEREST = (
    "Equity - Intraday",
    "Equity - Short Term",
    "Equity - Long Term",
)

EXPECTED_COLUMNS = (
    "Symbol", "ISIN", "Entry Date", "Exit Date", "Quantity",
    "Buy Value", "Sell Value", "Profit", "Period of Holding",
    "Fair Market Value", "Taxable Profit", "Turnover",
)


@dataclass
class ParsedTaxFile:
    client_id: str | None
    client_name: str | None
    pan: str | None
    period_label: str | None
    sections: dict[str, pd.DataFrame]


def _find_tradewise_sheet(xls: pd.ExcelFile) -> str:
    for name in xls.sheet_names:
        if name.startswith(TRADEWISE_SHEET_PREFIX):
            return name
    raise ValueError(
        f"No sheet starting with '{TRADEWISE_SHEET_PREFIX}' found. "
        f"Sheets present: {xls.sheet_names}"
    )


def _extract_metadata(df: pd.DataFrame) -> dict[str, str | None]:
    meta: dict[str, str | None] = {
        "client_id": None, "client_name": None, "pan": None, "period_label": None,
    }
    for i in range(min(15, len(df))):
        key = df.iat[i, 1]
        val = df.iat[i, 2] if df.shape[1] > 2 else None
        if not isinstance(key, str):
            continue
        k = key.strip().lower()
        if k == "client id":
            meta["client_id"] = str(val) if pd.notna(val) else None
        elif k == "client name":
            meta["client_name"] = str(val) if pd.notna(val) else None
        elif k == "pan":
            meta["pan"] = str(val) if pd.notna(val) else None
        elif k.startswith("tradewise exits"):
            meta["period_label"] = key.strip()
    return meta


def _find_section_starts(df: pd.DataFrame) -> dict[str, int]:
    """Return {section_name: row_index_of_section_header}."""
    starts: dict[str, int] = {}
    for i in range(len(df)):
        val = df.iat[i, 1]
        if isinstance(val, str) and val.strip() in SECTIONS_OF_INTEREST:
            starts[val.strip()] = i
    return starts


def _read_section(df: pd.DataFrame, header_row_idx: int) -> pd.DataFrame:
    """Read a single section starting at the row holding 'Symbol','ISIN',...

    Stops at the first row where the Symbol column is blank.
    """
    header = df.iloc[header_row_idx, 1:1 + len(EXPECTED_COLUMNS)].tolist()
    rows = []
    for i in range(header_row_idx + 1, len(df)):
        symbol = df.iat[i, 1]
        if pd.isna(symbol) or (isinstance(symbol, str) and not symbol.strip()):
            break
        rows.append(df.iloc[i, 1:1 + len(EXPECTED_COLUMNS)].tolist())
    section = pd.DataFrame(rows, columns=header)

    for col in ("Entry Date", "Exit Date"):
        if col in section.columns:
            section[col] = pd.to_datetime(section[col], errors="coerce").dt.date
    numeric_cols = (
        "Quantity", "Buy Value", "Sell Value", "Profit",
        "Period of Holding", "Fair Market Value", "Taxable Profit", "Turnover",
    )
    for col in numeric_cols:
        if col in section.columns:
            section[col] = pd.to_numeric(section[col], errors="coerce")
    return section


def parse_zerodha_xlsx(path: str | Path) -> ParsedTaxFile:
    """Entry point. Returns metadata + DataFrames keyed by section name."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)

    xls = pd.ExcelFile(path)
    sheet = _find_tradewise_sheet(xls)
    raw = pd.read_excel(path, sheet_name=sheet, header=None)

    meta = _extract_metadata(raw)
    section_starts = _find_section_starts(raw)

    sections: dict[str, pd.DataFrame] = {}
    for section_name, title_row in section_starts.items():
        header_row = title_row + 2
        if header_row >= len(raw):
            sections[section_name] = pd.DataFrame(columns=list(EXPECTED_COLUMNS))
            continue
        sections[section_name] = _read_section(raw, header_row)

    for s in SECTIONS_OF_INTEREST:
        sections.setdefault(s, pd.DataFrame(columns=list(EXPECTED_COLUMNS)))

    return ParsedTaxFile(
        client_id=meta["client_id"],
        client_name=meta["client_name"],
        pan=meta["pan"],
        period_label=meta["period_label"],
        sections=sections,
    )
