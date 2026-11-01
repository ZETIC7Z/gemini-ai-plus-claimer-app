# AGENT.md — Project Blueprint & AI Context Handoff

> **For Future AI Agents & Developers**:  
> This file is the primary context and architectural blueprint for **ZETICUZ AI PLUS GEN** (`gemini-ai-plus-claimer-app`), engineered by **Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)**. Read this document first before writing code, modifying layout, updating links, or making releases.

---

## 1. 📌 Executive Summary & Project Purpose

- **Product Name**: ZETICUZ AI PLUS GEN
- **Type**: 3D interactive, accessible, zero-telemetry web hub, desktop generator & distribution portal
- **Developer**: **Sam Pangilinan** (`ZETICUZ` / `ZETIC7Z` / `TECHNOLOHIYA`)
- **Developer Portfolio**: [https://www.zeticuz.xyz/](https://www.zeticuz.xyz/)
- **Production URL**: [https://gemini-ai-plus-claimer.vercel.app](https://gemini-ai-plus-claimer.vercel.app/)
- **Repository (Public)**: [https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app](https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app)
- **Primary Brand Logo**: `images/ZE.svg` (copied from `C:\Users\ZETICUZ\Downloads\ZE.svg`)
- **Official Developer Signature Logo**: `images/zeticuz-logo.svg` (copied from `C:\Users\ZETICUZ\Downloads\zeticuz-logo.svg`)
- **Underlying Desktop Software**: A standalone, native Windows 10/11 (64-bit) portable application (`app/zeticuz_ai_plus_gen.py`) that automates promotional student onboarding and captures canonical official Google One offer links for 12 months of complimentary Gemini Advanced and 2TB cloud storage.

---

## 2. 🏗️ Tech Stack & Philosophy

| Layer                 | Technology                                             | Details                                                                                                                                                    |
| :-------------------- | :----------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **3D Motion Engine**  | Three.js (raw WebGL)                                   | High-performance 60fps 3D neural core, rotating dual orbital rings, ambient dust, mouse/touch parallax, and `prefers-reduced-motion` detection             |
| **Web Markup**        | HTML5 Semantic                                         | Strictly structured with ARIA landmarks, WCAG 2.1 AA compliance, zero broken tags                                                                          |
| **Styling**           | Tailwind CSS (CDN) + Custom CSS                        | Loaded via Tailwind CDN (`tailwind.config` in `<head>`), dark slate theme palette (`#090d16` base, `#0f172a` cards, `#0284c7` sky brand)                   |
| **Interactivity**     | Vanilla JavaScript (`js/app.js`)                       | Centralized `CONFIG` object, dynamic download routing, interactive desktop mockup simulation, mobile drawer, accessible clipboard copy                     |
| **Desktop App**       | Python (CustomTkinter / Tkinter)                       | `app/zeticuz_ai_plus_gen.py`: Standalone GUI with demographic randomization, Chromium browser detection cascade, interactive logs                          |
| **Compilation**       | PyInstaller (`scripts/build_exe.py`)                   | Bundles python app into standalone single-file portable Windows executable (`dist/Zeticuz AI Plus Gen.exe`)                                                |
| **CI/CD & Packaging** | GitHub Actions (`.github/workflows/build-release.yml`) | Automatically builds executable, compresses into `Zeticuz AI Plus Gen v1.0.1 by ZETICUZ.zip`, generates `SHA256SUMS.txt`, and publishes to GitHub Releases |
| **Fonts**             | Google Fonts                                           | `Inter` (UI typography) & `JetBrains Mono` (code, terminal, and spec readouts)                                                                             |
| **Code Formatter**    | Prettier                                               | Project-scoped `.prettierrc` (tabs, tabWidth: 2, printWidth: 100), `.vscode/settings.json` formatOnSave enabled                                            |
| **Hosting**           | Vercel                                                 | Plain HTML framework preset; automatic deploys triggered on `git push origin main`                                                                         |

---

## 3. 📂 Repository File Tree & Purpose

```
gemini-ai-plus-claimer-app/
├── .github/
│   └── workflows/
│       └── build-release.yml # Automated GitHub Actions release builder & packager
├── app/
│   ├── zeticuz_ai_plus_gen.py # Standalone Python desktop GUI application
│   └── requirements.txt      # Python dependencies (Playwright, PyInstaller, CustomTkinter)
├── scripts/
│   └── build_exe.py          # PyInstaller automated packaging script
├── build.bat                 # 1-click Windows compilation script
├── 404.html                  # Custom 404 error page (dual file:// and http/https routing)
├── index.html                # Core landing page with Three.js 3D motion & interactive simulator
├── robots.txt                # Crawler instructions referencing canonical sitemap
├── sitemap.xml               # XML sitemap with weekly frequency for search engines
├── site.webmanifest          # Progressive web app / mobile bookmark metadata
├── package.json              # NPM package file with build, format, and run commands
├── AGENT.md                  # Project blueprint and AI agent context handoff
├── README.md                 # User-facing repository overview, quickstart, and binary checksums
├── CHANGELOG.md              # Semantic Versioning change log (Keep a Changelog format)
├── .prettierrc               # Prettier formatting configuration
├── .prettierignore           # Prettier ignore patterns
├── .gitignore                # Git exclusion rules
├── .vscode/
│   ├── settings.json         # VS Code formatOnSave and default formatter setup
│   └── extensions.json       # Recommended VS Code extensions
├── css/
│   └── style.css             # Custom scrollbars, focus rings, reduced-motion overrides
├── js/
│   ├── app.js                # Client configuration, live mockup simulation, a11y announcer
│   └── three-hero.js         # Three.js 3D WebGL hero core and pointer parallax
└── images/
    ├── ZE.svg                # Official primary brand vector logo
    ├── zeticuz-logo.svg      # Official developer signature logo
    ├── app_icon.ico          # Multi-resolution Windows desktop icon (16x16 to 256x256)
    ├── app_icon.png          # High-resolution (512x512) master logo asset
    ├── og-image.png          # Official 1200x630 OpenGraph & Twitter preview banner
    ├── qrcode-bmc.png        # Buy Me a Coffee QR code
    └── qrcode-gcash.JPG      # GCash QR code
```

---

## 4. 🧭 Developer Attribution & Footer Standard

Per Sam Pangilinan's global instructions:

1. Centered at the bottom of the footer:
   - `[zeticuz-logo.svg] SITE DEVELOPED BY: Sam Pangilinan · © 2026`
   - Interactive button opening `https://www.zeticuz.xyz/` in a new tab without showing the raw URL string.
2. All prior third-party references have been completely purged and unified under `ZETICUZ` / `ZETIC7Z`.
3. All repository links route to `https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app`.

---

## 5. 🔗 Release & Direct Download Architecture

- **Release Tag URL**: `https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app/releases/tag/v1.0.1`
- **Direct Site Download**: `./downloads/Zeticuz AI Plus Gen.exe` (Bundled with Playwright & Chromium)
- **Portable Zip Bundle**: `./downloads/Zeticuz AI Plus Gen v1.0.1 by ZETICUZ.zip`
- **SHA-256 Checksum**: `7DA218B03C277D45CF7D5F72F0C6856CEADA229655080C0999A3DE1065570A29`
- **Brand Asset Architecture**:
  - Website App Logo & Desktop App Icon: `images/zeticuz_app_icon.png` (3rd image squircle monogram) & `images/app_icon.ico`
  - Desktop Application Header Banner: `images/zeticuz_header_logo.png` (2nd image 3D metallic red "ZE" monogram with crisp white bold uppercase "ZETICUZ")
  - Official Developer Signature: `images/zeticuz-logo.svg` + centered footer signature linked to `https://www.zeticuz.xyz/`
- **Centralized Configuration in `js/app.js`**:
  ```javascript
  const CONFIG = {
  	APP_NAME: "ZETICUZ AI PLUS GEN",
  	VERSION: "v1.0.1",
  	REPO_URL: "https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app",
  	DEV_NAME: "Sam Pangilinan",
  	PORTFOLIO_URL: "https://www.zeticuz.xyz/",
  	DIRECT_DOWNLOAD_URL: "./downloads/Zeticuz AI Plus Gen.exe",
  };
  ```

---

## 6. 🛠️ Instructions for Future AI Agents

1. **Prettier Formatting is Mandatory**: Always run Prettier before committing:
   ```bash
   npx prettier --write .
   ```
2. **Preserve Semantic HTML & ARIA**:
   Never add an `<svg>` without `aria-hidden="true" focusable="false"`. Ensure all interactive buttons have explicit `type="button"` and labels.
3. **Preserve Underlying Engine & Config**:
   The Playwright claimer pipeline and account activation flow (`claimer.pyc`, `constants.pyc`, and queue listeners) are 100% verified and activated. Never alter the underlying parameters.
4. **Verify in Real Browser & Desktop**:
   Always verify locally via Playwright / Chrome DevTools and desktop process execution before claiming completion.
