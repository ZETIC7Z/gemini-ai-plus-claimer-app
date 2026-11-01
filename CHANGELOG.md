# Changelog

All notable changes to **ZETICUZ AI PLUS GEN** landing page, 3D motion engine, and desktop distribution package are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.1-ZET] - 2026-11-01

### Rebranded & Enhanced by Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)

- **Complete Brand Transformation**:
  - Rebranded the portal to **ZETICUZ AI PLUS GEN** across all metadata, markup, schema, and documentation.
  - Integrated primary brand logo `ZE.svg` into navigation bar and preview headers.
  - Implemented Sam Pangilinan's official developer signature standard in the footer (`zeticuz-logo.svg` + interactive portfolio button to `https://www.zeticuz.xyz/`).
  - Purged all previous owner references and linked repository to [ZETIC7Z/gemini-ai-plus-claimer-app](https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app).
- **Interactive 3D WebGL Motion Engine (`js/three-hero.js`)**:
  - Implemented a real-time Three.js 60fps 3D neural core in the hero section.
  - Features geometric crystal core, counter-rotating orbital token rings, ambient particle field, and smooth damped pointer parallax.
  - Built-in accessibility support for `prefers-reduced-motion` and viewport visibility culling via `IntersectionObserver`.
- **Standalone Desktop Application (`app/zeticuz_ai_plus_gen.py`)**:
  - Created native desktop GUI application matching the portal's dark slate palette.
  - Integrated candidate profile setup, 1-click demographic randomizer, browser cascade detection, live terminal readout, and canonical link generation.
- **Automated GitHub Actions Release Pipeline (`.github/workflows/build-release.yml`)**:
  - Automatically compiles standalone Windows binary via PyInstaller upon release tags or dispatch.
  - Bundles into `Zeticuz AI Plus Gen v1.0.1 by ZETICUZ.zip`, generates `SHA256SUMS.txt`, and publishes to GitHub Releases.
- **Interactive Web Mockup Simulation**:
  - Connected "Randomize Info" and "Get 1-Year Access Link" buttons in the homepage mockup to an interactive simulator with live terminal logs and stepper state transitions.

---

## [1.0.1] - 2026-10-31

### Added

- **Universal Multi-Browser Discovery Cascade**:
  - Compatibility with Microsoft Edge, Google Chrome, Brave Browser, Opera, and Vivaldi.
  - Zero-bloat architecture attaching directly to host browser binaries.
- **Centralized Version & Download Infrastructure**:
  - Single-source-of-truth configuration in `js/app.js` (`CONFIG.VERSION = "v1.0.1"`).
  - Centralized version indicators and resilient fallback links.
- **Custom 404 Error Page (`404.html`)**:
  - Dual-environment `<base>` URL resolution for root Vercel deployments and offline `file://` testing.
  - Unified header navigation and legal footer.
