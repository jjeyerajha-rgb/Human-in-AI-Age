# Human-in-AI-Age

A weekly research automation that pulls thoughtful, evidence-based advice from the
world's leading **AI practitioners, neuroscientists, behavioural scientists, and
academics** on one question:

> As AI tools get pulled into nearly every task at work and at home, how do we stay
> **alive, sane, and cognitively active** — keeping our brains engaged rather than
> quietly outsourcing our thinking?

## How it works

A Cursor Cloud Agent runs **every Monday at 03:30 UTC** (cron `30 3 * * 1`). Each run:

1. Reads the editorial brief in [`prompts/weekly-report.md`](prompts/weekly-report.md).
2. Researches the newest studies and expert commentary.
3. Writes a new dated brief to `reports/YYYY-MM-DD-human-in-the-ai-age.md` using
   [`reports/TEMPLATE.md`](reports/TEMPLATE.md).
4. Adds a row to [`reports/INDEX.md`](reports/INDEX.md) and opens a pull request.

## Repository layout

| Path | Purpose |
|---|---|
| `prompts/weekly-report.md` | The editorial prompt the automation runs each week. Edit this to change coverage. |
| `reports/TEMPLATE.md` | The fixed structure every weekly brief follows. |
| `reports/INDEX.md` | Running index of all issues, newest first. |
| `reports/YYYY-MM-DD-human-in-the-ai-age.md` | The weekly briefs. |

## Latest brief

See [`reports/INDEX.md`](reports/INDEX.md) for the full list. Each brief is calm and
non-alarmist by design: AI is useful — the goal is to use it in a way that keeps the
human sharp.
