# Human in the AI Age

A weekly research digest, generated automatically by a Cursor Cloud Agent, on
how humans can stay **alive, sane, and cognitively active** as AI tools take
over more of our everyday work and personal lives.

Each Monday at **03:30 UTC** a cron-triggered agent pulls fresh research and
advice from the world's leading **AI researchers, neuroscientists,
behavioural scientists, and academics**, synthesises it, and commits a new
report to [`reports/`](./reports/).

## Repository layout

| Path | Purpose |
| ---- | ------- |
| [`reports/`](./reports/) | One Markdown file per week (`YYYY-MM-DD.md`) plus `INDEX.md` |
| [`prompts/weekly-report.md`](./prompts/weekly-report.md) | Standing brief the cron-agent follows |
| [`agents/`](./agents/) | Typed placeholders for the four-stage agent pipeline |
| [`app/streamlit_app.py`](./app/streamlit_app.py) | Streamlit dashboard to browse all editions |
| `requirements.txt` | Python dependencies for the dashboard |

## Run the dashboard locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

The dashboard reads directly from `reports/` — no database, no API keys.
The sidebar lists every edition, the **Current edition** tab renders the
selected report, **Archive** shows the full back-catalogue, and **Pipeline**
visualises the four-stage agent flow.

## Automation

| Piece | Location | Purpose |
| ----- | -------- | ------- |
| Cron trigger | Cursor Automation `0598b520-…` (`30 3 * * 1`) | Wakes the agent every Monday at 03:30 UTC |
| Standing brief | [`prompts/weekly-report.md`](./prompts/weekly-report.md) | What to research, how to structure, what to avoid |
| Pipeline contract | [`agents/`](./agents/) | Will eventually replace the single-agent path |
| Reports | [`reports/`](./reports/) | Markdown output, one per week |
| Index | [`reports/INDEX.md`](./reports/INDEX.md) | Running table of contents |

## Latest report

- **Sample / inaugural edition (28 May 2026):**
  [reports/2026-05-28-sample-report.md](./reports/2026-05-28-sample-report.md)

## Editorial principles

- Evidence-based, not alarmist.
- Always cite named researchers and primary sources.
- Always include at least one counter-voice (AI as cognitive _amplifier_).
- Practical — every report ends with a copy-pasteable playbook.
- No emojis, no marketing language, no recycled headlines.

## Branch

All automation work lives on `cursor/ai-human-best-practices-5584`.
