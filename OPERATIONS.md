# Self-Running Operations

How the Video Factory runs itself, without waiting for Mohamed to say
"continue". This file is the operating manual. `STATE.md` is the live state.
Both live in this repository so any run can resume from them.

## The loop

1. **Wake.** A scheduled run starts (cron `video-factory-loop`, every 6 hours)
   or a delegated worker finishes and hands back a result.
2. **Read state.** The run reads `STATE.md` first, then the files it points to
   (research reports, test reports, run logs). Memory and chat history are
   secondary; the repository state is the source of truth.
3. **Do one next step.** The run takes the single next step in `STATE.md`
   (or the next step it derives from the evidence) and executes it to a
   testable result: research with cited sources, a test with measured output,
   or a decision with reasons, risks, and alternatives.
4. **Evaluate.** The run judges its own result against the criteria set in
   advance for that step. A pass, a fail, and an inconclusive result are all
   recorded as what they are. A report documents the work; it never replaces
   continuing it.
5. **Choose the next step.** The run writes the next step into `STATE.md`
   with its success criteria, then either executes it in the same run (when
   it fits the run's remaining budget) or leaves it for the next run.
6. **Save state.** The run updates `STATE.md` and appends a line to
   `RUNLOG.md`, then pushes both to this repository. If a push needs an
   approval the run cannot obtain, that is recorded as a blocker, not
   silently skipped.

## Rules

- **Zero spend, always.** No purchases, subscriptions, paid balances, paid
  API keys, or paid cloud resources. Free source is not free operation.
- **Escalate only for:** a permission, an account link, a financial or legal
  commitment, private data of Mohamed, or an irreversible change. Everything
  else is decided by the run itself.
- **No theoretical autonomy.** A claim about what the loop can do must be
  backed by an observed run. Limits are recorded in `STATE.md` under
  "Known limits", with the evidence for each.
- **One step per run, minimum.** A run that does nothing but report "still
  working" is a failure of the loop, unless the next step genuinely waits on
  an external event (then the wait is recorded with its trigger).
- **Never invent.** No invented numbers, results, or repository access. A
  failed check is reported as failed, with the cause found, not assumed.
- **English outputs, Arabic conversation.** Factory content is English only.
  Conversation with Mohamed stays in Arabic.

## Schedule

- `video-factory-loop`: every 6 hours, agent run. Owner: goal `مصنع الفيديو`.
- `video-factory-loop-test`: one-off proof run, shortly after setup, to prove
  the scheduler fires, the state is read, work resumes, and a result is
  delivered. After it proves those four things, it is not needed again.

## Known limits (honest, updated from evidence)

- Muse does not run continuously. It wakes on schedule, on a message, or on
  a worker handoff, and is idle between runs. Continuity is periodic, not
  constant.
- Each run starts with limited context and must rebuild it from `STATE.md`
  and the repository. Anything not written down does not survive.
- GitHub writes ask for approval on every call. No standing approval exists
  for GitHub (checked 2026-11-22). A background run that needs to push may
  stall on an approval card until Mohamed answers it. This is the main
  unproven part of full autonomy, and the test run is designed to measure it.
- A run has a time budget (the schedule's timeout). Long work is split
  across runs or delegated to subagents, whose results arrive as handoffs.
- VM replacement can interrupt a run. The runtime recovers saved jobs and
  crons; local progress survives only if it was written to the home
  directory or pushed to this repository before the interruption.
