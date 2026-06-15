# Human in the AI Age

A weekly research automation, run in Cursor, that pulls thoughtful research and advice
from the world's best practitioners — **AI subject-matter experts, neuroscientists,
behavioural scientists, and academics** — on the key best practices that keep humans
**alive, sane, and cognitively active** as we are increasingly pulled toward depending
on AI tools for everyday tasks at work and in our personal lives.

Each brief answers one recurring question:
**"How do I get the benefits of AI without quietly outsourcing my own thinking?"**

## How it works

A Cursor Cloud Agent runs on a schedule (**every Monday**) and:

1. Researches the latest credible studies, essays, and expert recommendations.
2. Synthesises them into a balanced, well-cited brief — including counter-evidence.
3. Writes a new report to `reports/` and updates [`reports/INDEX.md`](reports/INDEX.md).
4. Opens a pull request with the new brief.

> **Recurring schedule:** the automation is configured to run weekly on Monday. This
> repo also contains a **sample run** so you can see the output format immediately.

## Repository layout

| Path | Purpose |
|---|---|
| [`reports/`](reports/) | The weekly briefs, one Markdown file per week |
| [`reports/INDEX.md`](reports/INDEX.md) | Running index of all briefs (newest first) |
| [`reports/TEMPLATE.md`](reports/TEMPLATE.md) | The structure each brief follows |
| [`prompts/weekly-report.md`](prompts/weekly-report.md) | Standing instructions for each Monday run |

## Latest brief

- **Issue 001 — [Week of 15 June 2026](reports/2026-06-15-human-in-the-ai-age.md):**
  Active vs. passive AI use, "cognitive debt," and the 3R principle.

## Editorial stance

Calm, evidence-led, and non-alarmist. We are **pro-AI *and* pro-human**: the goal is
skillful, intentional use — not abstinence, and not surrender. Findings from preprints
or self-report studies are flagged as such, and every claim links to its source so you
can check the work yourself.
