# Skill Selection Guide

## `plan-literature-review`

Use before searching. It converts a research idea into a bounded question, review type, eligibility criteria, database plan, reproducible queries, screening procedure, extraction schema, and synthesis plan.

## `search-academic-sources`

Use for structured discovery. Its Python utility queries Semantic Scholar, OpenAlex, Crossref, and PubMed, normalizes common metadata, and deduplicates DOI-bearing records. Results still require screening and source verification.

## `conduct-systematic-review`

Use to manage the full review process. It connects protocol, documented searches, deduplication, screening, appraisal, extraction, synthesis, and reporting while preserving an auditable evidence trail.

## `synthesize-scientific-literature`

Use after selecting studies. It organizes evidence around claims and themes, preserves contradictions and uncertainty, verifies citation metadata, and can produce a structured Markdown or PDF review.

## `identify-literature-gaps`

Use near the end of a bounded review. It converts documented omissions, inconsistencies, and limitations into cautious candidate gaps and answerable future-research questions.

## `analyze-research-gaps`

Use for deeper corpus-wide analysis. It maps coverage across populations, methods, time, theory, evidence quality, and implementation, then actively searches for counterexamples before prioritizing a gap.

## Quick choice

| Request | Skill |
|---|---|
| “Help me decide how to review this topic” | `plan-literature-review` |
| “Find papers and DOI metadata” | `search-academic-sources` |
| “Run a systematic or scoping review” | `conduct-systematic-review` |
| “Write a synthesis from these studies” | `synthesize-scientific-literature` |
| “What gaps follow from this review?” | `identify-literature-gaps` |
| “Is this claimed gap real across the field?” | `analyze-research-gaps` |
