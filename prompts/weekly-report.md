# Weekly automation prompt — "Human in the AI Age"

This is the instruction set the weekly Cursor automation follows every Monday
(cron `30 3 * * 1`, 03:30 UTC) to generate a new brief.

## Mission

Pull thoughtful research and advice from the world's best practitioners — AI
subject-matter experts, neuroscientists, behavioural scientists, and academics —
on the best practices to keep humans **alive, sane, and actively using their brains**
while we are increasingly pulled toward depending on AI tools for everyday tasks at
work and in personal life.

## Each week, do this

1. **Research (web search).** Find the most relevant, recent, and credible material.
   Prioritise:
   - Named experts (neuroscientists, cognitive/behavioural scientists, leading AI
     researchers, respected academics and clinicians).
   - Peer-reviewed studies, reputable preprints, major institutional/policy reports
     (MIT, Stanford HAI, Microsoft Research, OECD, WEF, Nature/npj, etc.).
   - New developments from the **past week** where possible; otherwise the most
     significant findings of the past quarter.
   - At least one **dissenting / critical** perspective for balance.

2. **Verify.** Capture exact study sizes, journals, dates, and direct quotes. Flag
   anything that is a preprint or not yet peer-reviewed. Do not overstate findings.

3. **Write** a new brief at `reports/YYYY-MM-DD-human-in-the-ai-age.md` (date = the
   Monday of the week) following `reports/TEMPLATE.md`. Keep it skimmable: executive
   summary first, practical checklist near the top, sources at the bottom.

4. **Index.** Add the new brief to the top of the table in `reports/INDEX.md` and
   increment the issue number.

5. **Ship.** Commit on the working branch and open/update a pull request.

## Quality bar

- Every non-obvious claim has a linked source.
- Advice is **concrete and actionable** ("write the first draft before opening an
  LLM"), not vague ("be mindful").
- Tone: clear, calm, non-alarmist, evidence-led. Respect the reader's intelligence.
- Avoid repeating the previous week's content verbatim — lead with what is *new*,
  and rotate which experts/themes are foregrounded.

## Recurring themes to track over time

- Cognitive offloading, "cognitive debt," and deskilling.
- Deep reading / the reading brain, attention, and focus.
- Critical thinking, verification, and over-trust/automation bias.
- Behaviour design: attention vs. "attachment" tech, habit and friction design.
- Healthy human-in-the-loop patterns at work (delegation, oversight, judgment).
- Mental health, loneliness, and AI companionship.
- Education and child/adolescent development.
- Policy, governance, and worker-centred AI design.
