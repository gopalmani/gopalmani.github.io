# Deepak Dubey — Engineer & Product Builder

A product-led personal portfolio: **Dayframe, PsyPlay, KRIPA, and BrahminBooking**, followed by QueryMindAI and other work, skills, contributions, and contact details.

**Live:** [gopalmani.github.io](https://gopalmani.github.io/)

## Design & implementation

Semantic HTML, CSS, and a small vanilla-JavaScript clock. No framework, build step, package installation, or application backend. Geist and Instrument Serif are loaded from Google Fonts with system fallbacks.

The restrained olive/charcoal palette, editorial typography, and original animated SVG workspace share a visual direction with the [GitHub profile](https://github.com/gopalmani). The supplied desk GIF was a mood reference; its artwork is not redistributed.

The scene's clock reads the visitor's device clock, formats it in `Asia/Kolkata`, and refreshes every second while the tab is visible. It refreshes immediately when the tab becomes visible again. It does not claim server-synchronized time. With JavaScript disabled, it displays `IST`, never a fabricated time. Reduced-motion preferences disable decorative animations without freezing the actual clock.

GitHub README images cannot execute JavaScript and may be cached by GitHub. The profile therefore links an animated SVG preview to this live clock instead of displaying a stale time as current. No scheduled timestamp commits, image-generation service, or additional credentials are needed.

## Local preview

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Verification

```sh
python3 -m unittest discover -s tests -v
node --test tests/clock.test.cjs
```

Tests cover local assets, anchors, unique IDs, product links, metadata, accessibility hooks, valid SVG, clock timezone conversion across midnight, ticking, and hidden-tab recovery. CI runs the same checks. Before publishing, also inspect desktop/mobile layouts, keyboard focus, reduced motion, and the external activity image.

## Files

```text
index.html                    Product narrative and semantic page structure
style.css                     Responsive layout, typography, accessible states
site.js                       Live India-time clock
assets/studio.svg             Original, self-contained animated illustration
tests/test_site.py            Static content and asset checks
tests/clock.test.cjs           Dependency-free clock behavior tests
.github/workflows/test.yml    CI checks
```

## Content & external services

- Keep product claims grounded in implemented capabilities; do not invent adoption or performance figures.
- Dayframe's verified address is `https://dayframehq.github.io/`, not `dayframe.github.io`.
- GitHub activity is provided by OSS Insight and may lag; the image links to GitHub's current contribution view.
- Profile views remain on the GitHub profile via the existing Komarev provider.
- Google Fonts and OSS Insight receive normal browser requests. This portfolio adds no analytics, tracking scripts, cookies, contact-form backend, or stored visitor data.

## Publish

GitHub Pages publishes `main` from the repository root. Run checks before merging to `main`, then verify the Pages deployment and live site. Updating the separate `gopalmani/gopalmani` repository publishes the GitHub profile README automatically.

## Reuse

Reuse is welcome under the [MIT License](LICENSE). Replace names, product descriptions, contact details, external activity URLs, and favicon assets with your own. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance.
