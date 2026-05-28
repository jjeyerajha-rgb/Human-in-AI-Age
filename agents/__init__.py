"""Agent pipeline that produces the weekly Human-in-AI-Age digest.

Pipeline:
    research_agent  ->  synthesis_agent  ->  editor_agent  ->  orchestrator (write)

These modules are placeholders. Today the Cursor cron-agent performs all
stages in a single autonomous run guided by `prompts/weekly-report.md`.
The stubs here define the contracts so the pipeline can be replaced piece
by piece with real implementations (LangChain, OpenAI SDK, Anthropic SDK,
etc.) without changing the rest of the system.
"""

from .research_agent import ResearchAgent, ResearchFinding
from .synthesis_agent import SynthesisAgent, DraftReport
from .editor_agent import EditorAgent, FinalReport
from .orchestrator import Orchestrator

__all__ = [
    "ResearchAgent",
    "ResearchFinding",
    "SynthesisAgent",
    "DraftReport",
    "EditorAgent",
    "FinalReport",
    "Orchestrator",
]
