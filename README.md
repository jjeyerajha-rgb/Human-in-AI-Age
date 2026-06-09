# Human in the AI Age

A weekly research brief that pulls thoughtful research and advice from the world's
best practitioners — **AI subject-matter experts, neuroscientists, behavioural
scientists, and academics** — on the key best practices for staying **alive, sane,
and cognitively active** while we are increasingly pulled toward depending on AI
tools for everyday tasks at work and in our personal lives.

> The goal is not to reject AI. It is to use it deliberately so that it *augments*
> human thinking instead of quietly eroding it.

---

## What this repo produces

Every week the automation generates a new **Weekly Brief** in [`reports/`](reports/):

- A short, skimmable executive summary.
- "Voices from the field" — current, sourced findings and recommendations from
  named experts and peer-reviewed/preprint research.
- A practical, do-this-now checklist for work and personal life.
- A one-page "keep your brain on" routine.
- A balanced view (what the skeptics and critics say).
- Fully linked sources so every claim can be verified.

Browse all editions in [`reports/INDEX.md`](reports/INDEX.md).

## Schedule

- **Sample / launch issue:** generated on demand (see the first report).
- **Recurring:** every **Monday at 03:30 UTC** via a Cursor scheduled automation
  (cron `30 3 * * 1`).

Each run:

1. Researches the latest expert thinking and studies from the past week/quarter.
2. Synthesises it into a new dated brief in `reports/`.
3. Updates `reports/INDEX.md`.
4. Opens/updates a pull request for review.

## Repo structure

```
.
├── README.md                  # this file
├── prompts/
│   └── weekly-report.md       # the instructions the weekly automation follows
├── reports/
│   ├── INDEX.md               # chronological index of all briefs
│   ├── TEMPLATE.md            # the structure every brief follows
│   └── YYYY-MM-DD-human-in-the-ai-age.md
```

## How to read a brief

Start with **§1 Executive Summary** and **§5 Do This Now**. If a claim matters to
you, follow the linked source — the briefs are designed to be a starting point for
your own thinking, not a replacement for it. (That is, after all, the whole point.)

## A note on sourcing & caution

Research in this area is young and fast-moving. Some headline findings (e.g. the MIT
"cognitive debt" preprint) are **not yet peer-reviewed** and have drawn legitimate
methodological criticism. Briefs flag this explicitly and include dissenting views so
readers can weigh the evidence themselves.
