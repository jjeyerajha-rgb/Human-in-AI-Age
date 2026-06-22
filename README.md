# Human-in-AI-Age

A weekly research automation, run by a **Cursor Cloud Agent**, that pulls thoughtful,
evidence-based advice from the world's best practitioners — **AI subject-matter experts,
neuroscientists, behavioural scientists, and academics** — on a single question:

> As AI tools get pulled into nearly every task at work and in our personal lives, how
> do we keep humans **alive, sane, and cognitively active** — keeping our brains engaged
> rather than quietly outsourcing our thinking?

Each Monday the agent researches the latest studies and expert commentary and publishes
a short, practical brief with habits you can start that week.

## How it works

- **Schedule:** a Cursor Automation runs on cron `30 3 * * 1` — **every Monday at 03:30
  UTC**. (The launch/sample issue was generated on 2026-06-22.)
- **What runs:** the agent follows the prompt in
  [`prompts/weekly-report.md`](prompts/weekly-report.md), researches current sources,
  and writes a new brief.
- **Where it lands:** a dated Markdown file in [`reports/`](reports/), plus a new row in
  [`reports/INDEX.md`](reports/INDEX.md). Reports follow
  [`reports/TEMPLATE.md`](reports/TEMPLATE.md).

## Repository layout

```
.
├── README.md                      # this file
├── prompts/
│   └── weekly-report.md           # the prompt the automation runs each Monday
└── reports/
    ├── INDEX.md                   # list of all weekly briefs (newest first)
    ├── TEMPLATE.md                # report structure
    └── YYYY-MM-DD-human-in-the-ai-age.md
```

## Latest brief

- **Issue 001 (2026-06-22):**
  [Human in the AI Age — Weekly Brief](reports/2026-06-22-human-in-the-ai-age.md) —
  cognitive offloading, "cognitive debt," and the core habit: *think first, prompt
  second.*

## What each brief covers

1. **Executive summary** — the single most useful idea, in plain language.
2. **Why it matters now** — current context.
3. **Voices from the field** — neuroscience, behavioural science, AI practitioners,
   academia.
4. **The evidence, briefly** — a table of key studies with peer-review status.
5. **Do this now** — practical checklists for work and personal life.
6. **Myth vs. reality** + **honest caveats** — no hype, no scare tactics.
7. **Sources** — primary papers and author pages first.

## A note on rigor

Several headline studies in this space are **preprints** or **correlational**. The
briefs say so explicitly and avoid the claim that "AI damages the brain." The evidence
is about *patterns of use* — passive, uncritical reliance is the risk; active, critical,
verify-as-you-go use is not. The goal of this project is **AI literacy**, not alarm.

## Changing the cadence or focus

- To change **what** the reports cover, edit [`prompts/weekly-report.md`](prompts/weekly-report.md).
- To change **when** they run, edit the Automation's cron schedule in the Cursor
  Dashboard (currently weekly on Monday).
