# Final 60-second video script — teleprompter version

> **Target:** 131 words → ~54 seconds spoken + ~6 seconds of screen transitions = 60 seconds total.
> **Voice:** ElevenLabs — pick an Indian-accented male voice (try "Raj", "Anchal", or "Niraj" in voice library).
> **Reading pace:** Natural conversational, not rushed. Pauses marked with ` ... `.

---

## Voiceover script — paste this exact text into ElevenLabs

```
If you file ITR for Zerodha clients, you know this file. Three hundred rows. Ten charge categories. About thirty minutes per client to extract the numbers.

I built a tool. Drop the same file here. Thirty seconds later, every number you need for Schedule CG and Schedule BP.

Short-term capital gain. Long-term, with the one-point-two-five lakh exemption already applied. Intraday speculative profit. Deductible charges, with STT properly excluded. And turnover, for the audit threshold check.

Download the bundle. Seven CSVs. Per-scrip LTCG table with FMV grandfathering. Trade-level detail for review. Notes for the CA. Paste straight into your filing software.

Free during beta for the first fifty CAs. Link in the description. Send me one client file and tell me what breaks.
```

**Word count: 131. Character count: ~720.** Well under ElevenLabs free tier (10,000 chars/month).

---

## Screen recording cue sheet — what to capture in Game Bar

Record one ~60-second screen session. Don't worry about syncing perfectly to the voiceover yet — that happens in CapCut at the end.

| Time | Voiceover beat | What to show on screen |
|---|---|---|
| 0:00–0:11 | "If you file ITR for Zerodha clients..." | Have the sample XLSX open in Excel. Scroll through it slowly. Pause on the section header "Equity - Intraday", then scroll fast through 200+ rows. End on the charges section. |
| 0:11–0:21 | "I built a tool. Drop the same file..." | Cut to Chrome with the ITRReady URL open. Drag the XLSX from desktop onto the uploader. Show the "Parsed: ... — 2025-04-01 to 2026-03-31" success message. |
| 0:21–0:33 | "Short-term capital gain. Long-term..." | Hover over each of the three metric cards in order: STCG, LTCG, Intraday. Then scroll to charges table and hover the "Deductible" caption. |
| 0:33–0:43 | "Download the bundle. Seven CSVs..." | Click the "Download tax-bundle.zip" button. Open the downloaded ZIP. Show the 7 files. Open `01_summary.csv` for ~2 seconds. |
| 0:43–0:54 | "Free during beta..." | Cut back to the app's top banner showing the free-beta blue info box. |

---

## Step-by-step workflow

### Step 1 — Generate voiceover (3 min)

1. Go to **https://elevenlabs.io** → sign up free
2. Voice Library → search "Indian" → pick a clear male voice (try "Raj" or "Niraj")
3. Paste the script above into the text box
4. Click **Generate** → preview → download the MP3
5. Rename to `voiceover.mp3`, save to Desktop

### Step 2 — Record screen (5 min)

1. Open Excel with the sample XLSX
2. Open Chrome to the ITRReady URL in a second window
3. Press **Win + G** to open Game Bar → click **Capture** widget → click record button (or **Win + Alt + R**)
4. Follow the cue sheet above — one continuous recording, ~60 seconds
5. **Win + Alt + R** again to stop
6. Recording saves to `C:\Users\GAURA\Videos\Captures\`
7. If you fumble, just record again — keep the best take

### Step 3 — Combine in CapCut (10 min)

1. Download **CapCut Desktop** from capcut.com (free, no watermark on export)
2. New Project → import the screen recording (drag to video track)
3. Import `voiceover.mp3` (drag to audio track below)
4. **Mute the original screen-recording audio** (right-click clip → Volume → 0)
5. Trim the video to match the voiceover length (~60 sec)
6. If voice and screen drift out of sync, **split** the video clip at transitions and stretch/shrink each segment to align
7. Export → 1080p MP4 → save as `itrready-demo.mp4`

### Step 4 — Distribute

- **Upload to YouTube as Unlisted** → use that URL in DMs (most reliable)
- Or upload directly to LinkedIn as a native video post (gets better algorithmic reach but loses the URL)
- Embed on the landing page (if you build one)

---

## If you don't want to do CapCut

Easiest fallback: use **Veed.io** (free tier with watermark, but has a "voice + video" combiner that does the syncing automatically). Upload the screen recording + the MP3, it'll auto-align and export.

Trade-off: Veed adds a watermark on free tier. CapCut doesn't. 10 min extra in CapCut saves the watermark.
