"""Stage 3 — Editor agent (placeholder).

Quality pass on the draft. Enforces the anti-patterns listed in
`prompts/weekly-report.md`:

    - No emojis.
    - No "in today's fast-paced world" filler.
    - Every expert mentioned must be named with affiliation.
    - Every quantitative claim must have a sample size and methodology.
    - At least one counter-voice (AI as cognitive amplifier).
    - Mix of geographies — not US-only.
    - Headline must not duplicate any line in reports/INDEX.md.

Returns a FinalReport ready to be written to disk by the orchestrator.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .synthesis_agent import DraftReport


@dataclass
class FinalReport:
    """Edited, ready-to-publish report."""

    draft: DraftReport
    markdown: str
    issues_fixed: list[str] = field(default_factory=list)
    remaining_warnings: list[str] = field(default_factory=list)


class EditorAgent:
    """Placeholder. Will call an LLM with the editorial checklist."""

    BANNED_PHRASES = (
        "in today's fast-paced world",
        "in the age of AI",   # too generic for a headline
        "game-changer",
        "revolutionize",
        "unlock the power",
    )

    def edit(self, draft: DraftReport, *, already_covered_headlines: list[str]) -> FinalReport:
        """Run the editorial checklist over a DraftReport."""
        # TODO: call LLM with the checklist; for now just pass the draft through.
        _ = already_covered_headlines
        return FinalReport(
            draft=draft,
            markdown=draft.markdown,
            issues_fixed=[],
            remaining_warnings=[],
        )
