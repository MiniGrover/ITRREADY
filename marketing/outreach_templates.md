# Outreach templates for first 30 CAs

> Goal: get the first 10 CAs to try it free → 3 of them to pay → 1 testimonial. That's enough to fuel the next 100.

## Where to send these

| Channel | Best for | Volume |
|---|---|---|
| LinkedIn DM | CAs you can identify by name + firm | 5/day max, sustainable |
| Twitter/X DM | CA tax-twitter accounts (#CAfinal, #IncomeTax) | 5/day |
| WhatsApp CA groups | If you're in any — share once, don't spam | 1-2 groups |
| TaxGuru / CAclub forum post | Long-form, gets indexed | 1 post per platform |
| Cold email | Last resort, lowest reply rate | only if you have a list |

**Do not** mass-DM. The Indian CA community is small and talks. One spam complaint kills the channel.

---

## LinkedIn DM — first touch (cold)

> Hi [Name],
>
> I built a small tool that turns a Zerodha Tax P&L XLSX into ITR-ready capital-gains figures — Section 111A / 112A numbers, deductible charges with STT properly excluded, per-scrip LTCG with grandfathering. About 30 seconds per client file instead of 30 minutes.
>
> Free during beta — no signup, no payment: https://itrready-dirxr3fop2qs9sfsgkctkm.streamlit.app/
>
> Would you be open to trying it with one of your client files and telling me what breaks? Genuinely looking for feedback, not pitching.
>
> [Your name]

**Why this works:** specific (Zerodha + 111A/112A names dropped = you know the domain), short, asks for feedback not money, gives them an out.

**What to avoid:** "Hope you're doing well." / "Quick question:" / anything that sounds like a template.

---

## LinkedIn DM — second touch (if they replied "interesting, will check")

> Thanks [Name]. One quick thing — if you do try it, run it on a client file you've already filed for FY 24-25. The numbers should reconcile to what you filed. If they don't, that's the bug I want to know about.
>
> Also, if F&O / ICICI / Groww support would matter for your practice, let me know — I'll prioritize whichever broker the first 10 CAs ask for.

---

## Twitter/X DM (more casual)

> Hey [@handle] — saw your thread on [specific tweet they posted about tax filing pain]. Built a tool for exactly that. Turns the Zerodha XLSX into ITR-ready numbers in 30 sec. Free for first 3 files: https://itrready-dirxr3fop2qs9sfsgkctkm.streamlit.app/. Would love your roast.

**Why this works:** reference a specific tweet of theirs (don't copy-paste). Calling it "roast" lowers the stakes.

---

## WhatsApp CA group post

> Folks — built a side project that takes a Zerodha Tax P&L XLSX and outputs ITR-ready numbers (Sec 111A / 112A, per-scrip LTCG with FMV, deductible charges with STT excluded).
>
> Free for 3 client files: https://itrready-dirxr3fop2qs9sfsgkctkm.streamlit.app/
>
> Looking for 10 CAs to break it and tell me what's wrong. DM if interested or just try it directly — no signup. Won't post in this group again.

**Why this works:** the "won't post again" line is what keeps you from getting kicked. Mean it.

---

## TaxGuru / CAclubindia forum post

**Title:** Tool to convert Zerodha Tax P&L XLSX into ITR-2/3 ready figures — free for first 3 files

**Body:**

Built this over the past few weeks because I was tired of seeing my own CA spend 30 minutes per client on Zerodha statements during tax season.

What it does:
- Parses the Tax P&L XLSX (Tradewise Exits sheet)
- Outputs aggregated figures for Schedule CG-A1 (111A STCG), CG-B1 (112A LTCG), and Schedule BP (intraday speculative)
- Builds per-scrip LTCG table with FMV grandfathering applied
- Separates deductible charges (brokerage, GST, exchange, stamp duty) from STT (not deductible against gains)
- Computes intraday turnover for the 44AB audit threshold check

What it doesn't do (yet):
- F&O / currency / commodity / mutual funds
- Anything other than Zerodha
- It is not tax advice. You are the CA.

Free during beta — no signup, no payment, no data stored. Paid plans (₹2,999/season) launch once the beta validates demand; beta users get 12 months free after launch.

Link: https://itrready-dirxr3fop2qs9sfsgkctkm.streamlit.app/

Genuinely want feedback on what's wrong. If a number doesn't match what you'd file, that's a bug I want to fix.

---

## Cold email (only if needed)

**Subject:** A tool for the Zerodha file you'll see 50 times this season

> [Name],
>
> Built a small utility that converts a Zerodha Tax P&L XLSX into the figures that go into Schedule CG-A1, CG-B1, and Schedule BP — including per-scrip LTCG with FMV grandfathering and the STT-excluded charges breakdown.
>
> Free during beta for the first 50 CAs. Paid plans launch later — beta users get 12 months free.
>
> [Link]
>
> If it works for you, share with one other CA. If it doesn't, reply and tell me why.
>
> [Your name]

---

## Tracking — where this matters

Make a simple spreadsheet (or just a Notion doc):

| Date | Channel | CA name | Reply? | Tried tool? | Paid? | Feedback notes |
|---|---|---|---|---|---|---|

After 30 DMs across two channels, you'll know which channel converts and where to double down. Most builders skip this and end up confused why nothing works.
