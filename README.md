# GitHub Starter Template

A lightweight, practical starter repository with templates and helpers
for bootstrapping new projects on GitHub.

## Features

- A project bootstrap script for quickly creating new GitHub
  repositories.
- A Cookiecutter template for generating consistent project skeletons.
- Built-in GitHub Actions for CI/CD automation.
- Starter GitHub Agents metadata for automation tasks.

## Quick start

1. Use this repository as a template on GitHub (Use this template).
1. Install project dependencies (if used):

```bash
pip install -r requirements.txt
```

1. Generate a new project using Cookiecutter (if present):

```bash
cookiecutter cookiecutter/
```

1. (Optional) Create a GitHub repo automatically:

```bash
python scripts/create_repo.py --name my-new-project \
  --private --description "My project bootstrapped from github_starter"
```

## Usage

Workflows live under `.github/workflows/`. Edit or remove them to
match your project's needs.

Agent metadata files are under `.github/agents/`. These are specs for
GitHub Agents and may be used as references for automation.

## Repository structure

```text
github_starter/
 scripts/
   create_repo.py
 .github/
   workflows/
   agents/
 docs/
 src/
 README.md
 LICENSE
 requirements.txt
```

## Contributing

Contributions are welcome. Typical workflow:

1. Fork the repository.
1. Create a feature branch.
1. Commit and push your changes.
1. Open a pull request.

Please keep changes aligned with the template's goals: simple and
reusable project bootstrapping.

## License

This project is licensed under the MIT License. See the `LICENSE`
file for details.

## Notes

- This repository is a starting point. Adapt workflows, tooling, and
  agent metadata to suit your stack and policies.
