# ZETICUZ AI PLUS GEN — Official Web Hub & Distribution Portal

[![Platform: Windows 10 / 11](<https://img.shields.io/badge/platform-Windows%2010%20%2F%2011%20(64--bit)-0284c7?style=flat-square&logo=windows>)](https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app/releases)
[![Version: v1.0.1](https://img.shields.io/badge/release-v1.0.1-38bdf8?style=flat-square&logo=github)](https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app/releases/tag/v1.0.1)
[![Developer: Sam Pangilinan](https://img.shields.io/badge/developer-Sam%20Pangilinan-10b981?style=flat-square)](https://www.zeticuz.xyz/)
[![Telemetry: Zero](<https://img.shields.io/badge/telemetry-Zero%20(100%25%20Local)-10b981?style=flat-square>)](#-privacy--local-execution)

Official web hub, 3D interactive portal, and release distribution platform for **ZETICUZ AI PLUS GEN** — an independent, lightweight, zero-telemetry Windows desktop utility engineered by **Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)** to automate promotional student onboarding and capture canonical official Google One offer links for 12 months of complimentary Gemini Advanced and 2TB cloud storage.

🌐 **Live Web Hub**: [https://gemini-ai-plus-claimer.vercel.app](https://gemini-ai-plus-claimer.vercel.app/)  
📦 **Official Release (v1.0.1)**: [https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app/releases/tag/v1.0.1](https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app/releases/tag/v1.0.1)  
👨‍💻 **Developer Portfolio**: [https://www.zeticuz.xyz/](https://www.zeticuz.xyz/)

---

## 📁 Repository Structure

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
├── 404.html                  # Custom, restrained 404 error page matching homepage UI
├── index.html                # Semantic, accessible landing page with Three.js 3D motion
├── robots.txt                # Search engine crawler directives & sitemap reference
├── sitemap.xml               # XML sitemap for SEO discovery
├── site.webmanifest          # Web app manifest for installable/bookmark metadata
├── README.md                 # Project documentation and deployment guide
├── CHANGELOG.md              # Comprehensive version history & release changelog
├── package.json              # NPM package file with build & format commands
├── css/
│   └── style.css             # Custom scrollbars, focus rings & prefers-reduced-motion
├── js/
│   ├── app.js                # Centralized CONFIG, interactive simulator & a11y announcer
│   └── three-hero.js         # Three.js 60fps 3D neural core & orbital motion system
└── images/
    ├── ZE.svg                # Official primary brand vector logo
    ├── zeticuz-logo.svg      # Official developer signature logo
    ├── app_icon.ico          # Multi-resolution Windows application icon
    ├── app_icon.png          # High-resolution brand icon (512x512)
    └── og-image.png          # Official 1200x630 OpenGraph & Twitter preview banner
```

---

## ⚡ Key Features

### 1. Three.js 3D WebGL Hero Motion System

- **Interactive 3D Neural Core**: Real-time WebGL rendering of a futuristic geometric AI crystal surrounded by counter-rotating particle rings and cyber dust.
- **Pointer Parallax & Damped Physics**: Responds dynamically to mouse and touch coordinates with buttery 60fps interpolation.
- **Accessibility & Battery Aware**: Automatically honors `prefers-reduced-motion` and pauses rendering via `IntersectionObserver` when scrolled out of view.

### 2. Standalone Windows Desktop Application (`app/zeticuz_ai_plus_gen.py`)

- **Native GUI Execution**: Styled in modern dark slate palette (`#090d16` base, `#0f172a` container, `#0284c7` buttons).
- **Universal Multi-Browser Cascade**: Auto-detects and binds to pre-installed Google Chrome, Microsoft Edge, Brave, and Opera on Windows.
- **Profile Randomizer**: 1-click demographic generation for realistic candidate details.
- **Human-in-the-Loop Dialog**: Prompts cleanly for confirmation codes only when required.
- **Direct Local Archive**: Saves resolved redemption links locally to `results/zeticuz_google_one_links.txt`.

### 3. Automated GitHub Actions Package Pipeline

- When you fork or tag (`v*`) this repository, `.github/workflows/build-release.yml` automatically builds the Windows binary, compresses it into `Zeticuz AI Plus Gen v1.0.1 by ZETICUZ.zip`, generates `SHA256SUMS.txt`, and publishes a GitHub Release.

### 4. Accessibility (WCAG 2.1 AA Compliance)

- **Skip Navigation Link (2.4.1)**: Screen-reader keyboard bypass link at top of `<body>`.
- **Screen Reader Announcer (4.1.3)**: Live polite ARIA regions announcing clipboard and generation updates.
- **High-Contrast Palette (1.4.3)**: Typography exceeds 7:1 contrast ratios on dark slate backgrounds.

---

## 🚀 Running & Packaging Locally

### Run the Web Hub Locally:

```bash
python -m http.server 3000
# Open http://localhost:3000 in your browser
```

### Run the Desktop App:

```bash
python app/zeticuz_ai_plus_gen.py
```

### Build the Standalone Windows `.exe`:

```bash
# Double click build.bat or run:
python -m pip install -r app/requirements.txt
python scripts/build_exe.py
# The output binary is created at dist/Zeticuz AI Plus Gen.exe
```

---

## 📦 Release Package Details (v1.0.1)

| Attribute              | Specification                                                      |
| :--------------------- | :----------------------------------------------------------------- |
| **Release Version**    | `v1.0.1` (Stable)                                                  |
| **Release Archive**    | `Zeticuz AI Plus Gen v1.0.1 by ZETICUZ.zip` (9.8 MB)               |
| **Application Binary** | `Zeticuz AI Plus Gen.exe` (10.1 MB)                                |
| **Direct Site Path**   | `downloads/Zeticuz AI Plus Gen.exe`                                |
| **SHA-256 Checksum**   | `1D25E74C5A372504F70A6777022ED53D1F61756C9DA7B1E3DC89B5535E2E0AC1` |
| **Target OS**          | Windows 10 / Windows 11 (64-bit)                                   |
| **Developer**          | Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)                            |
| **Package Type**       | Single portable binary (Zero installation needed)                  |

### Checksum Verification in PowerShell:

```powershell
Get-FileHash "downloads\Zeticuz AI Plus Gen.exe" -Algorithm SHA256
```

---

## 👨‍💻 Developer Attribution & Standard Signature

Developed by **Sam Pangilinan** (`ZETICUZ` / `ZETIC7Z` / `TECHNOLOHIYA`).  
Explore developer projects, full-stack systems, and 3D WebGL builds at:  
👉 **[https://www.zeticuz.xyz/](https://www.zeticuz.xyz/)**

---

## ⚖️ Disclaimer & Non-Affiliation

This project is an independent desktop utility provided strictly for convenience, personal educational testing, and research. This project is **not** affiliated with, sponsored by, or endorsed by Google LLC, Alphabet Inc., or Internshala. Google, Google One, and Gemini are trademarks of Google LLC.
