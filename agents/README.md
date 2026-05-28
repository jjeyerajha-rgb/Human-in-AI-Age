# `agents/` — Weekly digest agent pipeline

These modules define the **contract** for the agent pipeline that produces
the weekly Human-in-AI-Age report. They are placeholders today: the Cursor
cron-agent currently performs all stages in a single autonomous run guided
by [`../prompts/weekly-report.md`](../prompts/weekly-report.md).

## Pipeline

```
research_agent  ──►  synthesis_agent  ──►  editor_agent  ──►  orchestrator
   (web)              (LLM + brief)         (checklist)        (write + index)
```

| Stage | File | Responsibility |
| ----- | ---- | -------------- |
| 1. Research | `research_agent.py` | Pull fresh primary research, deduplicate against `reports/INDEX.md`. |
| 2. Synthesis | `synthesis_agent.py` | Produce a draft that follows the standing brief's required structure. |
| 3. Editor | `editor_agent.py` | Quality pass — naming, citations, anti-patterns, counter-voice. |
| 4. Orchestrator | `orchestrator.py` | Glue, write `reports/YYYY-MM-DD.md`, append to `INDEX.md`. |

## Replacing the placeholders

Each stage exposes a small, typed API. You can replace any stage
independently without touching the others.

```python
from datetime import date
from agents import Orchestrator, ResearchAgent, SynthesisAgent, EditorAgent

result = Orchestrator(
    researcher=ResearchAgent(),       # swap in a real web search + LLM
    synthesiser=SynthesisAgent(),     # swap in your model of choice
    editor=EditorAgent(),             # swap in the checklist runner
).run(edition_date=date.today())

print(result.report_path, result.headline, result.word_count)
```

Until the stages are wired up to real backends, calling `Orchestrator.run()`
raises `NotImplementedError`. The cron-agent path remains the source of
truth in the meantime.
