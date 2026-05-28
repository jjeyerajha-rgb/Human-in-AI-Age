"""Stage 1 — Research agent (placeholder).

Pulls fresh primary research from the web on the standing theme:
"How humans can stay alive, sane, and cognitively active as AI tools take
over more of everyday work and personal life."

Real implementation should:
    - Query multiple sources (arXiv, Nature, MIT, Stanford HAI, expert
      podcasts, named-researcher Substacks).
    - Deduplicate against `reports/INDEX.md` so we do not recycle headlines.
    - Prefer primary sources with concrete numbers, sample sizes, and
      methodology.
    - Tag each finding by source type (peer-reviewed, preprint, expert
      commentary, news).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable


@dataclass
class ResearchFinding:
    """One unit of evidence pulled from the web."""

    title: str
    author: str
    year: int
    source_type: str        # peer_reviewed | preprint | book | podcast | news | substack
    venue: str
    url: str
    summary: str
    quantitative_claims: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


class ResearchAgent:
    """Placeholder. Will be replaced by a real web-research agent."""

    def __init__(self, *, max_findings: int = 10, freshness_days: int = 30) -> None:
        self.max_findings = max_findings
        self.freshness_days = freshness_days

    def gather(
        self,
        *,
        already_covered_headlines: Iterable[str] = (),
        as_of: date | None = None,
    ) -> list[ResearchFinding]:
        """Return a list of fresh ResearchFinding objects.

        Args:
            already_covered_headlines: lines from reports/INDEX.md so the
                agent can avoid recycling.
            as_of: anchor date for "fresh" (defaults to today).

        Today this returns an empty list — the cron-agent does the real
        research directly. Wire a search backend in here when ready.
        """
        # TODO: integrate a search backend (WebSearch tool, Tavily, Perplexity,
        # serpapi, etc.) and an LLM for filtering/summarisation.
        _ = already_covered_headlines, as_of
        return []
