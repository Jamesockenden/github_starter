---
title: GitHub Agents
---

# 🤖 GitHub Agents (metadata)

This repository includes example "GitHub Agent" metadata files in `.github/agents/`. These are small, human-readable Markdown files (commonly named `*.agent.md`) that describe automated helpers, examples, or agent-like behaviours used by contributors or tooling.

This short guide explains what they are, how they are organized, and how you can extend them safely.

## What are Agent files?

- Agent files are documentation/metadata files — they do not execute automatically. They describe an automation idea, suggested prompts, examples, or configuration that contributors can use or extend.
- Location: `.github/agents/`
- File format: Markdown (`.md`) using a simple structure: title, short description, and sections such as `Usage`, `Examples`, and `Extending`.

## Why we keep them

- Shareable knowledge: Capture reusable prompts, automation patterns, or deployment notes.
- Onboarding: Help new contributors understand what automations exist and how to use them.
- Reviewable: Keep automation intent in source control so changes are reviewed via PRs.

## Typical structure

Use a clear structure so both humans and tools can read the file. Example:

```markdown
# Agent name — short description

## Purpose
Explain what the agent is for and when to use it.

## Usage
Provide examples, command-line snippets, or prompts.

## Examples
Show example inputs and outputs.

## Extending
How contributors can add variants, new prompts, or update metadata.
```

## How to extend or add an agent

1. Fork or branch the repo.
2. Create a new file in `.github/agents/` named something-descriptive.agent.md.
3. Follow the structure above and be concise. Include examples and expected behavior.
4. Run the Markdown linter locally: `npx -y markdownlint-cli2 "**/*.md"`.
5. Open a PR describing the change and request a review.

## Testing and validation

- There is no runtime engine for these files in this repo — they are metadata. To validate:
  - Run `npx -y markdownlint-cli2 "**/*.md"` to ensure formatting is lint-clean.
  - Preview docs with MkDocs (`mkdocs serve`) to check rendering under `docs/`.

## Best practices

- Be explicit about inputs/outputs and any assumptions (secrets, tokens).
- Avoid embedding secrets or credentials in agent files.
- Keep examples small and focused so reviewers can understand changes quickly.

## Example (minimal)

```markdown
# label-suggest.agent.md — Suggest labels for issues

## Purpose
Given an issue title + body, suggest 1–3 repository labels.

## Usage
Prompt example and expected output.

## Extending
Add language/localization examples or rules for label precedence.
```

---

If you'd like, I can add a simple validator script or a template `agent` file to help contributors add new agents consistently.
