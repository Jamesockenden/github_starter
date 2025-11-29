# Summary

Describe the purpose of this pull request and the high-level
changes it contains.

---

## Type of change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation change
- [ ] Chore / Maintenance

---

## Checklist

- [ ] I have read the contribution guidelines in `CONTRIBUTING.md`.
- [ ] Code changes are linted and formatted.
- [ ] All new and existing tests pass locally.
- [ ] I have added or updated documentation where required.
- [ ] I have updated `README.md` or `docs/` if behaviour changed.

---

## Linting / Validation

Please confirm the following were run and pass locally (or in CI):

- `npx -y markdownlint-cli2 "**/*.md"` (Markdown lint)
- Project tests (e.g., `npm test`, `pytest`, etc.)

If this PR involves repository structure or missing files, run:

- Request the structure validator agent with a comment: `/validate-structure`

---

## Testing instructions

Provide clear steps to reproduce or test the changes locally.

Example:

```powershell
git fetch origin
git checkout -b my-branch
# make changes
npx -y markdownlint-cli2 "**/*.md"
npm test
```

---

## Related issues

Link any related issues, e.g., `Fixes #123`.

---

## Additional notes for reviewers

Anything the reviewer should know (design notes, potential
side-effects, reasons for approach).
