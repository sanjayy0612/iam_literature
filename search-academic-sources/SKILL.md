---
name: search-academic-sources
description: Search Semantic Scholar, OpenAlex, Crossref, and PubMed for academic records and abstracts using the bundled command-line utility. Use when finding papers by topic, comparing database coverage, resolving a DOI, collecting structured metadata, or creating a deduplicated discovery set for a literature review.
---

# Search Academic Sources

Use `scripts/lit_search.py` for structured discovery across supported scholarly APIs. Treat results as candidates for screening, not as proof that a search is comprehensive or that a claim is true.

## Requirements

- Python 3
- The `requests` package
- Network access to the selected public APIs

Optional environment variables:

| Variable | Purpose |
|---|---|
| `USER_EMAIL` | Contact address for polite API identification |
| `SEMANTIC_SCHOLAR_API_KEY` | Higher Semantic Scholar rate limits |
| `OPENALEX_API_KEY` | Authenticated OpenAlex access |

Never print, persist, or include API keys in reports.

## Search

Run commands from this skill directory:

```bash
python3 scripts/lit_search.py search "retrieval augmented generation evaluation" --limit 20 --source all
```

Supported source values:

- `s2` — Semantic Scholar
- `oa` — OpenAlex
- `cr` — Crossref
- `pm` — PubMed
- `both` — Semantic Scholar and OpenAlex
- `all` — all supported sources

Use a domain-specific source when appropriate. PubMed is strongest for biomedical indexing; Crossref is useful for DOI metadata but often lacks abstracts.

## Resolve a paper

Retrieve Semantic Scholar details using a DOI or supported paper identifier:

```bash
python3 scripts/lit_search.py details "DOI:10.1038/s41586-023-00000-0"
```

Verify the returned record against the DOI resolver or publisher before citing it.

## Interpret output

Records may include:

- Source identifier and DOI
- Title, year, authors, and venue
- Abstract when the source supplies one
- Citation count for sources that expose it
- Originating database

The utility deduplicates multi-source results by normalized DOI. Records without a DOI can remain duplicated; check normalized titles, authors, and years before counting.

## Build a reproducible discovery set

Record:

1. Exact query and source selection
2. Search date and result limit
3. API errors, rate limits, and missing fields
4. Deduplication method
5. Exported raw results before screening

Use multiple query formulations for systematic work. Supplement API discovery with discipline-specific databases, citation chasing, and full-text screening.

## Guardrails

- Do not describe metadata or an abstract as full-text evidence.
- Do not rank study quality by citation count alone.
- Do not infer that absent results prove a research gap.
- Keep peer-reviewed articles, preprints, corrections, and retractions distinguishable.
- Report partial API failures instead of silently treating them as zero results.
