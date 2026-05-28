"""Stage 2 — Synthesis agent (placeholder).

Takes raw ResearchFinding objects and produces a draft report that follows
the structure mandated by `prompts/weekly-report.md`:

    1. Headline finding of the week
    2. What the world's best practitioners are recommending (4-8 named experts)
    3. 10-rule best-practice playbook
    4. Open questions to sit with this week
    5. Sources
    6. Pointer to next edition

Real implementation should:
    - Use an LLM with the standing brief loaded as system context.
    - Always include at least one counter-voice.
    - Mix AI researchers, neuro/behavioural scientists, philosophers of
      mind, and operator-academics.
    - Avoid recycling headlines covered in reports/INDEX.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from .research_agent import ResearchFinding


@dataclass
class DraftReport:
    """A first-pass synthesis ready for the editor agent."""

    edition_date: date
    title: str
    markdown: str
    headline_finding_one_liner: str
    cited_findings: list[ResearchFinding]


class SynthesisAgent:
    """Placeholder. Will call an LLM with the standing brief loaded."""

    def __init__(self, *, target_word_count: tuple[int, int] = (1500, 2500)) -> None:
        self.target_word_count = target_word_count

    def synthesise(
        self,
        findings: list[ResearchFinding],
        *,
        edition_date: date,
        standing_brief: str,
    ) -> DraftReport:
        """Produce a DraftReport from findings + the standing brief."""
        # TODO: call LLM with standing_brief + findings, enforce template.
        _ = findings, standing_brief
        return DraftReport(
            edition_date=edition_date,
            title=f"Human in the AI Age — week of {edition_date.isoformat()}",
            markdown="",
            headline_finding_one_liner="",
            cited_findings=[],
        )
