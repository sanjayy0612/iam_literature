---
name: synthesize-scientific-literature
description: Synthesize an already selected set of scientific studies into a traceable narrative, thematic synthesis, evidence table, or review document with verified citations. Use when comparing study findings, reconciling contradictions, evaluating evidence strength, drafting results and discussion sections, formatting references, or producing Markdown or PDF output from an established evidence set.
---

# Synthesize Scientific Literature

Turn a selected evidence set into a claim-linked synthesis. Do not silently expand the corpus or present metadata and abstracts as if they were full-text evidence.

## Confirm inputs

Require:

- The synthesis question and intended audience
- The included-study set and selection boundary
- Available full text, extracted data, and quality assessments
- Desired synthesis type and output format
- Required citation style

If study selection is still in progress, use `conduct-systematic-review`. If only a topic is provided, first use `plan-literature-review` and suitable discovery tools.

## Normalize evidence

Create or verify an evidence table containing:

- Citation and persistent identifier
- Publication status
- Design, population or dataset, setting, and sample size
- Intervention, exposure, comparator, and outcomes where applicable
- Effect estimate or principal finding with uncertainty
- Limitations, funding, conflicts, and quality assessment
- Source location for every extracted claim

Separate reported results from interpretation. Mark fields unavailable from the source rather than inferring them.

Use `scripts/search_databases.py` to normalize and deduplicate compatible JSON exports:

```bash
python3 scripts/search_databases.py results.json --deduplicate --format json --output unique_results.json
```

## Choose the synthesis method

- **Narrative** for heterogeneous evidence and explanatory comparison
- **Thematic** for recurring concepts or qualitative findings
- **Framework** for a predefined model or set of questions
- **Quantitative** only when outcomes, designs, populations, and effect measures are sufficiently comparable

Do not call a numerical summary a meta-analysis without an explicit statistical model, heterogeneity assessment, and reproducible inputs.

## Synthesize across studies

Organize around claims or themes, not one paragraph per paper. For each claim:

1. State the conclusion and its scope.
2. Cite the studies that support it.
3. Describe contradictory or null findings.
4. Explain relevant differences in design, population, measurement, or context.
5. State evidence strength and residual uncertainty.

Avoid vote counting based only on the number of positive and negative studies.

## Verify citations

Use `scripts/verify_citations.py` to check DOI resolution and Crossref metadata:

```bash
python3 scripts/verify_citations.py review.md
```

Resolve mismatches manually against the paper or publisher record. DOI resolution verifies identity, not the truth of a claim.

Read `references/citation_styles.md` for supported formatting patterns and `references/database_strategies.md` only when documenting how the supplied evidence set was discovered.

## Produce the review

Use `assets/review_template.md` when a full review document is requested. Include:

1. Question, scope, and evidence boundary
2. Methods used to select and synthesize studies
3. Study-characteristics or evidence table
4. Claim-linked thematic or quantitative results
5. Contradictions and evidence-strength judgments
6. Limitations and research implications
7. Verified references

Generate a PDF only when requested and the required conversion tools are available:

```bash
python3 scripts/generate_pdf.py review.md review.pdf
```

Visualizations are optional and should be included only when they materially clarify selection flow, evidence structure, or findings.

## Guardrails

- Never invent findings, effect sizes, sample sizes, quotations, or citations.
- Never attribute a claim to a paper without locating support in the available source.
- Label abstract-only evidence and inaccessible full text.
- Keep preprints, peer-reviewed papers, corrections, and retractions distinguishable.
- Preserve disagreement and uncertainty instead of forcing consensus.
