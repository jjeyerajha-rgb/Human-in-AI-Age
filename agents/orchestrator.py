"""Stage 4 — Orchestrator (placeholder).

Coordinates the pipeline:

    research -> synthesis -> editor -> write to disk + update INDEX.md

The Cursor cron-agent calls this once a week. Until the individual stages
are wired up to real LLM/search backends, the orchestrator simply exposes
the contract and the file-write logic that any implementation will need.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .research_agent import ResearchAgent
from .synthesis_agent import SynthesisAgent
from .editor_agent import EditorAgent


REPO_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = REPO_ROOT / "reports"
PROMPTS_DIR = REPO_ROOT / "prompts"
INDEX_PATH = REPORTS_DIR / "INDEX.md"
STANDING_BRIEF_PATH = PROMPTS_DIR / "weekly-report.md"


@dataclass
class RunResult:
    report_path: Path
    headline: str
    word_count: int


class Orchestrator:
    """End-to-end pipeline. Currently a placeholder."""

    def __init__(
        self,
        *,
        researcher: ResearchAgent | None = None,
        synthesiser: SynthesisAgent | None = None,
        editor: EditorAgent | None = None,
    ) -> None:
        self.researcher = researcher or ResearchAgent()
        self.synthesiser = synthesiser or SynthesisAgent()
        self.editor = editor or EditorAgent()

    def _read_already_covered_headlines(self) -> list[str]:
        if not INDEX_PATH.exists():
            return []
        return [line.strip() for line in INDEX_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]

    def _read_standing_brief(self) -> str:
        if not STANDING_BRIEF_PATH.exists():
            return ""
        return STANDING_BRIEF_PATH.read_text(encoding="utf-8")

    def run(self, *, edition_date: date | None = None) -> RunResult:
        """Run the full pipeline and write the report to disk.

        This is the function the cron-agent should ultimately invoke once the
        individual stages have real implementations. Today it raises
        NotImplementedError so callers know to use the human-in-the-loop
        cron-agent path instead.
        """
        edition_date = edition_date or date.today()

        already = self._read_already_covered_headlines()
        brief = self._read_standing_brief()

        findings = self.researcher.gather(already_covered_headlines=already)
        draft = self.synthesiser.synthesise(findings, edition_date=edition_date, standing_brief=brief)
        final = self.editor.edit(draft, already_covered_headlines=already)

        if not final.markdown.strip():
            raise NotImplementedError(
                "Agent stages are still placeholders. The Cursor cron-agent "
                "currently produces reports directly using prompts/weekly-report.md."
            )

        report_path = REPORTS_DIR / f"{edition_date.isoformat()}.md"
        report_path.write_text(final.markdown, encoding="utf-8")

        self._append_to_index(edition_date, final.draft.headline_finding_one_liner, report_path)

        return RunResult(
            report_path=report_path,
            headline=final.draft.headline_finding_one_liner,
            word_count=len(final.markdown.split()),
        )

    @staticmethod
    def _append_to_index(edition_date: date, headline: str, report_path: Path) -> None:
        if not INDEX_PATH.exists():
            INDEX_PATH.write_text("# Weekly Report Index\n\n", encoding="utf-8")
        line = f"| {edition_date.isoformat()} | {headline} | [report](./{report_path.name}) |\n"
        with INDEX_PATH.open("a", encoding="utf-8") as f:
            f.write(line)


if __name__ == "__main__":
    Orchestrator().run()
