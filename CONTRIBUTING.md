# Contributing

Thanks for helping improve this portfolio. Small fixes, accessibility
improvements, documentation updates, and focused design refinements are
welcome.

## Before opening a pull request

1. Fork the repository and create a branch from `main`.
2. Keep changes focused on one concern.
3. Preview the site at desktop and mobile widths.
4. Run the automated checks:

   ```bash
   python3 -m unittest discover -s tests -v
   ```

5. Explain what changed and include screenshots for visual updates.

## Local preview

Start a static server from the repository root:

```bash
python3 -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000).

## Pull request guidelines

- Preserve semantic HTML and keyboard accessibility.
- Keep the project dependency-free unless a dependency has a clear benefit.
- Do not commit personal secrets, analytics keys, or private contact details.
- Update documentation when behavior or project structure changes.

By contributing, you agree that your contribution is licensed under the
repository's [MIT License](LICENSE).
