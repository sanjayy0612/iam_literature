# Research Skills Collection

This repository contains a curated set of research-oriented skills for literature review, evidence synthesis, and research-gap analysis. Each folder is a local copy of a community skill definition collected for review, comparison, and selective installation in Codex or Copilot workflows.

## Included skills

- `aiwg-research-gap` — identifies under-covered topics and recommends where additional literature is needed.
- `borghei-litreview` — systematic literature-review workflow with search strategy, screening, quality assessment, and synthesis.
- `davila7-literature-review` — database-oriented review process with citation verification and document generation.
- `ltk-literature-review` — concise review guide for planning, searching, and synthesizing academic evidence.
- `openclaw-literature-review` — multi-source literature discovery using Semantic Scholar, OpenAlex, Crossref, and PubMed.
- `mcpmarket-literature-gap-rendered` — recovered marketplace rendering of a literature-gap skill for reference and archival use.

## When to use each skill

| Goal | Recommended skill |
|---|---|
| Identify missing coverage in a research field | `aiwg-research-gap` |
| Build a rigorous review with explicit methods | `borghei-litreview` |
| Search, verify citations, and generate review output | `davila7-literature-review` |
| Start with a compact literature-review workflow | `ltk-literature-review` |
| Find papers across multiple academic sources | `openclaw-literature-review` |
| Reference a recovered gap-analysis description | `mcpmarket-literature-gap-rendered` |

## How to use this repository

1. Review the `SKILL.md` file for the skill you want to use.
2. Copy only the relevant folder into your local skills directory.
3. Restart Codex or Copilot so the skill is recognized.
4. Use the skill that matches your research task rather than installing the entire collection blindly.

This repo is intended as a reviewable archive and a selection tool, not as a single runtime package.

## Provenance

| Folder | Source | Pinned version |
|---|---|---|
| `borghei-litreview` | `borghei/Claude-Skills`, `research/litreview` | `ddca910e95580c63a236303fc1534054f0f14d4c` |
| `davila7-literature-review` | `davila7/claude-code-templates`, `cli-tool/components/skills/scientific/literature-review` | `5ee4e51edbbc0bc4355f023e497d9efc1d6cc93d` |
| `aiwg-research-gap` | `jmagly/aiwg`, `agentic/code/frameworks/research-complete/skills/research-gap` | `f33d13476b9567299374d269b653dd56f444744c` |
| `ltk-literature-review` | `eyadsibai/ltk`, `plugins/ltk-product/skills/literature-review` | `f8e85697b95d8e4968cff3c49d20e632048faae9` |
| `openclaw-literature-review` | LobeHub package `openclaw-skills-literature-review` | `1.2.0` |

## Notes

These skills are useful for systematic research work, literature synthesis, and evidence mapping. They should be reviewed before installation and adapted to your project context as needed.