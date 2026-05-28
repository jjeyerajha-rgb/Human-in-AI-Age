# Weekly Report Generation Prompt

This file is the **standing brief** for the Cursor automation that runs every
Monday at 03:30 UTC (`30 3 * * 1`). When the cron fires, follow the steps
below.

---

## Goal

Produce one new Markdown report at `reports/YYYY-MM-DD.md` (use the Monday's
date) on the theme:

> Thoughtful research and practical advice — pulled from the world's best
> AI researchers, neuroscientists, behavioural scientists, and academics — on
> how to keep humans **alive, sane, curious, and cognitively active** as AI
> tools take over more of our everyday work and personal life.

Reports must be substantive, citation-rich, and _practical_. Treat the reader
as a thoughtful professional who already uses AI tools daily.

---

## Required sections

Every weekly report should contain, in this order:

1. **Headline finding of the week** — one new study, paper, or expert
   statement from the past 7–14 days. Include numbers, methodology, and
   limitations.
2. **What the world's best practitioners are recommending** — synthesise
   recommendations from 4–8 named experts. Mix AI researchers (e.g. Stuart
   Russell, Yoshua Bengio, Demis Hassabis, Fei-Fei Li, Pattie Maes, Nataliya
   Kosmyna), neuro/behavioural scientists (e.g. Adam Gazzaley, Richard
   Davidson, Lisa Feldman Barrett, Daniel Kahneman's legacy, Andrew
   Huberman, Wendy Suzuki, Nate Kornell, Maryanne Wolf), philosophers of mind
   (Andy Clark, David Chalmers), and operator-academics (Cal Newport, Ethan
   Mollick, Andrew Ng).
3. **A 10-rule best-practice playbook** — concrete, copy-pasteable.
4. **Open questions to sit with this week** — 3–5 reflective prompts.
5. **Sources** — with authors, year, venue, and a one-line description.
6. **Pointer to next edition** — date of the next Monday.

---

## Research instructions for the agent

1. Run **at least 4 fresh web searches**. Vary the angles:
   - Latest peer-reviewed neuroscience on AI cognitive effects (last ~30 days).
   - Behavioural science / decision science on AI dependency.
   - Specific practitioner advice from named experts.
   - Counter-evidence or contrarian voices (we are not running a doom blog).
2. Prefer **primary sources** — arXiv, Nature, PNAS, MIT, Stanford HAI,
   Berkeley CHAI, university press releases, expert podcasts (Lex Fridman,
   Knowledge Project, Huberman Lab, Ezra Klein), Substacks of named
   researchers.
3. Where claims are quantitative, **include the number** (e.g. "55% drop in
   alpha-band connectivity") and the **sample size + study design**.
4. Avoid recycling the same MIT EEG study every week — _rotate the headline_.
   Keep a running list of already-covered studies in `reports/INDEX.md` and
   pick something new.
5. No emojis. No "in today's fast-paced world" filler. Direct, dense prose.

---

## Style guide

- **Tone:** Calm, evidence-based, practical. Not alarmist, not techno-utopian.
- **Voice:** "We" when describing shared human condition; second person when
  giving instructions to the reader.
- **Length:** ~1500–2500 words.
- **No emojis.**
- **No marketing language.**
- Use tables when comparing groups / conditions / studies.
- Use blockquotes for direct quotes from named experts.
- Always include at least one **counter-voice** — someone who argues AI is
  _enhancing_ human cognition under the right conditions (e.g. Ethan Mollick,
  Andy Clark, Andrew Ng). This is not a moral panic newsletter.

---

## Mechanics

1. Branch: stay on `cursor/ai-human-best-practices-5584` (see Cloud Agent
   config).
2. Write the report to `reports/YYYY-MM-DD.md` where the date is the Monday
   on which the cron fires.
3. Append a one-line entry to `reports/INDEX.md`:
   ```
   - [YYYY-MM-DD](./YYYY-MM-DD.md) — <headline finding in <10 words>>
   ```
4. Commit with message:
   `report: weekly digest YYYY-MM-DD`
5. Push to origin.
6. Do **not** open a PR or modify any other files unless the user asks.

---

## Anti-patterns to avoid

- Repeating last week's headline.
- Vague "experts say" without naming the expert and the source.
- Long quotations without a take-away.
- US-only sources — pull from EU, India, Japan, and Latin American
  researchers when possible.
- Treating AI as a single thing. Distinguish chat assistants, agentic
  systems, recommender systems, and embedded copilots — they have different
  cognitive effects.
- Generic productivity advice that has nothing to do with the AI angle.
