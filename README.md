# Portable Research Skills

Six agent-neutral skills for planning, discovering, reviewing, synthesizing, and auditing scientific literature. The shared `SKILL.md` files avoid vendor-specific tool names and work as portable instruction bundles for agents that support the Agent Skills directory pattern.

Codex-specific UI metadata lives in each optional `agents/openai.yaml`; it does not alter the shared workflow.

## Skills

| Skill | Use it for |
|---|---|
| `plan-literature-review` | Design a review question, protocol, search strategy, eligibility criteria, and screening plan |
| `search-academic-sources` | Query Semantic Scholar, OpenAlex, Crossref, and PubMed through a bundled Python utility |
| `conduct-systematic-review` | Run an auditable systematic, scoping, or rapid review from protocol through reporting |
| `synthesize-scientific-literature` | Build a claim-linked synthesis and verified review document from selected studies |
| `identify-literature-gaps` | Derive candidate gaps from an existing bounded review or evidence summary |
| `analyze-research-gaps` | Test and prioritize gaps across a corpus, including searches for counterexamples |

## Recommended workflow

```text
plan-literature-review
        ↓
search-academic-sources
        ↓
conduct-systematic-review
        ↓
synthesize-scientific-literature
        ↓
identify-literature-gaps
```

Use `analyze-research-gaps` when the main task is a deeper coverage audit rather than the final step of one review.

## Install selectively

Review a skill and its scripts before installing it. Copy only the folders you need.

For a personal Codex installation:

```bash
cp -R plan-literature-review ~/.codex/skills/
```

For Claude Code or another compatible agent, copy the folder into that product's documented personal or project skills directory. Installation locations and supported metadata vary by agent version; the portable contract is the skill folder and its `SKILL.md`.

After installation, restart or reload the agent if it does not discover the skill immediately.

## Dependencies

- All instruction-only skills can operate with the host agent's available file, browsing, and document tools.
- `search-academic-sources/scripts/lit_search.py` requires Python 3, `requests`, network access, and access to the selected scholarly APIs.
- `conduct-systematic-review` bundles Python 3 utilities that use only the standard library.
- `synthesize-scientific-literature/scripts/verify_citations.py` requires `requests` and network access.
- PDF generation additionally requires the converters documented by `scripts/generate_pdf.py`.

Never store API keys in this repository. Use environment variables described by the relevant skill.

## Validation

Every skill keeps its shared YAML frontmatter to `name` and `description`, uses a matching folder name, and stays below 500 lines. Bundled Python files are syntax-checked before release. Platform-specific metadata is optional and isolated from the shared instructions.

## Provenance

This collection began as reviewed copies of third-party community skills and has since been rewritten for portability, clearer boundaries, and stronger evidence guardrails.

| Current folder | Upstream source | Pinned version |
|---|---|---|
| `conduct-systematic-review` | `borghei/Claude-Skills`, `research/litreview` | `ddca910e95580c63a236303fc1534054f0f14d4c` |
| `synthesize-scientific-literature` | `davila7/claude-code-templates`, `scientific/literature-review` | `5ee4e51edbbc0bc4355f023e497d9efc1d6cc93d` |
| `analyze-research-gaps` | `jmagly/aiwg`, `research-gap` | `f33d13476b9567299374d269b653dd56f444744c` |
| `plan-literature-review` | `eyadsibai/ltk`, `literature-review` | `f8e85697b95d8e4968cff3c49d20e632048faae9` |
| `search-academic-sources` | LobeHub package `openclaw-skills-literature-review` | `1.2.0` |
| `identify-literature-gaps` | MCP Market rendered instructions; advertised GitHub source unavailable | Marketplace transcription |

Review upstream licensing before redistribution or commercial use. In particular, the original Borghei package declared `MIT + Commons Clause`; this repository does not replace upstream license terms.

## Evidence safeguards

Across the collection:

- Metadata and abstracts are not represented as full-text evidence.
- “Not found” is distinguished from “no research exists.”
- DOI resolution verifies identity, not the truth of a claim.
- Preprints, peer-reviewed work, corrections, and retractions remain distinguishable.
- Search counts, reviewer participation, quality ratings, and citations must never be invented.
