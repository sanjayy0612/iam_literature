---
name: conduct-systematic-review
description: Conduct or audit a reproducible systematic, scoping, or rapid literature review from protocol through screening, quality assessment, synthesis, and reporting. Use when a review requires explicit eligibility criteria, documented searches, deduplication, selection records, source-quality assessment, PRISMA-style reporting, or an auditable evidence trail.
---

# Conduct a Systematic Review

Run a transparent review workflow while preserving a complete audit trail. Calibrate rigor to the declared review type and available reviewers.

## Establish the protocol

Confirm the question, review type, eligibility criteria, sources, timeframe, outcomes, and synthesis goal. If no protocol exists, create one with `plan-literature-review` before screening results.

Use the question framework appropriate to the domain. PICO is useful for interventions; PEO, SPIDER, PCC, or a concept map may fit other questions better.

## Build and document searches

Use `scripts/search_strategy_builder.py` to draft a strategy from structured inputs:

```bash
python3 scripts/search_strategy_builder.py --input question.json --format markdown
```

For every database, preserve the exact query, interface, filters, search date, result count, and export format. Add citation chasing or gray-literature searches when the protocol requires them.

Read `references/search-strategy-and-prisma.md` when developing detailed database searches or reporting the selection flow.

## Manage records and screening

1. Preserve raw exports unchanged.
2. Normalize metadata and deduplicate by DOI, then title/author/year.
3. Apply title/abstract criteria.
4. Retrieve and screen full text.
5. Record one explicit exclusion reason for every excluded full text.
6. Track counts through each stage for the flow report.

Do not claim independent dual screening unless two reviewers actually completed it. When screening is performed by one person or agent, disclose that limitation.

## Assess evidence quality

Select a design-appropriate appraisal method. Use `scripts/source_quality_scorer.py` for transparent triage support, not as a substitute for a validated domain instrument:

```bash
python3 scripts/source_quality_scorer.py --input sources.json --format markdown
```

Read `references/source-quality-assessment.md` before finalizing quality judgments. Keep methodological quality, relevance, publication status, and citation impact separate.

## Extract and synthesize

Define extraction fields before reading outcomes. Capture study design, population or dataset, setting, interventions or exposures, comparators, outcomes, effect estimates, uncertainty, limitations, funding, and conflicts.

Use `scripts/thematic_synthesis_builder.py` only after sources have been tagged consistently:

```bash
python3 scripts/thematic_synthesis_builder.py --input tagged_sources.json --format markdown
```

Read `references/synthesis-and-citation-management.md` for synthesis selection and citation hygiene. Do not pool quantitatively when studies are not sufficiently comparable.

## Report the review

Include:

1. Objective, protocol, and amendments
2. Complete search methods
3. Eligibility and screening process
4. Selection-flow counts
5. Included-study characteristics
6. Quality or risk-of-bias findings
7. Thematic or quantitative synthesis
8. Certainty, limitations, and potential biases
9. Verified references and data availability

Use cautious language when evidence is sparse, inconsistent, indirect, or based only on abstracts.

## Guardrails

- Never invent search counts, reviewer agreement, extracted values, citations, or quality scores.
- Never cite a source that has not been opened or otherwise verified.
- Separate “not found in this search” from “no research exists.”
- Treat protocol deviations as amendments and explain their impact.
- Check corrections and retractions before final reporting.
