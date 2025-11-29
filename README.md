# Starter Repository Template

![GitHub Workflow](https://github.com/Jamesockenden/github_starter/actions/workflows/lint-markdown.yml/badge.svg)
![License](https://img.shields.io/badge/license-CC--BY--NC%204.0-blue)

Clean, lightweight GitHub repository template for internal and
open-source projects. Use this to kickstart new repos with a
consistent layout and basic automation.

---

## Table of contents

- [Features](#features)
- [Automation Overview](#automation-overview)
- [Quick Start](#quick-start)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### 📘 Documentation

- `/docs` with an `index.md` navigation entry
- Architecture notes and example ADRs for decisions

### 🤖 Automation

- Markdown linting via GitHub Actions
- Repository validation for naming, required files, and
  conventions

## Automation Overview

This repository uses two automation approaches to maintain
quality and consistency:

- **GitHub Actions** — CI and repo validation. File:
  `.github/workflows/*.yml`.
- **GitHub Agents** — AI-assisted content reviews and
  suggestions. File: `.github/agents/*.agent.md`.

## Quick Start

Clone the template and begin:

```bash
git clone <your-repo-url>
cd <repo>
```

Start by editing `README.md` and `docs/index.md` to fit your
project. Add code under `src/` and update or add workflows in
`.github/workflows/` as needed.

### Git ignore

Include a `.gitignore` in your project root to exclude generated
files, OS artifacts, temporary editor files, and build outputs.
Common entries:

```gitignore
# Node
node_modules/

# Python
__pycache__/
*.py[cod]

# OS
.DS_Store
Thumbs.db

# Editor
.vscode/
*.sublime-workspace
```

Adjust entries to match your project's languages and tools.

## Contributing

See `CONTRIBUTING.md` for guidance on repository standards,
linting and PR workflows.

## License

This project is licensed under the Creative Commons
Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
See the `LICENSE` file for details.

SPDX-License-Identifier: CC-BY-NC-4.0
