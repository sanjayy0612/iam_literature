---
name: analyze-research-gaps
description: Identify, test, and prioritize defensible gaps in a research corpus or literature search. Use when analyzing papers, PDFs, bibliographies, evidence tables, research notes, or a topic to find missing populations, contexts, methods, mechanisms, time periods, conflicting findings, weak evidence, or unanswered questions; when planning a thesis, grant, experiment, or future-research agenda; or when auditing whether a claimed research gap is genuinely supported.
---

# Analyze Research Gaps

Identify gaps supported by an explicit evidence base. Distinguish a genuine research gap from incomplete retrieval, inaccessible sources, or an overly narrow search.

## Establish the scope

Determine:

- The question or decision the gap must inform
- The available corpus: files, URLs, bibliography, evidence table, or topic-only request
- Relevant dates, populations, contexts, methods, and source types
- Whether the goal is a thesis, grant, experiment, product decision, or field map

Ask only the two or three questions that would materially change the analysis. If the user requests immediate work, state reasonable assumptions and proceed.

When only a topic is provided, gather evidence with the available research tools. For a systematic search or formal source-quality assessment, apply `conduct-systematic-review` as the companion workflow.

## Build an evidence inventory

Record, when available, for every included source:

- Citation, year, DOI or stable URL, and publication status
- Population, setting, geography, and timeframe
- Research question, theory, and proposed mechanism
- Study design, sample or dataset, comparator, and outcome
- Main findings, uncertainty, limitations, and conflicts of interest
- Evidence quality and relevance to the scoped question
- Themes and claims the source supports or challenges

Deduplicate records before counting coverage. Keep peer-reviewed work, preprints, reviews, and gray literature distinguishable.

## Map coverage

Analyze dimensions relevant to the question:

1. **Knowledge** — unanswered phenomena or relationships
2. **Population and context** — missing groups, regions, settings, or operating conditions
3. **Temporal** — absent historical periods, follow-up durations, or recent evidence
4. **Methodological** — missing designs, comparators, measurements, replications, or validation
5. **Theoretical and mechanistic** — untested explanations, mediators, moderators, or causal pathways
6. **Contradiction** — inconsistent findings that have not been resolved
7. **Evidence quality** — small samples, bias, weak controls, low power, or poor reproducibility
8. **Implementation** — limited feasibility, safety, cost, adoption, scalability, or real-world evidence

Use counts only as descriptive evidence. Do not treat an arbitrary paper-count threshold as proof of adequacy.

## Test every candidate gap

For each proposed gap:

1. State the gap as a precise, falsifiable claim.
2. List the evidence showing what has already been studied.
3. Search specifically for counterexamples and near-matches.
4. Explain whether the issue is absence, scarcity, inconsistency, low quality, or limited generalizability.
5. Record search boundaries and inaccessible evidence.
6. Assign confidence:
   - **High** — broad, reproducible search with no material counterexample
   - **Moderate** — multiple sources support the gap but coverage is incomplete
   - **Low** — based on a small corpus, abstracts, narrow retrieval, or uncertain terminology

Use cautious language such as “little evidence was identified within this search scope.” Reserve “no research exists” for exceptionally comprehensive evidence.

## Prioritize gaps

Rank defensible gaps using importance, confidence, contribution, feasibility, ethics, urgency, affected population, and duplication risk. Keep novelty separate from importance.

## Produce the report

Return:

1. Scope and search boundary
2. Coverage map
3. Prioritized gap table with evidence, counterevidence, confidence, importance, feasibility, and next step
4. Concrete searches to challenge each gap
5. Answerable research questions or study designs
6. Limitations, including paywalls, language restrictions, missing full text, and indexing bias

Cite sources next to supported claims. Clearly mark conclusions based only on abstracts or metadata.

## Guardrails

- Never infer a research gap solely because an initial search returned few results.
- Never invent citations, DOI values, corpus counts, quality ratings, or search coverage.
- Do not confuse a paper's future-work suggestion with an independently verified gap.
- Check synonyms, terminology changes, neighboring disciplines, corrections, and retractions.
- Distinguish “not studied,” “not found,” “not accessible,” and “not adequately studied.”
