# Usage

This document shows basic commands contributors can run locally
to lint Markdown, run project tests (if present), and work with
repository agents. Commands are written for PowerShell on Windows.

## Linting Markdown

Use `markdownlint-cli2` (recommended via `npx`) to lint all
Markdown files in the repository without installing globally:

```powershell
npx -y markdownlint-cli2 "**/*.md"
```

If you prefer a global install:

```powershell
# Install globally (one-time)
npm install -g markdownlint-cli2

# Run
markdownlint-cli2 "**/*.md"
```

Typical issues the linter reports: missing blank lines around
headings, list spacing, code-fence languages, and line-length
violations. Fix the files and re-run the linter until it reports
no errors.

## Running Tests

This template does not include a specific test framework by
default. Use the commands appropriate for your project stack.

Node / JavaScript (if `package.json` exists):

```powershell
# install deps
npm install

# run the test script (expects a `test` script in package.json)
npm test
```

Python (if the project uses Python):

```powershell
# create virtual env and activate
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install test deps
pip install -r requirements.txt

# run pytest
pytest
```

If your repo uses another language or framework, run the
corresponding test command (e.g., `mvn test`, `gradle test`,
`dotnet test`, etc.).

## Working with Agents Locally

This repository contains an agent metadata file under
`.github/agents/` that describes an AI-assisted Markdown review
agent. GitHub Agents run in GitHub's Agents runtime and are not
directly executable locally.

Local development options:

- Use the metadata in `.github/agents/*.agent.md` as the spec
    for building local automation scripts or small helper tools.
- To manually run checks locally, use `markdownlint-cli2` as
    shown above and implement any additional checks as scripts.
- If you run an LLM or agent framework locally, you can write a
    small script that reads the agent metadata and performs the
    same actions (read files, suggest fixes). This is advanced
    and depends on the tooling you choose.

## Continuous Integration

This template includes GitHub Actions workflows (see
`.github/workflows/`) to run markdown linting and repository
validation on push and pull requests. If you want to run the
same workflows locally, consider using `act` (third-party) to
simulate GitHub Actions:

```powershell
# Install act and run a specific workflow (example)
# See https://github.com/nektos/act for usage and installation
act -j lint-markdown
```

Note: `act` uses Docker and requires extra setup; it is not an
official GitHub tool.

## Troubleshooting

- If `npx` fails, ensure you have Node.js and npm installed.
- If `pytest` or other test commands fail, make sure dev
    dependencies are installed and environment variables are set.
- For agent simulation, be explicit about which inputs and files
    the agent should read so results are reproducible.

## Want a PR?

specific instructions (Node, Python, Go, etc.). Tell me which
If you'd like I can open a PR that adds more detailed, stack-
specific instructions (Node, Python, Go, etc.). Tell me which
stacks you want and I will add tailored commands.
