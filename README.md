# Research Skills Collection

This repository contains a curated set of research-oriented skill definitions for literature review, gap analysis, citation management, and research synthesis. The folders here are local copies of community or third-party skill packs that were collected for review and reuse in projects that need systematic academic research support.

The purpose of the collection is simple: to make it easy to compare different literature-review and research-gap workflows, keep a record of provenance, and reuse the most useful patterns in a local environment.

## What is in this codebase?

Each folder represents a different approach to research support:

- `aiwg-research-gap` focuses on identifying missing coverage in a corpus and recommending where additional literature is needed.
- `borghei-litreview` provides a more structured literature-review workflow, including search strategy, source quality assessment, thematic synthesis, and citation hygiene.
- `davila7-literature-review` is oriented toward systematic literature review execution, database searching, citation verification, and document generation.
- `ltk-literature-review` offers a concise academic review guide centered on planning, searching, screening, synthesis, and quality assessment.
- `openclaw-literature-review` focuses on multi-source academic search using Semantic Scholar, OpenAlex, Crossref, and PubMed APIs.
- `mcpmarket-literature-gap-rendered` preserves a recovered version of a literature-gap skill description when the original marketplace source could not be directly downloaded.

## Skill descriptions and intended use

### 1. AIWG Research Gap
Location: `aiwg-research-gap`

This skill is best used when you want to check whether a research corpus is missing important areas of coverage. It is designed for gap analysis, not general search execution. It helps answer questions such as:

- What topics are underrepresented?
- What evidence is missing?
- Which areas need more literature before a project or framework is considered complete?

Typical use:

- evaluating a body of papers for blind spots
- identifying important gaps before launching a new study
- proposing targeted search queries to fill missing areas

### 2. Borghei Literature Review
Location: `borghei-litreview`

This is a structured, methodical literature-review workflow. It emphasizes reproducibility and research quality, including PRISMA-inspired review logic, inclusion criteria, source quality assessment, and synthesis into themes.

Typical use:

- building a systematic or scoping review
- screening sources by quality and relevance
- synthesizing a set of papers into themes and evidence summaries
- writing a literature review grounded in explicit criteria

This skill is especially useful when the goal is not just “find papers,” but “build a defensible review that is traceable and rigorous.”

### 3. Davila7 Literature Review
Location: `davila7-literature-review`

This skill is a practical academic workflow that combines database search, literature synthesis, citation verification, and output generation. It is designed for researchers who want a document pipeline that can produce a professional literature review with verified citations.

Typical use:

- comprehensive searches across scientific databases
- screening and aggregation of literature results
- generating review documents in markdown or PDF format
- verifying citations and maintaining reference quality

### 4. LTK Literature Review
Location: `ltk-literature-review`

This folder provides a compact, high-level guide to academic review work. It is useful as a starting point or a quick operational template for literature reviews and research synthesis.

Typical use:

- planning a review
- defining the question and scope
- identifying databases and search terms
- organizing findings into themes and synthesis sections

### 5. OpenClaw Literature Review
Location: `openclaw-literature-review`

This skill focuses on academic discovery through multiple search backends, including Semantic Scholar, OpenAlex, Crossref, and PubMed. It is strongly oriented toward literature discovery and result aggregation.

Typical use:

- finding papers on a topic across multiple research sources
- deduplicating results by DOI
- retrieving abstracts and metadata from multiple databases
- preparing candidate papers for a review or synthesis

### 6. MCP Market Literature Gap Rendered
Location: `mcpmarket-literature-gap-rendered`

This is a recovered, rendered representation of a literature-gap skill whose original source was no longer directly accessible. It documents the gap-identification playbook and is useful as a historical or secondary source when the original marketplace asset is unavailable.

Typical use:

- reviewing a gap-analysis framework
- understanding how research gaps are categorized and prioritized
- using the recovered documentation as a reference model for a custom gap-analysis process

## Quick selection guide

| If your goal is... | Best skill to start with |
|---|---|
| Identify missing knowledge in a field | `aiwg-research-gap` |
| Build a systematic review with clear methodology | `borghei-litreview` |
| Search, verify citations, and format a review | `davila7-literature-review` |
| Create a quick review plan or workflow | `ltk-literature-review` |
| Search many academic sources at once | `openclaw-literature-review` |
| Reference a recovered gap-analysis skill | `mcpmarket-literature-gap-rendered` |

## How to use this repository

1. Review the individual `SKILL.md` files before adopting a skill.
2. Choose the workflow that matches your research task.
3. Copy only the relevant folder into your local skills directory if you want to use it in a code assistant or research environment.
4. Keep this repository as a provenance and comparison archive rather than as an active runtime environment.
5. Prefer the skill that matches the problem:
   - gap detection for coverage analysis,
   - literature review for systematic synthesis,
   - multi-source search for discovery,
   - citation verification for writing quality.

## Provenance and sourcing

This repository includes original source references for the downloaded and recovered skill content:

| Folder | Source | Pinned version |
|---|---|---|
| `borghei-litreview` | `borghei/Claude-Skills`, `research/litreview` | `ddca910e95580c63a236303fc1534054f0f14d4c` |
| `davila7-literature-review` | `davila7/claude-code-templates`, `cli-tool/components/skills/scientific/literature-review` | `5ee4e51edbbc0bc4355f023e497d9efc1d6cc93d` |
| `aiwg-research-gap` | `jmagly/aiwg`, `agentic/code/frameworks/research-complete/skills/research-gap` | `f33d13476b9567299374d269b653dd56f444744c` |
| `ltk-literature-review` | `eyadsibai/ltk`, `plugins/ltk-product/skills/literature-review` | `f8e85697b95d8e4968cff3c49d20e632048faae9` |
| `openclaw-literature-review` | LobeHub package `openclaw-skills-literature-review` | `1.2.0` |

## Notes

This repo is best thought of as a research toolbox and a source archive. It is useful for understanding how different literature-related skills are designed, how they differ in emphasis, and which approach is most appropriate for a given academic workflow.

The material is intentionally kept in a reviewable form so that it can be inspected, adapted, and selectively installed rather than used blindly.
