# Starter Repository Template

This repository demonstrates a clean, modern GitHub project
structure with:

- A meaningful `README.md`
- Automated linting of Markdown and repository structure
- A documentation section following common best practices
- Example GitHub workflows
- A predictable, maintainable folder layout

Use this as a baseline for new projects or as a pattern for
internal tooling repositories.

---

## Features

### Documentation

- `/docs` folder with a navigation entry (`index.md`)
- Architecture notes
- Example ADRs for decision history

### Automation

- Markdown linting via GitHub Actions
- Repository validation for naming, required files, and
  conventions

## Automation Overview

This repository uses two complementary automation systems to
maintain quality, consistency, and structure:

- **GitHub Actions** - CI/CD, structural validation, and
  markdown linting. File: `.github/workflows/*.yml`. Runs on
  GitHub-hosted runners.

- **GitHub Agents** - AI-assisted content review and
  documentation suggestions. File: `.github/agents/*.agent.md`.
  Runs on the GitHub Agents runtime.

### Why Both?

- **GitHub Actions** provide deterministic, rule-based
  automation. Examples: linting, formatting, and structural
  validation.

- **GitHub Agents** provide intelligent automation that can
  interpret intent, suggest content improvements, and assist
  contributors.

Using both ensures the repository stays clean, consistent,
and aligned with modern best practices.

### Structure

- Source lives in `/src`
- GitHub workflows under `.github/workflows`
- `ISSUE_TEMPLATE` directory included

---

## Getting Started

Clone the repository:

```bash
git clone <your-repo-url>
cd <repo>
```

## License

This project is licensed under the Creative Commons
**Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**
license.

You are free to use, adapt, and share this material for
non-commercial purposes as long as attribution is provided.

See the [LICENSE](LICENSE) file for full details.
SPDX-License-Identifier: CC-BY-NC-4.0
