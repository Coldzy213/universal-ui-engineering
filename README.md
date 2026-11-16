# Universal UI Engineering — Codex Skill

**Install once. Use in any project. Build consistent, responsive, accessible interfaces.**

Universal UI Engineering is a reusable [Codex Agent Skill](https://learn.chatgpt.com/docs/build-skills) for designing, implementing, reviewing, and improving user interfaces. It supplies practical UI/UX standards for typography, spacing, cards, forms, navigation, responsive layouts, accessibility, and frontend quality assurance.

It can guide work on **web, iOS, Android, tablet, and desktop** applications, adapting to each platform's conventions rather than imposing identical dimensions everywhere.

> **Start here:** This README is an **installation and usage guide for developers**. You do not need to copy the large standards document into each project: install the skill, open your app in Codex, and invoke `$universal-ui-engineering`.

## Contents

1. [Requirements](#1-requirements)
2. [Install globally — use in every project](#2-install-globally--use-in-every-project)
3. [Install in one project — share with your team](#3-install-in-one-project--share-with-your-team)
4. [Verify and activate the skill](#4-verify-and-activate-the-skill)
5. [Use it in your application](#5-use-it-in-your-application)
6. [Ready-to-copy Codex prompts](#6-ready-to-copy-codex-prompts)
7. [Optional project-wide instructions](#7-optional-project-wide-instructions)
8. [Update or remove the skill](#8-update-or-remove-the-skill)
9. [Troubleshooting](#9-troubleshooting)
10. [Files, standards, and references](#10-files-standards-and-references)

---

## 1. Requirements

- **Codex** in VS Code or Codex CLI, installed and signed in.
- **Git** installed if using the recommended Git installation commands. Check with `git --version`.
- An existing application or a new project to work on.
- Access to this repository. **Replace `YOUR_USERNAME` below with the account that published this skill on GitHub.**

You do **not** need to install React, Tailwind, Flutter, or any other framework solely to use this skill. It provides instructions and references, not a required UI runtime.

### Choose where to install

| Your goal | Install the folder here | Result |
| --- | --- | --- |
| Use in **all your projects** | `~/.agents/skills/universal-ui-engineering/` | Recommended for individual developers |
| Use in **just one Git repository** | `<project-root>/.agents/skills/universal-ui-engineering/` | Recommended for shared team standards |

**Important:** The `SKILL.md` file must be directly inside the `universal-ui-engineering` folder. Do not place an extra nested folder between them.

## 2. Install globally — use in every project

This is the **recommended** choice when you use Codex for multiple applications.

<details>
<summary><strong>Windows (PowerShell)</strong></summary>

Open PowerShell (or the VS Code terminal) and run:

```powershell
# Create the user-wide skill directory.
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null

# Download the complete skill from GitHub.
git clone https://github.com/YOUR_USERNAME/universal-ui-engineering.git `
  "$HOME\.agents\skills\universal-ui-engineering"

# Verify that Codex can find the skill manifest.
Test-Path "$HOME\.agents\skills\universal-ui-engineering\SKILL.md"
```

Expected output for the last command: `True`.

**Example destination:** `C:\Users\YourWindowsUser\.agents\skills\universal-ui-engineering\SKILL.md`

</details>

<details>
<summary><strong>macOS / Linux (Terminal)</strong></summary>

```bash
mkdir -p "$HOME/.agents/skills"

git clone https://github.com/YOUR_USERNAME/universal-ui-engineering.git \
  "$HOME/.agents/skills/universal-ui-engineering"

test -f "$HOME/.agents/skills/universal-ui-engineering/SKILL.md" && echo 'Skill installed'
```

Expected output: `Skill installed`.

</details>

Once installed, proceed to [Verify and activate](#4-verify-and-activate-the-skill). You only need to install it **once per computer/user account**, not separately for each application.

### Alternative: install using Codex itself

In Codex, ask the built-in skill installer:

```text
$skill-installer
Install the universal-ui-engineering skill from
https://github.com/YOUR_USERNAME/universal-ui-engineering
```

This option depends on the skill installer being available and able to access the repository. Manual Git installation above is a predictable alternative.

## 3. Install in one project — share with your team

Choose this option when you want contributors to the **same application** to use the same version of the UI standards.

### Option A: Git submodule (recommended for a Git-managed project)

Open a terminal at your application's **repository root** (where its `.git` directory is), then run:

```powershell
git submodule add https://github.com/YOUR_USERNAME/universal-ui-engineering.git .agents/skills/universal-ui-engineering

git add .gitmodules .agents/skills/universal-ui-engineering
git commit -m "Add Universal UI Engineering Codex skill"
```

Your application repository will contain a reference to the skill repository. When colleagues clone the application, they can fetch the skill with:

```bash
git submodule update --init --recursive
```

They can also clone the application and its submodules in one step:

```bash
git clone --recurse-submodules https://github.com/YOUR_ORG/YOUR_APP.git
```

### Option B: copy the folder (no submodule)

1. On this GitHub page, select **Code → Download ZIP**.
2. Extract the archive.
3. Copy the whole `universal-ui-engineering` folder to `<your-project>/.agents/skills/`.
4. Check that `<your-project>/.agents/skills/universal-ui-engineering/SKILL.md` exists.
5. If the folder came from a Git clone, **do not copy its inner `.git` directory** into your application repository.
6. Commit the copied skill files if you want your teammates to receive them automatically.

Example application layout:

```text
my-application/
├── .agents/
│   └── skills/
│       └── universal-ui-engineering/
│           ├── SKILL.md
│           ├── references/
│           ├── assets/
│           └── scripts/
├── src/                 # Or app/, pages/, resources/, lib/, etc.
├── package.json         # Or composer.json, pubspec.yaml, etc.
└── ...
```

**Tip:** A global installation is simpler for solo developers. A project-level installation makes the standards visible and versioned with the application. Avoid installing duplicate versions at both locations unless you intentionally need them.

## 4. Verify and activate the skill

1. **Open your actual application folder** in VS Code or launch Codex CLI from that folder.
2. Open a new Codex conversation. If the installation does not show up, **restart Codex**.
3. Type `/skills` to browse available skills, or type `$` and select `universal-ui-engineering`.
4. Include the skill at the beginning of your prompt:

```text
$universal-ui-engineering
Inspect this project's frontend and identify the highest-impact
UI/UX, accessibility, and responsive layout problems.
Audit only for now; do not edit code.
```

The skill can sometimes be selected automatically for matching frontend tasks, but **explicit invocation is the most predictable way** to request it.

**How to confirm it is working:** Ask Codex which skill it is using, request a UI audit, and look for a plan grounded in your actual codebase, existing components, and design tokens. It should not assume your framework or invent test results.

## 5. Use it in your application

### Recommended workflow

| Step | What you ask Codex | Expected result |
| --- | --- | --- |
| **1 — Audit** | Inspect existing UI, components, styles, and breakpoints | A prioritized list of real issues with file locations |
| **2 — Plan** | Propose shared tokens/components and responsive behavior | A small, justified implementation plan |
| **3 — Implement** | Fix one screen or shared component group | Code changes using your current stack and theme |
| **4 — Validate** | Run relevant tests and inspect key states/sizes | Clear pass/fail results, plus untested risks |
| **5 — Review** | Check the diff for regressions | No unrelated business-logic or API changes |

Start with **one screen or a shared component family** rather than requesting a high-risk rewrite of the entire frontend. Ask Codex to keep the application functionality, branding, routing, and existing component library intact unless you explicitly want changes.

### What the skill should consider

- **Visual consistency:** typography hierarchy, spacing, alignment, radii, borders, shadows, icon sizes, reusable design tokens.
- **Component quality:** cards, navigation, buttons, forms, menus, dialogs, tables, feedback and empty/loading/error states.
- **Responsive behavior:** narrow phones, tablets, desktops, landscape, split-screen windows, large text, safe areas, and zoom.
- **Accessibility:** contrast, keyboard navigation, focus indicators, accessible names, errors, touch areas, screen readers, reduced motion.
- **Reliability:** no clipped critical content, broken scrolling, layout flicker, duplicated state, or regressions introduced by refactoring.

### Works with different stacks

| Project type | How to use the skill |
| --- | --- |
| **React / Next.js / Vue / Angular** | Audit shared components, CSS/Tailwind tokens, app layouts, interaction states, and browser responsiveness |
| **Laravel + Blade / Livewire** | Standardize templates, reusable UI components, form validation, tables, and dashboard layouts |
| **React Native / Expo** | Check native navigation, safe areas, touch targets, keyboard overlap, and dynamic text scaling |
| **Flutter** | Apply consistent themes and widgets; test adaptive constraints, text scaling, and platform interaction patterns |
| **SwiftUI / Jetpack Compose** | Follow native accessibility, layout, typography, and navigation conventions |
| **Desktop / .NET MAUI** | Adapt to window resizing, keyboard/mouse interaction, density, and platform conventions |

It is a guidance-and-review skill: it **does not automatically install project dependencies, guarantee bug-free code, or certify WCAG compliance**.

## 6. Ready-to-copy Codex prompts

### A. Audit my UI before editing

```text
$universal-ui-engineering
Audit this project's frontend as a senior UI/UX engineer.
First inspect the framework, existing design system, shared components,
and current screens. Identify inconsistencies in spacing, typography,
cards, forms, navigation, responsiveness, and accessibility.
Report issues with file paths and priority. Propose a focused fix plan.
Do not modify files until I approve.
```

### B. Improve a screen without changing its business logic

```text
$universal-ui-engineering
Improve the UI of [SCREEN_OR_PAGE] using our current components,
colors, typography, and visual identity. Fix alignment, spacing,
component hierarchy, overflow, and missing feedback states.
Support phone, tablet, and desktop layouts where applicable.
Do not change the API, routes, database, or business logic.
Run relevant checks and report what was and was not tested.
```

### C. Standardize cards, buttons, and form inputs

```text
$universal-ui-engineering
Audit every instance of cards, buttons, and form controls in this
project. Reuse existing components and centralize duplicated styling
where appropriate. Standardize their anatomy, spacing, interactive
states, accessibility, and responsive behavior without changing
functionality. Start with a component inventory and implementation plan.
```

### D. Fix mobile responsiveness

```text
$universal-ui-engineering
Find and fix responsive layout problems in [SCREEN_OR_FEATURE].
Test narrow/medium/wide widths, landscape, long labels, large text,
keyboard appearance, and any applicable safe areas. Prioritize
content and keep primary actions reachable. Do not hide essential
content just to make the layout fit. Document the viewport sizes
and checks you actually performed.
```

### E. Review my changes before merging

```text
$universal-ui-engineering
Review the current Git diff for UI regressions. Focus on inconsistent
design tokens, clipped content, broken small-screen layouts,
inaccessible controls, focus behavior, loading/error states, and
unnecessary rendering. Report actionable findings by severity
and file path. Do not edit code unless I ask.
```

### F. Create a new responsive screen

```text
$universal-ui-engineering
Design and implement a new [FEATURE] screen for this project.
Inspect our current styling and components before creating anything.
Define the primary user task, content hierarchy, narrow/wide layout,
reusable components, loading/empty/error states, and accessibility
requirements. Implement the screen and run applicable quality checks.
```

**Tip:** Replace bracketed placeholders like `[SCREEN_OR_PAGE]` with your actual file, page, or feature. For higher safety, separate the audit, approval, and implementation into multiple Codex prompts.

## 7. Optional project-wide instructions

You can also put a short policy in your application's root `AGENTS.md` to remind Codex to apply consistent UI engineering practices. This is **optional**; it does not replace installing the skill.

```markdown
# UI engineering guidance

When working on frontend screens or visual components:
- Use the installed `universal-ui-engineering` skill when appropriate.
- Inspect existing components, tokens, and styles before changing UI.
- Reuse established design patterns instead of introducing duplicates.
- Check responsive layouts, keyboard/focus behavior, and text scaling.
- Preserve API behavior and business logic unless explicitly requested.
- Report exact tests run and any remaining manual checks.
```

If your project already has an `AGENTS.md`, **merge these lines into it** rather than overwriting its existing instructions. For a more extensive template, see [`docs/AGENTS_UI_TEMPLATE.md`](docs/AGENTS_UI_TEMPLATE.md).

## 8. Update or remove the skill

### Update a global Git installation

**Windows (PowerShell):**

```powershell
git -C "$HOME\.agents\skills\universal-ui-engineering" pull --ff-only
```

**macOS / Linux:**

```bash
git -C "$HOME/.agents/skills/universal-ui-engineering" pull --ff-only
```

### Update a project Git submodule

Run from the application's repository root:

```bash
git submodule update --remote .agents/skills/universal-ui-engineering
git add .agents/skills/universal-ui-engineering
git commit -m "Update Universal UI Engineering skill"
```

### Remove a global installation

Close any Codex session using the skill and delete only the `universal-ui-engineering` installation folder inside `~/.agents/skills/`. Do **not** delete your entire `.agents` or `.agents/skills` directory; it may contain other skills. For a Git submodule, use your team's normal submodule removal process instead of simply deleting the folder.

## 9. Troubleshooting

<details>
<summary><strong>I installed it but it does not appear in Codex.</strong></summary>

- Make sure the path ends with `.../.agents/skills/universal-ui-engineering/SKILL.md`.
- Ensure `SKILL.md` is not inside an extra nested folder.
- Open your app folder in Codex, start a new session, and try `/skills` or `$universal-ui-engineering`.
- Restart Codex if necessary.
- Check that your Codex installation supports local skills and that the skill isn't disabled in your configuration.

</details>

<details>
<summary><strong>Git says "destination path already exists".</strong></summary>

Do not clone over an existing installation. If it was installed from Git, use the **Update** command above. If it was copied from a ZIP, inspect and back up any local modifications before replacing the folder.

</details>

<details>
<summary><strong>Git says "repository not found".</strong></summary>

Replace `YOUR_USERNAME` with the **actual GitHub owner**, verify the repository exists, and confirm it is public (or that you have access). Copy the HTTPS clone URL directly from GitHub's **Code** menu.

</details>

<details>
<summary><strong>The skill appears twice.</strong></summary>

You may have installed a global and a repository-level copy with the same skill name. Keep the version you intend to use, or explicitly select the correct entry. Codex does not merge duplicate skills automatically.

</details>

<details>
<summary><strong>Can I use it without Git?</strong></summary>

Yes. Download the repository as a ZIP, extract it, and copy the entire skill folder to the correct `.agents/skills` location. The file structure matters, not the download method.

</details>

<details>
<summary><strong>Does the skill fix all UI bugs automatically?</strong></summary>

No. It guides Codex to inspect, plan, implement, and verify changes. Real-device testing, browser checks, accessibility testing, and human review remain important. The skill asks Codex to report test limitations instead of claiming unverified results.

</details>

## 10. Files, standards, and references

The repository is structured like this:

```text
universal-ui-engineering/
├── README.md                       # Installation & usage guide (this file)
├── SKILL.md                        # Required skill manifest / workflow
├── agents/openai.yaml              # Optional display/skill metadata
├── references/
│   ├── 01-foundations-tokens.md    # Typography, spacing, colors, tokens
│   ├── 02-adaptive-layout.md       # Responsive and adaptive layout
│   ├── 03-components-patterns.md   # Buttons, cards, forms, navigation, etc.
│   ├── 04-accessibility-interaction.md
│   ├── 05-platform-implementation.md
│   ├── 06-quality-assurance.md
│   ├── 07-sources.md               # Official design/accessibility sources
│   ├── 08-implementation-recipes.md
│   └── 09-component-sizing-matrix.md
├── assets/
│   ├── design-tokens.json          # Example semantic design tokens
│   └── web-theme.css               # Optional sample CSS theme
├── scripts/
│   └── check_tokens.py             # Example token validation script
└── docs/
    ├── AGENTS_UI_TEMPLATE.md
    └── UNIVERSAL_UI_UX_ENGINEERING_STANDARDS.md
```

**Full details:** [`docs/UNIVERSAL_UI_UX_ENGINEERING_STANDARDS.md`](docs/UNIVERSAL_UI_UX_ENGINEERING_STANDARDS.md) and the focused [`references/`](references/) documents.

**Using the design tokens:** `assets/design-tokens.json` and `assets/web-theme.css` are examples, **not** mandatory dependencies. If an application already has a design system, keep it and ask Codex to normalize inconsistencies around it instead of replacing the brand styles.

**Optional validation (Python 3):**

```bash
python scripts/check_tokens.py
```

This checks the bundled sample tokens; it does **not** test your application's actual screens. Use your project's own test, lint, build, and accessibility tools for application validation.

### Official documentation

- [OpenAI — Build skills and skill installation locations](https://learn.chatgpt.com/docs/build-skills)
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Apple — Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Google — Material Design 3](https://m3.material.io/)
- [Android — Design for Android](https://developer.android.com/design)
- [MDN — Responsive Design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)

See [`references/07-sources.md`](references/07-sources.md) for the extended source list and the distinction between official requirements and recommended defaults.

### License

No license is bundled in this release. The repository owner should choose and add an appropriate `LICENSE` file before encouraging third-party redistribution or contribution.
