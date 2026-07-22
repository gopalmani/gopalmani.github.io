# Deepak Dubey — Personal Portfolio

A lightweight engineering portfolio focused on backend systems, distributed pipelines, AI-powered developer tools, and production reliability.

Built as a small, dependency-free static site and designed for deployment through GitHub Pages.

**Live site:** [gopalmani.github.io](https://gopalmani.github.io/)

## Overview

The portfolio presents:

- Professional background and engineering interests
- Selected open-source projects
- Engineering focus areas
- Core technologies
- Engineering principles
- Contact and social links

The design follows a restrained editorial style with strong typography, subtle interaction states, and responsive layouts rather than a dashboard or résumé-template presentation.

## Technology

- Semantic HTML5
- Modern CSS
- [Inter](https://fonts.google.com/specimen/Inter) for body copy
- [Sora](https://fonts.google.com/specimen/Sora) for headings and labels
- No JavaScript framework
- No build process
- No runtime dependencies

## Project Structure

```text
.
├── .github/workflows/test.yml  # Pull request and push checks
├── tests/test_site.py          # Dependency-free website tests
├── index.html                  # Page content and semantic structure
├── style.css                   # Theme, layout, and interactions
├── favicon.svg                 # Browser icon source
├── CONTRIBUTING.md             # Contribution guidelines
└── LICENSE                     # MIT license
```

## Running Locally

The site can be opened directly from `index.html`. For a more representative local environment, serve the directory with any static HTTP server.

Using Python:

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000).

## Use This Website as a Template

You are welcome to reuse and customize this portfolio under the MIT License.

### GitHub template method

1. Open this repository on GitHub.
2. Select **Use this template → Create a new repository**. If the button is not
   visible, the repository owner must first enable **Template repository** under
   **Settings → General**.
3. Clone your new repository.
4. Replace Deepak's name, biography, projects, links, email address, and social
   profiles in `index.html`.
5. Update the colors and typography variables in `style.css`.
6. Replace the `D/` text and favicon files with your own branding.
7. Update this README and retain the original MIT license notice.
8. Enable GitHub Pages under **Settings → Pages**.

### Fork or clone method

Fork the repository on GitHub, or make a fresh local copy:

```bash
git clone https://github.com/gopalmani/gopalmani.github.io.git my-portfolio
cd my-portfolio
rm -rf .git
git init
```

The `rm -rf .git` command only removes the copied repository history; run it
inside the newly cloned `my-portfolio` directory.

## Testing

Run the same checks used for pushes and pull requests:

```bash
python3 -m unittest discover -s tests -v
```

The test suite validates key assets and metadata, internal anchors, local file
references, unique IDs, safe new-tab links, and balanced CSS braces. GitHub
Actions runs it automatically through `.github/workflows/test.yml`.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before
opening an issue or pull request.

Using Node.js:

```bash
npx serve .
```

## Design and Accessibility

The implementation includes:

- Responsive layouts for mobile, tablet, and desktop screens
- Fluid typography using `clamp()`
- Semantic landmarks and heading hierarchy
- A keyboard-accessible skip link
- Visible `:focus-visible` states
- Descriptive labels for external links
- Reduced-motion support
- Sufficient text contrast against the dark theme
- Secure external links using `rel="noopener noreferrer"`

## Customization

Most visual settings are defined as custom properties near the top of `style.css`:

```css
:root {
  --background: #0b0d10;
  --surface: #12161b;
  --surface-hover: #181d24;
  --text: #f4f6f8;
  --muted: #9da7b3;
  --border: rgba(255, 255, 255, 0.09);
  --accent: #8b9cff;
}
```

Portfolio copy, project information, and links can be edited directly in `index.html`.

## Deployment

This repository is compatible with GitHub Pages without compilation or additional configuration.

1. Push the site files to the repository's publishing branch.
2. Open **Settings → Pages** in GitHub.
3. Select **Deploy from a branch** as the source.
4. Choose the publishing branch and the repository root (`/`).

GitHub Pages will publish the site after the deployment workflow completes.

## Contact

- [GitHub](https://github.com/gopalmani)
- [LinkedIn](https://www.linkedin.com/in/gopal269/)
- [Blog](https://gopal-blog.github.io/)
- [X](https://x.com/deeep8o)
- [Email](mailto:gopalmanidubey@gmail.com)

## License

Licensed under the [MIT License](LICENSE). You may copy, modify, and distribute
the site while preserving the copyright and license notice.
