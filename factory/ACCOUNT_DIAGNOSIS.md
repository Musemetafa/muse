# Account Diagnosis — template

**How to use this file:** copy it to `accounts/<handle>/DIAGNOSIS.md`
when a new account is handed to the factory, and fill it in **before**
any strategy is chosen for that account (see `factory/ADVANTAGE.md`
§1). One copy per account. Nothing in this template is a fact about
any account — every field is empty until evidence fills it. An empty
field is an honest unknown, not a gap to guess over.

**Current state (2026-11-22): no account exists yet.** This template
is unfilled. The first diagnosis is written when the dedicated TikTok
account arrives.

---

## 1. Account facts

| Field | Value | Evidence / date read |
|---|---|---|
| Handle | | |
| Account type | Personal / Business | |
| Country of registration | | |
| Registration route | | (see §5 — the route determines the country; decided **before** creation, not after) |
| Created | | |
| Account age | | |
| Followers | | |
| Following | | |
| Videos published | | |
| Posting history | | (dates, cadence, gaps — or "none yet") |
| Strikes / removals / reviews | | (count, dates, reasons, outcomes — or "none") |
| Monetization status | UNKNOWN | See §6. Only TikTok Studio → Monetization, read for *this* account, with the date, counts as evidence. |

## 2. Audience — what is known, what is unknown

**Known** (from TikTok Studio, recorded verbatim with read dates):

- Follower demographics:
- Activity times:
- Traffic sources:
- Search queries reaching the account:
- Top videos and why (per the metrics in `EXPERIMENTS.md` §4):

**Unknown** (written down, not guessed):

-
-

For a new account the honest entry is: *audience unknown; the first
videos are the measurement instrument.*

## 3. Capabilities — what the factory can produce for this account

**Can produce now:**

- Formats built:
- Voices available:
- Render pipeline:
- Checkers and specs in force (safe zone, audio spec, icon library):
- Caption system:

**Cannot produce** (see `factory/DESIGN_RULES.md` "What the current
stack cannot do"):

-
-

## 4. Constraints

- Community Guidelines version in force:
- Creator Rewards eligibility state (with evidence — see §6):
- Series/Rewards conflict (LEARNING.md rule 7): no free episode is
  ever linked into a paid Series without an explicit decision weighing
  the lost Rewards income.
- Owner-only actions for this account (see `factory/ADVANTAGE.md`
  §4.3): account registration, authorization/OAuth, publishing taps,
  monetization application, any payment, any use of private data, any
  irreversible change, appeal submissions.
- Other constraints (policy, licence, platform):

**Registration-country warning (recorded 2026-11-22):** the country
an account is registered in determines Creator Rewards eligibility,
and it is set at creation. The Muse cloud browser egresses from Fez,
Morocco (IP 104.29.199.94, Africa/Casablanca), not the US — creating
an account from it would likely register it as Moroccan, and Morocco
is not on the current Creator Rewards country list per the factory's
research, so the account would likely not be eligible for Creator
Rewards. Account creation is paused pending Mohamed's decision
(create anyway, or stop and research a route to US registration).
**No account is created until that decision is made.** When the
decision is recorded, write it here with the date, and record the
registration route actually used.

## 5. Current strategy hypothesis

One sentence, with a falsifier, in the format of
`factory/EXPERIMENTS.md` §2.

```
Claim:
Variable:
Control:
Variant:
Prediction:
Falsifier:
Deciding metric:
```

For a new account the honest entry is: *no strategy yet — the first
experiments are the diagnosis.*

## 6. Monetization status — evidence only

Allowed values (from `EXPERIMENTS.md` §7): `UNKNOWN` ·
`NOT ELIGIBLE — <reason as Studio states it>` · `ELIGIBLE — NOT
APPLIED` · `APPLIED — PENDING` · `ENROLLED — <date>` · `REJECTED —
<reason>`. Nothing else.

| Field | Value |
|---|---|
| Status | UNKNOWN |
| Evidence | (none yet — TikTok Studio → Monetization has not been read for this account) |
| Date read | |
| Estimated rewards | (TikTok Studio's own figure only, with the read date — never a forecast, never an RPM-based estimate; TikTok publishes no RPM) |

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
| | | | |

## 8. Assumption register

Every assumption the factory carries into this account, its evidence,
and what would falsify it (see `factory/ADVANTAGE.md` §5.1).

| Assumption | Evidence (source + date) | Falsifier | Last checked | Status |
|---|---|---|---|---|
| | | | | held / corrected / dropped |

## 9. What we do NOT assume

- That a strategy that worked on another account will work here.
- That the audience of a similar account is this account's audience.
- That a format's success in desk research predicts its success here.
- That followers, views, or a viral video equal an asset.
- That the factory's current tools or current thinking are the best
  available.
- That a competitor's visible numbers tell the whole story.
- (Add account-specific non-assumptions here as they are found.)

## 10. Benchmark record

One row per comparator (see `factory/ADVANTAGE.md` §6). Medians, not
peaks; same format, same video age, same audience-size band;
per-view ratios, not raw counts; never guess a competitor's
completion rate.

| Comparator | Format | Videos used | Metric | Comparator (median) | Factory (median) | Gap |
|---|---|---|---|---|---|---|
| | | | | | | |

**Current state:** no benchmark exists. No competitor has been
observed (Scan 1, gap 5). The Revid baselines (comments/view 0.08%,
likes/view 7.1%) are the only comparators on record, and they are a
floor for the whole platform, not a bar for the strongest quiz
accounts.

## 11. The four audience tests

Recorded with evidence, per `factory/ADVANTAGE.md` §3.3.

| Test | Evidence | Verdict |
|---|---|---|
| Remember — does the viewer remember the account a day later? | | |
| Search — does the viewer search for the account or its topics? | | |
| Return — does the viewer come back tomorrow? | | |
| Trust — does the viewer believe and defend the account's accuracy? | | |

## 12. Next actions

1.
2.
3.

*(The first actions for a new account: complete this diagnosis;
publish EXP-001/EXP-002 as learning instruments, with the explicit
note that their strategy comes from desk research, not from this
account's data; read the first numbers after the 7-day / 1,000-view
window; hold the first learning review.)*
