# Landing page copy — single page for tax-tool.streamlit.app

> Goal: a CA lands here from a DM or WhatsApp link, scrolls once, gets the value, pays. No fluff, no testimonials we don't have, no fake countdown timers.

---

## Hero (above the fold)

**Headline**
Zerodha Tax P&L → ITR-ready numbers in 30 seconds.

**Sub-headline**
Built for CAs who file 50+ ITR-2 / ITR-3 returns each season. Drop the client's XLSX, get the six numbers that go straight into Schedule CG and Schedule BP. STT correctly excluded. ₹1.25L 112A exemption applied. Per-scrip LTCG table for grandfathering.

**Primary CTA button**
→ Try free with your file (no signup)

**Secondary text under button**
Free beta for the first 50 CAs. No signup, no payment, no data stored.

---

## The problem (one section, four lines)

You open the Zerodha Tax P&L for one client.

- 333 rows across Intraday, Short Term, Long Term, Buyback, F&O.
- Charges split across 10 categories — half deductible, half not.
- STT mistakes are the #1 reason CG figures get questioned in scrutiny.
- And you have 199 more clients waiting.

You know exactly what numbers ITR needs. The XLSX is just in the way.

---

## What this gives you

A ZIP of seven files, ready to paste into ITR utility or your filing software:

| File | What it is |
|---|---|
| `01_summary.csv` | The six numbers — STCG, LTCG, intraday P&L, deductible charges, turnover |
| `02_charges.csv` | Brokerage / GST / exchange charges (deductible) vs STT (not deductible) |
| `03_ltcg_per_scrip.csv` | Per-scrip table with FMV grandfathering applied for Section 112A |
| `04_intraday_trades.csv` | Speculative business detail for Schedule BP |
| `05_short_term_trades.csv` | STCG detail with holding period |
| `06_long_term_trades.csv` | LTCG detail with FMV column populated |
| `07_notes.txt` | Apportionment + audit threshold + exemption notes |

---

## How it works

1. **Upload** — drag your client's Zerodha Tax P&L XLSX
2. **Verify** — preview the summary, sanity-check the numbers
3. **Download** — get the seven-file ZIP

The XLSX never leaves your browser session. No account, no PAN stored, no data retained.

---

## Pricing

**Free during beta** — first 50 CAs, no payment, unlimited files.

In exchange: email one line of feedback after you try it. What worked, what broke, what you wish it did. That's it.

Paid plans (₹2,999/season unlimited) launch once the beta validates the product. Beta users get 12 months free after launch.

---

## FAQ

**Which broker files do you support?**
Zerodha Tax P&L XLSX only, v1. ICICI Direct, Groww, Upstox, Angel One coming if there is demand — vote here: https://itrready-dirxr3fop2qs9sfsgkctkm.streamlit.app/.

**What about F&O / mutual funds / currency / commodity?**
v1 is equity only (Intraday + STCG + LTCG). F&O comes next — it's a separate ITR section and has different turnover rules under ICAI 2014 guidance.

**Is the tax math correct?**
The tool uses Zerodha's own pre-computed Profit and Taxable Profit columns (which already handle grandfathering for pre-Jan-2018 holdings) and applies the ₹1.25L Section 112A exemption. Numbers reconcile to Zerodha's own summary sheet. You are still the CA — verify before filing.

**Where does my client's data go?**
Nowhere. The file is parsed in memory in your browser session and discarded when you close the tab. No database. No login. No PAN logged.

**Refund policy**
First 3 files free — try before you pay. After purchase: 7-day refund if the tool doesn't parse your client's file correctly. Email at minikochar8@gmail.com.

---

## Footer

Built by an independent developer. Not affiliated with Zerodha. Not tax advice — this is a productivity tool for licensed professionals. Always verify before filing.

Contact: minikochar8@gmail.com / [Twitter handle]
