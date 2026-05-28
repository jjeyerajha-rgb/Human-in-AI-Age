"""
Human in the AI Age — Streamlit dashboard.

Browse the weekly research digests that the Cursor cron-agent commits to
the `reports/` directory.

Run locally:
    pip install -r requirements.txt
    streamlit run app/streamlit_app.py
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

import streamlit as st


REPO_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = REPO_ROOT / "reports"
PROMPTS_DIR = REPO_ROOT / "prompts"
AGENTS_DIR = REPO_ROOT / "agents"


def _parse_date_from_name(name: str) -> datetime | None:
    """Pull a YYYY-MM-DD prefix out of a report filename."""
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", name)
    if not match:
        return None
    try:
        return datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    except ValueError:
        return None


def _first_non_empty_line(text: str, skip_prefixes: tuple[str, ...] = ("#", ">", "|", "-")) -> str:
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if any(line.startswith(p) for p in skip_prefixes):
            continue
        return line
    return ""


def _extract_title(text: str, fallback: str) -> str:
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    return fallback


def list_reports() -> list[dict]:
    if not REPORTS_DIR.exists():
        return []
    reports: list[dict] = []
    for path in REPORTS_DIR.glob("*.md"):
        if path.name.upper() == "INDEX.MD":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        reports.append(
            {
                "path": path,
                "name": path.stem,
                "date": _parse_date_from_name(path.name),
                "title": _extract_title(text, fallback=path.stem),
                "summary": _first_non_empty_line(text),
                "word_count": len(text.split()),
                "text": text,
            }
        )
    reports.sort(key=lambda r: (r["date"] or datetime.min), reverse=True)
    return reports


def render_header() -> None:
    st.set_page_config(
        page_title="Human in the AI Age",
        page_icon=None,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(
        """
        <style>
            .hiaa-tag {
                display: inline-block;
                padding: 2px 10px;
                border-radius: 999px;
                background: #f1f3f5;
                color: #495057;
                font-size: 0.75rem;
                margin-right: 6px;
            }
            .hiaa-meta { color: #6c757d; font-size: 0.85rem; }
            .hiaa-card {
                padding: 18px 20px;
                border: 1px solid #e9ecef;
                border-radius: 12px;
                margin-bottom: 14px;
                background: #ffffff;
            }
            .hiaa-card h4 { margin: 0 0 4px 0; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("Human in the AI Age")
    st.caption(
        "A weekly research digest on staying alive, sane, and cognitively active "
        "while AI tools take over more of our everyday work and personal lives."
    )


def render_sidebar(reports: list[dict]) -> dict | None:
    st.sidebar.header("Editions")
    if not reports:
        st.sidebar.info("No reports yet. The first cron run will populate this.")
        return None
    labels = [
        f"{r['date'].strftime('%Y-%m-%d') if r['date'] else r['name']}  ·  {r['title'][:48]}"
        for r in reports
    ]
    idx = st.sidebar.radio(
        "Pick a week", options=list(range(len(reports))), format_func=lambda i: labels[i]
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Schedule**")
    st.sidebar.markdown("`30 3 * * 1` — Mondays 03:30 UTC")
    st.sidebar.markdown("**Branch**")
    st.sidebar.code("cursor/ai-human-best-practices-5584", language="text")
    st.sidebar.markdown("**Standing brief**")
    if (PROMPTS_DIR / "weekly-report.md").exists():
        with st.sidebar.expander("View the prompt the agent follows"):
            st.markdown((PROMPTS_DIR / "weekly-report.md").read_text(encoding="utf-8"))
    return reports[idx]


def render_overview(reports: list[dict]) -> None:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total editions", len(reports))
    if reports:
        latest = reports[0]
        col2.metric(
            "Latest edition",
            latest["date"].strftime("%d %b %Y") if latest["date"] else latest["name"],
        )
        col3.metric("Latest length (words)", f"{latest['word_count']:,}")
    avg = int(sum(r["word_count"] for r in reports) / len(reports)) if reports else 0
    col4.metric("Avg length (words)", f"{avg:,}")
    st.markdown(" ")


def render_report(report: dict) -> None:
    date_str = report["date"].strftime("%A, %d %B %Y") if report["date"] else "unknown date"
    st.markdown(
        f"<div class='hiaa-meta'>"
        f"<span class='hiaa-tag'>{date_str}</span>"
        f"<span class='hiaa-tag'>{report['word_count']:,} words</span>"
        f"<span class='hiaa-tag'>{report['path'].name}</span>"
        f"</div>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown(report["text"])


def render_archive(reports: list[dict]) -> None:
    st.subheader("All editions")
    if not reports:
        st.info("No reports yet.")
        return
    for r in reports:
        date_str = r["date"].strftime("%d %b %Y") if r["date"] else r["name"]
        st.markdown(
            f"<div class='hiaa-card'>"
            f"<h4>{r['title']}</h4>"
            f"<div class='hiaa-meta'>{date_str} · {r['word_count']:,} words · "
            f"<code>{r['path'].name}</code></div>"
            f"<p style='margin-top:8px;'>{r['summary']}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )


def render_pipeline_status() -> None:
    st.subheader("Agent pipeline")
    st.caption(
        "The weekly report is produced by a four-stage agent pipeline. "
        "These are placeholder stubs today; the Cursor cron-agent currently "
        "performs all stages in a single run."
    )
    stages = [
        ("research_agent", "Pulls fresh primary research from the web"),
        ("synthesis_agent", "Synthesises findings into the report template"),
        ("editor_agent", "Quality pass — tone, citations, anti-patterns"),
        ("orchestrator", "Coordinates the pipeline and writes to disk"),
    ]
    cols = st.columns(len(stages))
    for col, (name, blurb) in zip(cols, stages):
        path = AGENTS_DIR / f"{name}.py"
        status = "ready (stub)" if path.exists() else "missing"
        col.markdown(
            f"**{name}**  \n<span class='hiaa-meta'>{blurb}</span>  \n"
            f"<span class='hiaa-tag'>{status}</span>",
            unsafe_allow_html=True,
        )


def main() -> None:
    render_header()
    reports = list_reports()
    selected = render_sidebar(reports)

    tab_latest, tab_archive, tab_pipeline = st.tabs(["Current edition", "Archive", "Pipeline"])

    with tab_latest:
        render_overview(reports)
        if selected:
            render_report(selected)
        else:
            st.info("No report selected yet.")

    with tab_archive:
        render_archive(reports)

    with tab_pipeline:
        render_pipeline_status()


if __name__ == "__main__":
    main()
