---
layout: default
title: ITRReady — Zerodha Tax P&L to ITR-ready figures
description: Convert a Zerodha Tax P&L XLSX into ITR Schedule CG and Schedule BP figures in 30 seconds. Free beta for the first 50 CAs.
---

# Zerodha Tax P&L → ITR-ready numbers in 30 seconds

Built for CAs who file 50+ ITR-2 / ITR-3 returns each season. Drop the client's XLSX, get the six numbers that go straight into Schedule CG and Schedule BP. STT correctly excluded. ₹1.25L Section 112A exemption applied. Per-scrip LTCG table for grandfathering.

### [→ Try free with your file (no signup)](https://itrready-dirxr3fop2qs9sfsgkctkm.streamlit.app/)

*Free beta for the first 50 CAs. No signup, no payment, no data stored.*

---

## The problem

You open the Zerodha Tax P&L for one client:

- 333 rows across Intraday, Short Term, Long Term, Buyback, F&O
- Charges split across 10 categories — half deductible, half not
- STT mistakes are the #1 reason CG figures get questioned in scrutiny
- And you have 199 more clients waiting

You know exactly what numbers ITR needs. The XLSX is just in the way.

---

## What you get

A ZIP of seven CSVs, ready to paste into the ITR utility or your filing software:

| File | What it is |
|---|---|
| `01_summary.csv` | The six numbers — STCG, LTCG, intraday P&L, deductible charges, turnover |
| `02_charges.csv` | Brokerage / GST / exchange charges (deductible) vs STT (not deductible) |
| `03_ltcg_per_scrip.csv` | Per-scrip table with FMV grandfathering applied for Section 112A |
| `04_intraday_trades.csv` | Speculative business detail for Schedule BP |
| `05_short_term_trades.csv` | STCG detail with holding period |
| `06_long_term_trades.csv` | LTCG detail with FMV column populated |
| `07_notes.txt` | Apportionment, audit threshold, and exemption notes |

---

## How it works

1. **Upload** the client's Zerodha Tax P&L XLSX
2. **Verify** the summary preview against your records
3. **Download** the seven-file ZIP

The XLSX is parsed in memory in your browser session. No account. No PAN logged. No data retained when you close the tab.

### [→ Open the tool](https://itrready-dirxr3fop2qs9sfsgkctkm.streamlit.app/)

---

## Pricing

**Free during beta** — first 50 CAs, no payment, unlimited files.

In exchange: email one line of feedback after you try it. What worked, what broke, what you wish it did. That's it.

Paid plans (₹2,999/season unlimited) launch once the beta validates the product. Beta users get 12 months free after launch.

---

## FAQ

**Which broker files do you support?**
Zerodha Tax P&L XLSX only in v1. ICICI Direct, Groww, Upstox, and Angel One are next — priority depends on which brokers the first 50 CAs ask for. Email [minikochar8@gmail.com](mailto:minikochar8@gmail.com?subject=Broker%20request) with the broker you need.

**What about F&O, mutual funds, currency, commodity?**
v1 is equity only — Intraday (speculative), Short Term (Section 111A), Long Term (Section 112A). F&O comes next; it sits in a separate ITR section and has different turnover rules under ICAI 2014 guidance.

**Is the tax math correct?**
The tool uses Zerodha's own pre-computed Profit and Taxable Profit columns (which already handle grandfathering for pre-Jan-2018 holdings) and applies the ₹1.25L Section 112A exemption. Numbers reconcile to Zerodha's own summary sheet. You are still the CA — verify before filing.

**Where does my client's data go?**
Nowhere. The XLSX is parsed in memory in your browser session and discarded when the tab closes. No database. No login. No PAN logged. The code is open source — audit it: [github.com/MiniGrover/ITRREADY](https://github.com/MiniGrover/ITRREADY).

**Refund policy**
Free during beta. Once paid plans launch: 7-day refund if the tool doesn't parse your client's file correctly. Email [minikochar8@gmail.com](mailto:minikochar8@gmail.com).

---

## Contact

[minikochar8@gmail.com](mailto:minikochar8@gmail.com?subject=ITRReady)

Built by an independent developer. Not affiliated with Zerodha. This is a productivity tool for licensed professionals — not tax advice. Always verify before filing.
