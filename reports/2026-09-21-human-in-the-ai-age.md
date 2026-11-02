# Human in the AI Age — Weekly Brief

**Issue:** 013
**Week of:** Monday, 21 September 2026
**Generated:** 2026-08-31 03:30 UTC
**Editor:** Cursor Cloud Agent (automated weekly research)

---

## 1. Executive Summary

Issue 007 asked you to check the *load-bearing fact* in an AI answer. This week is the
layer underneath that: check that the **evidence even exists**. Large language models
now write with the grammar of scholarship — named authors, plausible titles, journal
abbreviations, even DOIs — and that surface has started to leak into the permanent
record. A May 2026 audit of **2.5 million** biomedical papers found **4,046**
fabricated citations across **2,810** published articles. The rate rose from roughly
**one in 2,828** papers in 2023 to **one in 458** in 2025 and **one in 277** in the
first seven weeks of 2026 — about a **twelve-fold** increase [1]. A concurrent
population-scale preprint, covering **111 million** references in **2.5 million**
manuscripts, conservatively estimates **146,932** hallucinated citations in 2025
*in four corpora alone* [2]. At top AI conferences, the *reference-level* rate stays
under one percent — and still, in 2025, roughly **one in twenty** NeurIPS and USENIX
Security papers carried at least *two* likely-hallucinated scholarly pointers after
peer review [3].

This is not “AI damages the brain.” It is a quieter failure: **epistemic offloading**.
Fluency used to be a costly signal of having done the work. In a language model it is
free. The brain’s vigilance system, evolved to doubt hesitant or self-interested
speakers, often stands down [4, 5]. What atrophies, if you never open the source, is
not a lobe. It is the *habit of knowing*.

**The single habit to start this week:** *open the source.* Before you paste a
citation, statistic, or “studies show” sentence from AI into anything you will sign —
an email, a slide, a memo, a tweet, homework — open the source and check two things:
**(1) it exists**, and **(2) it actually says that**. A title that looks real is not
evidence. A DOI that 404s is a gift. Treat both as the whole point of the interaction.

## 2. Why This Matters Now

For most of modern work, a bibliography was a costly object. You had to remember a
paper, find it, or copy it from a document you had actually read. That cost was the
verification. Generative models collapsed it. A half-remembered title becomes a
polished BibTeX line in seconds. The surrounding prose still *looks* like care:
claims are supported, references are alphabetized, the font is the same. What changed
is the chain of evidence underneath [3].

Science is the best-case domain for catching this class of error. Citations either
exist or they do not. Indexes already exist. Journals still have reviewers. And even
here, **85.3%** of unmatched references on bioRxiv survived into the PubMed Central
version of the same paper, and **78.8%** of estimated non-existent citations still
passed arXiv moderation [2]. More than **98%** of the biomedical papers in the Lancet
audit had seen no publisher action by February 2026 [1]. If the easiest hallucination
to detect is already in the archival record, the harder ones — a real paper cited for
a claim it does not make; a confident paragraph in a strategy memo with no paper
behind it at all — are already in your inbox.

That is the personal stake. You do not need to submit to NeurIPS to inherit the
problem. Every time a model answers “according to research…” in a health search, a
vendor comparison, or a school assignment, it is offering the same fluent pointer.
Issue 007 was automation complacency: trusting the *decision*. This week is
**epistemic complacency**: trusting the *footnote*.

## 3. Voices From the Field

### 3.1 Neuroscience & the Brain
- **Simone Rossi (University of Siena), Valter Fraccaro, and Riccardo Manzotti
  (IULM Milan)** published a peer-reviewed comment in *npj Artificial Intelligence*
  (January 2026) arguing that *how* you sit with a model, over weeks and months, is
  itself a plasticity regimen. Drawing on BCM synaptic-threshold theory, they
  hypothesize that passive copy-and-paste keeps postsynaptic activity below the
  threshold for long-term potentiation, while questioning, refining, and co-creating
  can push it above. Their practical frame is the **3R principle: Results, Responses,
  Responsibility**. An LLM produces *results* — statistically viable strings with no
  meaning of their own. A *response* is a result a human has interpreted, valued, and
  accepted the consequences of. That last step is **responsibility**, and it is not
  externalizable [6]. They are explicit that this is a **cognitive-hygiene
  hypothesis**, not a new scan of anyone’s cortex. The Kosmyna EEG preprint they cite
  remains unreviewed; treat 3R as a stance, not as a biomarker.
- The underlying rule is older than chatbots. **Alvaro Pascual-Leone** and colleagues’
  review of cortical plasticity is the “use it or lose it” backbone: synaptic efficacy
  and network organization are activity- and time-dependent across the lifespan [7].
  What you never practice — including the small act of retrieving a source and
  matching a claim to a paragraph — is what thins. Rossi’s group’s contribution is to
  name *verification* as the neural work worth protecting, not abstinence from the
  tool.
- **Norbert Schwarz and colleagues’** processing-fluency work is the cognitive
  mechanism that makes fabricated citations dangerous rather than merely sloppy.
  Statements that are easy to read feel more true. In a human speaker, fluency is
  expensive and therefore informative. In a transformer, fluency is the default
  output of next-token prediction, including when the token sequence names a paper
  that does not exist [4, 8]. The brain is not broken. It is applying a heuristic
  that used to work.

### 3.2 Behavioural Science & Habits
- **Dan Sperber, Hugo Mercier, and colleagues** named **epistemic vigilance**: a
  parallel process that runs alongside comprehension, watching for reasons to *doubt*
  a speaker — competence, benevolence, hesitation, stakes [5]. **Andrew Maynard
  (Arizona State University)** argues in a January 2026 preprint that conversational
  AI presents “honest non-signals”: real fluency, real helpfulness, real absence of
  self-interest, none of which carry the information those same features would carry
  in a person, because in a person they are costly to fake. Vigilance looks for
  *doubt-triggers*. In their absence, information is provisionally accepted. The
  model does not have to deceive you. It only has to fail to trip the alarm [4].
  Maynard’s paper is **theoretical**, not a trial. The useful prediction is
  practical: sophisticated users may be *more* vulnerable, because they are used to
  treating fluent, cited prose as the signature of a careful colleague.
- **Ethan Mollick (Wharton)** has been saying the applied version for two years: the
  **verisimilitude paradox**. As models get better, errors get harder for non-experts
  to see, so you need *more* vigilance, not less. A related, well-replicated
  behavioural trap: merely *being told* an explanation exists raises trust, even if
  nobody clicks it. A citation is that explanation. A bibliography is a stack of
  “I could check this.” Most people don’t.
- The cheap habit that actually closes the loop is older than AI. **Open the object.**
  Librarians taught this as “follow the footnote.” Experimental studies that *prompt*
  models to generate citations — rather than measuring what authors later ship —
  find fabrication rates from roughly **20% to 90%**, depending on model and domain
  [2, 9]. Those numbers are an *upper bound* on unattended model behaviour, not on
  your Tuesday memo. They are still the reason the two-check rule (exists? says
  that?) is worth the thirty seconds.

### 3.3 AI Practitioners & Researchers
- **Mark Russinovich (Microsoft Azure), Ram Shankar Siva Kumar, and Ahmed Salem**
  built **RefChecker** and ran it on **48,095** camera-ready papers from ICLR, ICML,
  NeurIPS, and USENIX Security (**2.61 million** extracted references). They count
  only identity-level failures — no matching work, or a substantial author-list
  mismatch — and explicitly *exclude* year/venue drift. Reference-level rates in 2025
  sit between **0.38% and 0.81%**. Paper-level exposure does not: **18.7–34.9%** of
  accepted 2025 papers had at least one likely-hallucinated reference; **1.9–5.1%**
  had at least two among academic-paper-like citations. Award papers were not exempt.
  Scanning ICLR 2025 cost about **four cents a paper**. They open-sourced the tool
  rather than naming authors, on the grounds that a single bad pointer is usually a
  workflow failure, not a hanging offence — and that **76.7%** of reviewers in a
  related survey report not checking references at all [3].
- **Zhenyue Zhao, Yihe Wang, Toby Stuart, Mathijs de Vaan, Paul Ginsparg, and
  Yian Yin** supply the population view. Unmatched citations existed before ChatGPT
  (parser noise, obscure venues). They treat the *excess* over the pre-2023 baseline
  as the hallucination signature. The excess is not a few garbage papers: it is a
  *thin film* of bad pointers inside otherwise ordinary manuscripts, concentrated
  among smaller and earlier-career teams, correlated with linguistic signs of
  LLM-assisted writing (**r = 0.441** at arXiv subfield), and biased toward already
  prominent, male-named scholars when the invented title maps to a real person [2].
  Ginsparg founded arXiv. The paper is a **preprint**; the design is conservative
  on purpose.
- **Maxim Topaz (Columbia Nursing / Data Science Institute)** and colleagues
  translated the same failure into medicine. Their CITADEL pipeline scanned PubMed
  Central’s open-access subset from 1 January 2023 to 18 February 2026. After
  requiring that a claimed title match no CrossRef, Google Scholar, or OpenAlex
  record, they were left with **4,046** fabrications in **2,810** papers. The
  acceleration is the story: mid-2024, when writing assistants moved from novelty to
  default workflow [1]. Topaz has said he found his *own* first fake reference when
  a journal queried a citation an AI tool had slipped into his draft. That is the
  practitioner lesson: the people who build the detectors still have to open the
  source.

### 3.4 Academia, Education & Policy
- *Nature Computational Science*’s August 2026 editorial is blunt: AI may polish
  language; it may not replace scholarly judgment. **Authorship stays human.
  Fabricating citations is a research-integrity breach.** Reviewers may use AI to
  tidy comments, not to *do* the review, and must not upload confidential manuscripts
  to public tools [10]. That is the adult version of this week’s habit, written as
  policy.
- **ICLR 2026** and **ICML 2026** now list hallucinated references among grounds for
  desk rejection, insisting on *evidence* rather than AI-detector scores. GPTZero
  reported **50** ICLR 2026 submissions with at least one *human-verified*
  hallucinated citation among **300** scanned — after those papers had already
  received three to five expert reviews [3]. Peer review is not a citation checker.
  It never was.
- **Accountability in Research** (2026) goes a step further for a narrower case:
  when citations *function as data* (reviews, bibliometrics) and an author is
  indifferent to fabrication risk, a hallucinated reference can meet the U.S. federal
  definition of research misconduct [11]. Most of us are not filing those papers.
  Most of us *are* filing the everyday equivalent: a slide that says “research
  shows,” a parent looking up a dose, a manager quoting a benchmark. The legal
  category is optional. The verification step is not.

## 4. The Evidence, Briefly

| Study | Who / N | Venue & date | Status | Headline |
|---|---|---|---|---|
| Topaz et al., CITADEL audit | 2.5M PubMed Central OA papers; 4,046 fake cites in 2,810 papers | *The Lancet* research letter, 7 May 2026 | Peer-reviewed | 1 in 2,828 papers (2023) → 1 in 277 (early 2026); ~12×; >98% no publisher action |
| Zhao et al., hallucinations in the wild | 111M refs / 2.5M papers (arXiv, bioRxiv, SSRN, PMC) | arXiv:2605.07723, 8 May 2026 | Preprint | ≥146,932 excess unmatched cites in 2025; 85.3% of bioRxiv unmatched persist to publication; 78.8% pass arXiv moderation |
| Russinovich, Siva Kumar & Salem, RefChecker | 48,095 camera-ready papers; 2.61M refs; ICLR/ICML/NeurIPS/USENIX | arXiv:2607.00738, July 2026 | Preprint | Ref-level <1%; ~1 in 20 NeurIPS/USENIX 2025 papers have ≥2 likely-hallucinated scholarly cites; ~$0.04/paper to audit |
| Rossi, Fraccaro & Manzotti, 3R principle | Commentary (no new dataset) | *npj Artif. Intell.* 2, 15 (27 Jan 2026) | Peer-reviewed comment | Results ≠ responses; responsibility is the non-externalizable step that may keep synapses in the LTP regime |
| Maynard, Cognitive Trojan Horse | Theoretical; draws on Sperber et al. 2010 | arXiv:2601.07085, 11 Jan 2026 (v2 May 2026) | Preprint | Fluency/helpfulness are “honest non-signals” that can bypass epistemic vigilance |
| *Nat. Comput. Sci.* editorial | Journal policy | *Nature Computational Science* 6, 803 (20 Aug 2026) | Editorial | AI is an aid; fabricating citations is a research-integrity breach; accountability stays human |

## 5. Do This Now — Practical Checklist

### At work
- **Two-check rule on anything you will sign.** If the model gave you a citation,
  number, or “according to X,” open the source. Confirm the work exists. Confirm the
  cited sentence is actually in it. If you cannot open it in sixty seconds, do not
  ship it.
- **Never let the model invent the bibliography.** Paste *your* real references in
  (or a DOI list) and ask it to *format* them. Generating related-work from a prompt
  is how phantom titles get into slides and papers.
- **Spot-check the load-bearing *source*, not just the load-bearing *claim*.** Issue
  007’s habit still holds. This week adds: the claim’s footnote is part of the
  load-bearing structure. A correct-sounding sentence with a fake pointer is still
  a miss.
- **If you lead a team, make verification a named step, not a vibe.** “Who opened
  this DOI?” is a forcing function. Russinovich’s cost figure is the institutional
  version: citation audit is now cheaper than a coffee per paper [3]. For a
  ten-citation memo, it is cheaper than a coffee, full stop.
- **Do not upload confidential drafts to public chatbots to “check the references.”**
  Nature’s peer-review rule is also a workplace rule [10]. Use a local lookup
  (Crossref, PubMed, your library) or an approved internal tool.

### In personal life
- **Health, money, and schoolwork get the same two checks.** “A study in 2024 found…”
  is not a finding. Search the title in Google Scholar or PubMed. If it is not there,
  the sentence is a rumour with good punctuation.
- **Ask the model for a quote plus a locator.** “Give me the sentence and the page
  or section.” Then read that sentence in the original. Models that cannot point
  have already told you they are guessing.
- **Keep one domain where you still go to the primary source first** — a medical
  decision, a large purchase, a child’s assignment. Outsource the formatting, not
  the knowing.
- **Teach the move, don’t just ban the tool.** For students (or yourself): AI may
  suggest search terms. *You* retrieve. *You* highlight. *You* write the claim.
  Bastani’s tutoring result from Issue 003 still applies: hints preserve learning;
  answers hollow it out. Verification is the adult form of the hint.

## 6. Myth vs. Reality

**Myth:** “If it passed peer review / came with a DOI / sounds academic, the citation
is real.”

**Reality:** Peer review is not a reference checker. Russinovich et al. found
likely-hallucinated citations in *accepted camera-ready* papers, including
award-winners; most affected bibliographies had only one bad pointer, which is
exactly the pattern reviewers miss [3]. Zhao et al. found that **85%** of unmatched
bioRxiv references were still there after journal publication [2]. A DOI can be
wrong, point at a different paper, or be invented. The test is not “does this look
like scholarship?” It is “can I open the work, and does it say this?”

A second, related myth: “Hallucinated citations are a science problem.” Science is
where we can *count* them. The same fluent-pointer failure in a legal filing, a
clinical note, a vendor RFP, or a parenting blog is harder to audit and, Zhao’s
group argues, likely *worse* — there is no Semantic Scholar for a paragraph in a
policy memo [2].

## 7. Caveats & Honest Limitations

- **Zhao et al. is a preprint.** “Hallucinated citations” there means *excess
  unmatched titles above a pre-LLM baseline*, not a human verdict on each reference.
  Parser failures, unindexed venues, and missing titles in some fields produce
  unmatched citations in 2020 too. The authors argue the *change* after 2023 is the
  signal. Field differences (SSRN at 1.91% vs bioRxiv at 0.21% by August 2025) show
  the estimate is not a single universal rate [2].
- **Russinovich et al. is also a preprint, and RefChecker uses LLMs** for noisy
  parsing and web-search escalation. The authors treat single-flag papers as the
  noisiest bin; the ≥2 and ≥5 tails are where they are most confident. They do not
  claim every flagged reference was generated by a chatbot — only that identity-level
  failures are now visible in the archival record, and that the high-count tail grew
  after ChatGPT [3].
- **The Lancet letter is peer-reviewed but observational.** Timing (mid-2024
  acceleration) is consistent with writing-assistant uptake; it does not prove that
  any given fake citation was produced by a named model. Their count is conservative
  (title must match *no* major database) and still only catches *non-existent*
  works, not real papers mis-cited [1].
- **Citation hallucination is the easy problem.** Zhao, Russinovich, and Topaz all
  say this. The harder error — a real source used to prop up a claim it does not
  support — has no cheap ground truth. This brief’s habit (open the source *and*
  check it says that) is aimed at both; the published numbers mostly measure the
  first.
- **Rossi et al. is a comment, not a trial.** BCM thresholds, LTP/LTD, and “System 0”
  are a framework. They cite the Kosmyna EEG preprint (already covered in the pilot
  issue) as *preliminary*. Do not tell anyone their synapses are decaying because
  they used Copilot on a Tuesday [6].
- **Maynard is a theoretical preprint.** Epistemic vigilance is a real research
  programme (Sperber et al., 2010). The “Cognitive Trojan Horse” is a hypothesis
  about how current LLM training objectives interact with that programme. Useful as
  a lens; not a measured bypass rate [4, 5].
- **This is literacy, not legal or clinical advice.** Fabricated citations in a
  manuscript can become a research-integrity matter [10, 11]. Fabricated citations
  in a health decision belong with a clinician and the actual paper, not with a
  chatbot’s bibliography.

## 8. Sources

1. **Topaz M**, Roguin N, Gupta P, Zhang Z, Peltonen L-M. “Fabricated citations: an
   audit across 2·5 million biomedical papers.” *The Lancet* 2026.
   https://doi.org/10.1016/S0140-6736(26)00603-3
   Columbia Nursing summary:
   https://www.nursing.columbia.edu/news/nearly-3-000-peer-reviewed-medical-papers-have-fake-citations-columbia-nursing-ai-assisted-audit-finds
2. **Zhao Z**, Wang Y, Stuart T, de Vaan M, Ginsparg P, Yin Y. “LLM hallucinations
   in the wild: Large-scale evidence from non-existent citations.” arXiv:2605.07723
   (8 May 2026). **Preprint.**
   https://arxiv.org/abs/2605.07723
3. **Russinovich M**, Siva Kumar RS, Salem A. “Phantom References: Hallucinated
   Citations That Survive Peer Review at Top-Tier Conferences.” arXiv:2607.00738
   (July 2026). **Preprint.** RefChecker: https://github.com/markrussinovich/refchecker
   https://arxiv.org/abs/2607.00738
4. **Maynard AD.** “The AI Cognitive Trojan Horse: How Large Language Models May
   Bypass Human Epistemic Vigilance.” arXiv:2601.07085 (11 Jan 2026; v2 26 May
   2026). **Preprint.**
   https://arxiv.org/abs/2601.07085
5. **Sperber D** et al. “Epistemic Vigilance.” *Mind & Language* 2010;25(4):359–393.
   https://doi.org/10.1111/j.1468-0017.2010.01394.x
6. **Rossi S, Fraccaro V, Manzotti R.** “The brain side of human-AI interactions in
   the long-term: the ‘3R principle’.” *npj Artificial Intelligence* 2026;2:15.
   https://doi.org/10.1038/s44387-025-00063-1
7. **Pascual-Leone A**, Amedi A, Fregni F, Merabet LB. “The plastic human brain
   cortex.” *Annual Review of Neuroscience* 2005;28:377–401.
   https://doi.org/10.1146/annurev.neuro.27.070203.144216
8. **Reber R, Unkelbach C.** “The epistemic status of processing fluency as source
   for judgments of truth.” *Review of Philosophy and Psychology* 2010;1:563–581.
   https://doi.org/10.1007/s13164-010-0039-7
9. **Walters WH, Wilder EI.** “Fabrication and errors in the bibliographic citations
   generated by ChatGPT.” *Scientific Reports* 2023;13:14045.
   https://doi.org/10.1038/s41598-023-41032-5
10. **Nature Computational Science.** “Responsible and transparent use of AI in
    scientific publishing.” *Nat Comput Sci* 2026;6:803 (20 August 2026). Editorial.
    https://doi.org/10.1038/s43588-026-01043-4
11. **Accountability in Research.** “Hallucinated citations produced by generative
    artificial intelligence may constitute research misconduct when citations
    function as data in scholarly papers.” 2026.
    https://doi.org/10.1080/08989621.2026.2645390

---

*This brief is generated automatically each week. It is a literacy project, not medical
or professional advice. Studies are summarized as accurately as possible with their
limitations noted; always consult primary sources (and, for health decisions, a
qualified clinician) before acting.*
