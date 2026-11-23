# Account Diagnosis — @TheQuizTeaser

**Diagnosed:** 2026-11-22 (~19:05–19:20 UTC), read-only, in the local
Playwright browser on the factory VM (US egress), session logged in as
the account owner. Evidence files:
`~/workspace/tiktok-session/diagnosis-evidence.json`,
`diagnosis-notes.txt`, `diagnosis-settings.json`,
`diagnosis-activity.json`, screenshots `diagnosis-profile.png`,
`diagnosis-studio.png`, `diagnosis-monetization.png`,
`diagnosis-settings.png`, `diagnosis-activity.png`. Scripts:
`diagnose.py`, `retry_settings.py`, `check_activity.py`.
No page was changed, nothing was uploaded, posted, liked, followed,
commented on, or dismissed; no code was entered; no challenge or
CAPTCHA appeared at any point.

**Standing note (Mohamed, 2026-11-22 15:56 UTC):** do NOT infer
anything about Mohamed from this account being British. The UK
registration is a means (UK is on the Creator Rewards eligible-country
list), not a fact about his identity, residence, or nationality.

---

## 1. Account facts

| Field | Value | Evidence / date read |
|---|---|---|
| Handle | @thequizteaser | Profile page, 2026-11-22 |
| Display name | The Quiz Teaser | Profile page, 2026-11-22 |
| Bio | `Daily quiz questions & riddles. Beat the timer — can you solve them all? 🧠` | Profile page, 2026-11-22 (exact match to the decided bio, 74 chars) |
| Profile picture | SET — violet circle, white question mark, glowing yellow lightbulb (the generated brand picture) | Confirmed visually in `diagnosis-profile.png`, 2026-11-22 |
| Account type | UNKNOWN | Web settings (`tiktok.com/setting`) does not state Personal/Business. The account was created as Personal per the instruction given to Mohamed at creation (~17:26 UTC) — that is an instruction, not a read of the account. To be confirmed from the TikTok app or a Studio surface that states it. |
| Country of registration | United Kingdom | Settings → Account information → Account region: "Your account region is initially set based on the time and place of registration. United Kingdom" (TikTok's own words), 2026-11-22 |
| Registration route | Created by Mohamed himself in his own browser, registered with Google (no password) | Mohamed, 2026-11-22 ~17:38 UTC; public profile first verified the same day |
| Created | 2026-11-22 | Account created ~17:38 UTC; first verified live the same day |
| Account age | < 1 day | 2026-11-22 |
| Followers | 0 | Profile + Studio, 2026-11-22 |
| Following | 0 | Profile + Studio, 2026-11-22 |
| Videos published | 0 | Profile + Studio ("No posts yet"), 2026-11-22 |
| Posting history | None yet | — |
| Strikes / removals / reviews | None observed | Studio home shows no warnings; Monetization page shows the normal programme list. One unread Activity notification (badge "1") exists — contents NOT opened (read-only rule), so it is recorded as unopened, not as a strike. |
| Monetization status | NOT ELIGIBLE — Studio lists the Creator Rewards Programme as "Ineligible" (no reason stated on the page) | See §6. TikTok Studio → Monetization, read 2026-11-22 |

**Owner-view proof (session logged in):** profile page shows "Edit
profile" and "Post video" buttons; Studio loads with the account
identity and metrics; Upload page loads without redirect to login;
left nav shows Messages / Activity (badge 1) / Upload / Profile.

**Quirk observed, not a defect of the account:** the profile video
grid shows "Something went wrong / Sorry about that! Please try again
later. / Refresh" instead of an empty state. The same error appeared
in the guest view on 2026-11-22 ~18:27 UTC. It is TikTok's empty-grid
behaviour on a 0-video account, not evidence of a strike.

## 2. Audience — what is known, what is unknown

**Known** (from TikTok Studio, recorded verbatim with read dates):

- Follower demographics: none — 0 followers, 2026-11-22.
- Activity times: none — no data, 2026-11-22.
- Traffic sources: none — no data, 2026-11-22.
- Search queries reaching the account: none — no data, 2026-11-22.
- Top videos and why: none — no videos published, 2026-11-22.

**Unknown** (written down, not guessed):

- Everything about the audience: age, gender, geography, interests,
  active hours, what they search for, what keeps them watching.
- Whether quiz or riddle content will find this account's audience
  at all.

For a new account the honest entry is: *audience unknown; the first
videos are the measurement instrument.*

## 3. Capabilities — what the factory can produce for this account

**Can produce now:**

- Formats built: trivia quiz round v2 (90.41 s, 5 fact-checked
  questions, 5 s think time) and riddle round v2 (92.29 s, 3 original
  riddles, "3 clues, 10 seconds"), both 720×1280, 30 fps, Kokoro
  af_heart narration (provisional voice — the listening test is
  unanswered), karaoke captions, safe-zone layout, 9 code-drawn
  icons + 5 motion functions. Both verified: safe-zone checker PASS
  on every frame, black/freeze/silence 0, byte-identical reruns.
- Voices available: Kokoro af_heart (in use, provisional), am_adam
  (available; switch requires re-synthesis + re-render).
- Render pipeline: Python + Pillow + FFmpeg, deterministic,
  ~3–4 min machine time per ~90 s video on this CPU-only VM.
- Checkers and specs in force (safe zone, audio spec, icon library):
  safe-zone layout system (`factory/layout.py`: top 160, bottom 440,
  sides 80; safe box x 80–640, y 160–840; subtitle band y 667–840)
  with an automated per-frame checker; black/freeze/silence
  detection; icon library (`factory/icons.py`). **Audio spec: none
  yet** — no loudness target, no music/SFX layer (D14/M10 pending).
- Caption system: karaoke captions with the current word
  highlighted, drawn inside the subtitle band; caption practice per
  Module 1 (topic phrase first, then context, then 3–5 hashtags).

**Cannot produce** (see `factory/DESIGN_RULES.md` "What the current
stack cannot do"):

- Rich character animation, lip-sync, and physics-based motion
  (Pillow frame-by-frame limits; motion vocabulary is slides, pops,
  pulses, ticks, travelling dots, progress bars, ambient stripes).
  OpenFilm (HTML/CSS/JS rendering) is the proven layer if a format
  needs richer motion.
- Any audio beyond voice-over (no music bed, no SFX, no loudness
  normalisation) until D14/M10 lands.
- The brain icon reads as an abstract thinking blob at small size,
  not a literal brain.

## 4. Constraints

- Community Guidelines version in force: released 25 Aug 2026,
  effective 24 Sep 2026 (Module 1; tracked re-check trigger).
- Creator Rewards eligibility state: NOT ELIGIBLE — see §6.
- Series/Rewards conflict (LEARNING.md rule 7): no free episode is
  ever linked into a paid Series without an explicit decision weighing
  the lost Rewards income.
- Owner-only actions for this account (see `factory/ADVANTAGE.md`
  §4.3): account registration, authorization/OAuth, publishing taps,
  monetization application, any payment, any use of private data, any
  irreversible change, appeal submissions.
- Other constraints (policy, licence, platform): AI-generated label
  is mandatory on every video (TikTok requires it for realistic AI
  audio/video — TTS narration is AI-generated speech). Zero spend:
  no purchases, subscriptions, paid API keys, or paid cloud resources.

**Registration-country warning — RESOLVED for this account:**
Settings → Account information confirms the account region is the
United Kingdom (see §1). The UK is on the Creator Rewards
eligible-country list per the factory's research, so the country side
of eligibility is satisfied; the audience side (10,000 followers,
100,000 views/30 days) is not. The earlier warning (cloud browser in
Fez, Morocco would have registered a Moroccan account) is moot for
this account, which Mohamed created himself in his own browser.

**Operating browser (Mohamed's decision, 2026-11-22 ~18:46 UTC):**
the factory operates this account from the local VM browser (US
egress — Seattle at check time, rotating), NOT the cloud browser
(Fez, Morocco), which cannot be moved. The local browser session was
verified logged in on 2026-11-22 ~18:58 UTC and again during this
diagnosis.

## 5. Current strategy hypothesis

No strategy yet — the first experiments are the diagnosis. The
comparison already built (EXP-001/EXP-002) is the starting hypothesis
from desk research, not from this account's data:

```
Claim:    A trivia quiz round earns more comments per view than a riddle round,
          because every question invites the viewer to answer in the comments.
Variable: Format (trivia vs riddles). One variable only; both videos follow
          DESIGN_RULES.md and pass the automated checks.
Control:  EXP-001 — trivia quiz round v2, 90.41 s, 5 questions, 5 s think time.
Variant:  EXP-002 — riddle round v2, 92.29 s, 3 riddles, "3 clues, 10 seconds".
Prediction: Trivia wins comments/view; riddles win shares/view (a riddle is a
          challenge to send to a friend); trivia wins or equals completion on
          pace (5 s vs 10 s think time).
Falsifier: The comparison's pre-registered thresholds (EXPERIMENTS.md §4):
          a format wins only on comments/view ≥50% relative AND completion
          ≥5 points absolute; rejection at ≥50% below the Revid baselines.
Deciding metric: comments/view, with completion as the joint condition.
```

## 6. Monetization status — evidence only

Allowed values (from `EXPERIMENTS.md` §7): `UNKNOWN` ·
`NOT ELIGIBLE — <reason as Studio states it>` · `ELIGIBLE — NOT
APPLIED` · `APPLIED — PENDING` · `ENROLLED — <date>` · `REJECTED —
<reason>`. Nothing else.

| Field | Value |
|---|---|
| Status | NOT ELIGIBLE — Studio lists the Creator Rewards Programme as "Ineligible" (no reason stated on the page) |
| Evidence | TikTok Studio → Monetization (`tiktok.com/tiktokstudio/monetization`), read 2026-11-22 ~19:10 UTC, screenshot `diagnosis-monetization.png`, full text in `diagnosis-evidence.json`. Programme list: Gaming Incentive Programme — Recommended (Join); Subscription — Ineligible; **Creator Rewards Programme — Ineligible** ("Create videos that are 1 minute or longer to get rewarded on qualified views."); Video Gifts — Ineligible; Creator Marketplace — Ineligible; Work with Artists — Ineligible; LIVE Incentive Programme — Ineligible; Service+ — Ineligible. A "Get notified when I'm eligible" link is present (not clicked). No reason for the ineligibility is stated anywhere on the page. |
| Date read | 2026-11-22 |
| Estimated rewards | $0.00 (TikTok Studio's own figure, "Rewards analytics — Total — Last 7 days", read 2026-11-22; TikTok Shop for Seller also $0.00). "Sources of rewards: Post videos to start getting rewarded." No revenue has happened; no forecast is recorded. |

**Inference, labelled as inference (not Studio's words):** with 0
followers and 0 videos, the published Creator Rewards thresholds
(10,000 followers; 100,000 views in the last 30 days) are unmet.
Studio itself states no reason — the status above records only what
Studio states.

**This account's eligibility is separate from any other account's.**
The other agent's monetized TikTok account is not this account. Its
status says nothing about this account's status.

## 7. Advantage map — claimed advantages for this account

One row per claimed advantage. Evidence levels use the LEARNING scale:
NONE → LEARNING → TESTED → PROVEN → RULE. At diagnosis time this map
is empty except for *methods* (which are capabilities, not
advantages).

| Advantage claimed | Evidence level | Evidence (source + date) | What would demote it |
|---|---|---|---|
| *(none claimed)* | — | — | — |

Methods held (capabilities, not advantages): deterministic render
pipeline; safe-zone checker; icon/motion library; experiment
protocol with pre-registered thresholds.

## 8. Assumption register

Every assumption the factory carries into this account, its evidence,
and what would falsify it (see `factory/ADVANTAGE.md` §5.1).

| Assumption | Evidence (source + date) | Falsifier | Last checked | Status |
|---|---|---|---|---|
| Trivia earns more comments/view than riddles; riddles earn more shares/view | None — it is EXP-001/EXP-002's hypothesis | The comparison's pre-registered thresholds | 2026-11-22 | held |
| A 5-second think time beats a 10-second think time on completion | None — H3 prediction | Riddles winning completion | 2026-11-22 | held |
| The three-layer SEO practice (caption + on-screen + spoken topic phrase) improves search discovery | Practitioner only (Module 1) | No search-traffic difference in a controlled test | 2026-11-22 | held |
| One video per day is the right cadence | Measured compute times + the no-volume rule | The account's own data showing a different cadence earns more per video | 2026-11-22 | held |
| The factory's current renderer and voice are good enough to compete | None about competitiveness — only that they render | Benchmark comparison showing a systematic gap | 2026-11-22 | held |

## 9. What we do NOT assume

- That a strategy that worked on another account will work here.
- That the audience of a similar account is this account's audience.
- That a format's success in desk research predicts its success here.
- That followers, views, or a viral video equal an asset.
- That the factory's current tools or current thinking are the best
  available.
- That a competitor's visible numbers tell the whole story.
- That the UK registration says anything about Mohamed (his explicit
  instruction, 2026-11-22 15:56 UTC).
- That the "Ineligible" label means the account can never be
  eligible — it means the thresholds are unmet today; eligibility is
  re-read at every learning review as the account grows.
- That the one unread Activity notification is a welcome message —
  its contents were not opened.

## 10. Benchmark record

One row per comparator (see `factory/ADVANTAGE.md` §6). Medians, not
peaks; same format, same video age, same audience-size band;
per-view ratios, not raw counts; never guess a competitor's
completion rate.

| Comparator | Format | Videos used | Metric | Comparator (median) | Factory (median) | Gap |
|---|---|---|---|---|---|---|
| *(none yet)* | | | | | | |

**Current state:** no benchmark exists. No competitor has been
observed (Scan 1, gap 5). The Revid baselines (comments/view 0.08%,
likes/view 7.1%) are the only comparators on record, and they are a
floor for the whole platform, not a bar for the strongest quiz
accounts.

## 11. The four audience tests

Recorded with evidence, per `factory/ADVANTAGE.md` §3.3.

| Test | Evidence | Verdict |
|---|---|---|
| Remember — does the viewer remember the account a day later? | No audience yet; no videos published | No evidence |
| Search — does the viewer search for the account or its topics? | No search data in Studio | No evidence |
| Return — does the viewer come back tomorrow? | No audience yet | No evidence |
| Trust — does the viewer believe and defend the account's accuracy? | No audience yet | No evidence |

## 12. Next actions

1. Publish EXP-001 (trivia v2) as the first video under the
   experiment protocol (AI-generated label on, caption per the Module
   1 practice, 1 video/day cadence), then EXP-002 (riddle v2) the
   next day — with the explicit note that their strategy comes from
   desk research, not from this account's data.
2. Open the one unread Activity notification and record what it is
   (welcome message vs anything else).
3. Confirm the account type (Personal) from the TikTok app or a
   Studio surface that states it — the web settings page does not.
4. Re-read TikTok Studio → Monetization at each learning review;
   record any status change with the date and Studio's exact words.
5. Read the first numbers after the 7-day / 1,000-view window for
   both experiments; hold the first learning review then.
6. Audit the assumption register (§8) at the first learning review.
