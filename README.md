# 🚀 GitHub Starter Template

![Repo stars](https://img.shields.io/github/stars/Jamesockenden/github_starter?style=flat-square)
![Repo issues](https://img.shields.io/github/issues/Jamesockenden/github_starter?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)
![Docs build](https://github.com/Jamesockenden/github_starter/actions/workflows/docs-build.yml/badge.svg)
![Markdown lint](https://github.com/Jamesockenden/github_starter/actions/workflows/lint-markdown.yml/badge.svg)

A lightweight, practical starter repository that helps you bootstrap new
GitHub projects quickly and consistently.

<!-- TOC -->
## 📑 Table of contents

- [What you'll find](#-what-youll-find)
- [Quick start](#-quick-start)
- [Features](#-features)
- [Repository structure](#-repository-structure)
- [Contributing](#-contributing)
- [License](#-license)

## 📚 What you'll find

- 📘 Documentation built with MkDocs — see `mkdocs.yml` and the
	`docs/` folder. The docs use `mkdocs-material` by default for a clean
	site theme and built-in search.
- 🍪 Cookiecutter template under `cookiecutter/` to generate projects
	quickly and consistently.
- ⚙️ GitHub Actions workflows under `.github/workflows/` for validation
	and docs builds.
- 🤖 Starter GitHub Agents metadata under `.github/agents/` (examples to
	get started). See `docs/agents.md` for details on how to use and
	extend them.

## ✨ Quick start

- On GitHub, click **Use this template → Create a new repository**.

- (Optional) Install Python deps locally:

```bash
pip install -r requirements.txt
```

Quick usage example (generate docs locally and preview):

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

Quick example to generate a project from the template:

```bash
cookiecutter cookiecutter/
```

## 🧩 Features

- 📘 MkDocs documentation — `docs/` + `mkdocs.yml` provide the documentation source and site configuration.
- 🧩 Cookiecutter template — generate consistent project scaffolds.
- 🔁 CI ready — example GitHub Actions for docs and validation.
- 📚 Docs scaffolded — use `docs/` and MkDocs to publish docs.

## 📁 Repository structure

```text
github_starter/
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

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

## 🙌 Credits

Created and maintained by **James Ockenden**.  
Contributions are welcome — please open a pull request or issue if you’d like to help improve the project.  
If you use this project, please provide attribution by linking back to the repository or mentioning the author.
