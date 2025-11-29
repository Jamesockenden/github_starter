# 🚀 GitHub Starter Template

![Repo stars](https://img.shields.io/github/stars/Jamesockenden/github_starter?style=flat-square)
![Repo issues](https://img.shields.io/github/issues/Jamesockenden/github_starter?style=flat-square)
![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey?style=flat-square)
![Docs build](https://github.com/Jamesockenden/github_starter/actions/workflows/docs-build.yml/badge.svg)
![Markdown lint](https://github.com/Jamesockenden/github_starter/actions/workflows/lint-markdown.yml/badge.svg)

A lightweight, practical starter repository that helps you bootstrap
new GitHub projects quickly and consistently.

<!-- TOC -->
## 📑 Table of contents

- [What you'll find](#-what-youll-find)
- [Quick start](#-quick-start)
- [Features](#-features)
- [Repository structure](#-repository-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 📚 What you'll find

- 🧰 Scripts to automate repository creation (`scripts/create_repo.py`)
- 🍪 Cookiecutter template under `cookiecutter/` to generate projects
- ⚙️ GitHub Actions workflows under `.github/workflows/`
- 🤖 Starter GitHub Agents metadata under `.github/agents/`
- 📄 Example docs under `docs/`

## ✨ Quick start

1. On GitHub, click **Use this template → Create a new repository**.
2. (Optional) Install Python deps locally:

```bash
pip install -r requirements.txt
```

3. Generate a new project with Cookiecutter (if used):

```bash
cookiecutter cookiecutter/
```

4. (Optional) Create a GitHub repo automatically from this machine:

```bash
python scripts/create_repo.py --name my-new-project \
  --private --description "My project bootstrapped from github_starter"
```

Quick usage example (create a project and install deps):

```bash
cookiecutter cookiecutter/ my-new-project
cd my-new-project
pip install -r requirements.txt
```

## 🧩 Features

- ⚙️ Repo creation script — create repos via the GitHub API.
- 🧩 Cookiecutter template — generate consistent project scaffolds.
- 🔁 CI ready — example GitHub Actions for docs and validation.
- 📚 Docs scaffolded — use `docs/` and MkDocs to publish docs.

## 📁 Repository structure

```text
github_starter/
├─ scripts/
│  └─ create_repo.py
├─ cookiecutter/
│  └─ {{cookiecutter.project_slug}}/
├─ .github/
│  ├─ workflows/
│  └─ agents/
├─ docs/
├─ src/
├─ README.md
├─ LICENSE
└─ requirements.txt
```

## 🤝 Contributing

Contributions are welcome — fork, create a branch, and open a PR. Run
the Markdown linter before opening a PR:

```powershell
npx -y markdownlint-cli2 "**/*.md"
```

## 📜 License

This project is licensed under the Creative Commons Attribution-
NonCommercial 4.0 International (CC BY-NC 4.0). See the `LICENSE`
file for full terms.

---
