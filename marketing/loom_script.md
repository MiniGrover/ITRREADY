# 60-second Loom demo script

> Record once. Embed on landing page + attach to every DM. Use a real (or sanitized) client file. Screen share only — no webcam needed but turn it on if you want a face on the brand.

## Setup before hitting record

- Open the deployed app URL in a clean Chrome window
- Have the sample XLSX on desktop, ready to drag
- Close all other tabs and notifications
- Practice once — under 60 sec is hard, two takes typically gets it

---

## Beat sheet (read these out, don't memorize verbatim)

### 0:00 – 0:08 — The hook
> "If you're a CA filing ITR-2 for clients with Zerodha accounts, you've seen this file."

Action: drag the Zerodha Tax P&L XLSX onto the screen, scroll fast through the 333 rows for two seconds.

### 0:08 – 0:18 — The pain
> "Three hundred trades, ten charge categories, FMV grandfathering for long term, STT that you can't deduct but everyone forgets. About thirty minutes per client. Now multiply by your client list."

Action: keep scrolling, land on the charges section.

### 0:18 – 0:30 — The product
> "I built a tool that does this in thirty seconds. Drop the file."

Action: switch to the app, drag-drop the XLSX. The summary table renders.

> "Here are the six numbers ITR actually needs. Short-term gain. Long-term after the 1.25 lakh exemption. Intraday speculative P&L. Deductible charges, with STT correctly excluded. Turnover for the audit threshold check."

Action: hover each number on the summary as you say it.

### 0:30 – 0:45 — The deliverable
> "And here's the part that saves the real time."

Action: enter unlock code, click download, open the ZIP.

> "Seven CSVs. Per-scrip LTCG table with FMV grandfathering already applied. Trade-level detail for review. Notes for apportionment. Paste straight into your ITR utility or filing software."

Action: open `01_summary.csv` for two seconds, then close.

### 0:45 – 0:58 — The pitch
> "First three client files are free. After that, 2,999 rupees gets you unlimited filings till March 2027 — covers your entire current season. No subscription, no signup, no data stored."

Action: back to landing page, hover the price.

### 0:58 – 1:00 — The CTA
> "Link in the description. Send me one client's file and tell me what breaks."

---

## What NOT to say

- "Revolutionary" / "AI-powered" / "10x your practice" — sounds like fluff, CAs roll their eyes
- "Compliant with [random thing]" unless you've actually verified
- "Trusted by 500 CAs" — don't lie about traction
- Don't mention ICAI, SEBI, or Income Tax Department by name in a claim — only in factual statements about which schedule a number goes into

## What to say if asked on a call

- *"Why should I trust the math?"* — "Numbers reconcile to Zerodha's own summary sheet. Run it on a file you've already filed and compare."
- *"What about F&O?"* — "Equity only in v1. F&O is next if there's demand — vote on the form."
- *"What about ICICI / Groww / Upstox?"* — "Same — coming if I get enough requests. Send me one of those statements and you'll be the first user when it's done."
- *"Is my data safe?"* — "File is parsed in memory in the browser session, discarded when the tab closes. No DB, no login, no PAN logged. The code is open source — you can audit it."
