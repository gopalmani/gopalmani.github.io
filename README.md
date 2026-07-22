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
├── index.html    # Page content and semantic structure
├── style.css     # Theme, layout, responsive styles, and interactions
└── README.md     # Project documentation
```

## Running Locally

The site can be opened directly from `index.html`. For a more representative local environment, serve the directory with any static HTTP server.

Using Python:

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000).

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
