---
name: universal-ui-engineering
description: Design, implement, refactor, or review consistent, responsive, accessible, polished, and regression-resistant user interfaces for web, iOS, Android, desktop, tablets, and cross-platform apps. Use for UI/UX work on cards, forms, dashboards, navigation, typography, spacing, layout, design tokens, breakpoints, dark mode, component states, accessibility, performance, and UI testing in React, Next.js, Vue, Angular, Laravel/Blade, Tailwind, React Native/Expo, Flutter, SwiftUI, Jetpack Compose, .NET MAUI, or native stacks. Apply when creating screens, correcting UI glitches, standardizing components, or auditing responsiveness; preserve the product's existing brand and functionality.
---

# Universal UI Engineering

## Mission
Create interfaces that are **consistent within the product, adaptive to available space and interaction methods, accessible, maintainable, and tested**. Treat this as an engineering process, not a license to apply a generic visual theme. A single universal numeric layout is impossible: web CSS px, iOS points, Android dp/sp, Flutter logical pixels, and desktop density conventions are distinct. Preserve native expectations and established product choices.

## Instruction precedence
1. Explicit user/product requirements and safety/security requirements.
2. Applicable accessibility requirements and platform/API constraints.
3. Existing project design system, design tokens, and component contracts.
4. This skill's suggested defaults, where the project has no established standard.

Never silently override a functioning, intentional product pattern merely because the examples here look different. If requirements conflict, report the conflict and the chosen compromise. Do not claim legal accessibility compliance based only on automated checks.

## Required workflow

### 1. Discover before editing
- Inspect framework, supported platforms, OS minimums, existing theme/design tokens, fonts, icon set, UI/component library, routing, screen structure, accessibility utilities, tests, build commands, and repository instructions.
- Determine the *real* target: responsive website, native app, desktop software, hybrid app, or shared UI. Identify whether it is touch-first, pointer-first, or mixed-input.
- Identify current design debt: inconsistent spacing, repeated one-off styles, clipped text, nested scroll areas, layout shift, unsafe fixed heights, disappearing focus, overcrowded cards, fragile state handling, or UI flicker.
- Inventory shared components before proposing new ones. Prefer extending existing components to introducing parallel variants.
- If there is no project design system, define the **smallest coherent token set** and clearly label defaults as recommendations, not official laws.

### 2. Load just the relevant references
Read these documents only when relevant to the task:
- `references/01-foundations-tokens.md` — type scales, spacing, colors, radii, elevation, iconography, density, token governance.
- `references/02-adaptive-layout.md` — responsive layouts, breakpoints, grids, cards, navigation, tables, keyboards, safe areas, foldables.
- `references/03-components-patterns.md` — component anatomy and states for buttons, cards, forms, modals, tables, menus, alerts, lists, charts, authentication, dashboards.
- `references/04-accessibility-interaction.md` — WCAG 2.2 AA targeting, native accessibility, focus, gestures, motion, RTL, keyboard and screen-reader checks.
- `references/05-platform-implementation.md` — concrete mappings for CSS/Tailwind, Laravel, React/Next, React Native/Expo, Flutter, SwiftUI, Android Compose, and .NET MAUI/Windows.
- `references/06-quality-assurance.md` — testing matrix, screenshot regression, performance, release gates, accessibility and defect severity.
- `references/07-sources.md` — official references, numerical provenance, version/recheck policy.
- `references/08-implementation-recipes.md` — focused implementation examples and QA test patterns when code is needed.
- `references/09-component-sizing-matrix.md` — detailed recommended sizes for nearly every common UI component when no product standards exist.

### 3. Produce a short implementation plan
For a new screen or meaningful redesign, determine before implementation:
- User's primary task and top one or two actions; content priority and information architecture.
- A screen structure (header/navigation, main content, secondary tools, footer), a narrow layout, and a wide layout.
- Reusable components and variants; their empty/loading/error/success/disabled/focus states.
- Relevant tokens (never ad hoc arbitrary values without a reason).
- Accessibility, keyboard, text resizing, locale, safe areas, and performance risks.
- How to prove quality with existing or newly appropriate tests.

For a small bug fix, keep the plan proportional; do not over-engineer.

### 4. Implement by design-system contract
- Use the app's established components and tokens. Add missing semantic tokens before scattering magic CSS or inline constants.
- Build *content-first*, smallest usable width first for responsive web; on native, use window/parent constraints, not assumed device names.
- Use layout primitives, flexible sizing, intrinsic content heights, and container constraints; avoid absolute-position layout for ordinary content.
- Use native controls/semantic HTML when possible; don't implement custom comboboxes, dialogs, or date pickers without a compelling need.
- Keep text selectable, readable, and allowed to wrap. Never solve overflow by hiding important actions or disabling font scaling.
- Distinguish visual size from **interactive hit area**: touch targets must follow the applicable platform guidance.
- Provide distinct hover, press, focus-visible, selected, active, disabled, loading, error, and success feedback where applicable.
- Prefer restrained, purposeful visuals: hierarchy and alignment before shadows/gradients. No arbitrary decorative badges, giant blank cards, pointless icon containers, or excessive rounded corners.
- Prevent interface glitches: reserve image/media space, stabilize loading states, guard async race conditions, clean up listeners, preserve state across resize/navigation, and avoid unnecessary remounting.
- Respect platform conventions for navigation/back behavior, keyboard, safe areas, edge gestures, pointer/hover, and input modalities.
- Keep business logic, API behavior, data models, and user flows unchanged unless requested.

### 5. Review every changed UI across dimensions
**Design:** hierarchy, consistency, readable content, action placement, affordances, density.
**Responsive:** 320 CSS-px reflow where WCAG applies; compact/medium/wide; very short heights; tablet; split-screen/resize; landscape; 200% zoom; largest supported system text; 400% zoom reflow as applicable.
**Accessibility:** keyboard-only, visible and unobscured focus, correct name/role/value, labels/errors, contrast, target sizes, screen reader, motion reduction, color-independent status.
**Behavior:** loading/empty/error/offline/retry/success, slow network, long names, localization, validation, duplicate submissions, navigation state, authorization, destructive actions.
**Quality:** lint/typecheck/unit/component/E2E/visual tests available in repo; console warnings, performance regressions, and no horizontal page overflow.

### 6. Deliver truthful verification
In the response after a code change, briefly report:
1. What changed and what existing conventions were reused.
2. Screen sizes / input modes / states actually tested.
3. Exact commands run and their outcomes; clearly say if tests were **not** run.
4. Remaining risks, deviations, or manual checks needed.

Never describe a UI as fully tested when only static inspection was possible. Do not install or upgrade dependencies, rewrite the design system, or remove project functionality without need and authorization.

## Decision rules (quick application)
| Situation | Prefer | Avoid |
|---|---|---|
| Repeating a surface | Existing shared `Card` with standardized variants | New one-off cards with divergent padding/radii |
| Small phone or large text | Stack sections; wrap labels; scroll vertically | Fixed-height forms, three-column mini cards |
| Narrow table | Prioritized list/card view or isolated labeled horizontal scroll for genuinely tabular data | Whole-page horizontal overflow; silently dropping critical columns |
| Form errors | Explicit text beside fields; error summary when useful; focus management | Color-only red outline or vague toast |
| UI transitions | Animate opacity/transform when meaningful; honor reduce-motion | Continuous or layout-thrashing animation |
| Action hierarchy | One clear primary action per immediate task context | Multiple equally emphasized CTAs |
| Interactive icon | Accessible name and adequate hit region | Bare 16px icon button with no label |
| Mobile/desktop navigation | Adapt navigation to usable window width and input | Identical mobile bottom tabs at all widths |
| Dense enterprise screen | User-selectable comfortable/compact density with stable tokens | Microscopic labels and inaccessible controls |
| Existing library component | Use its accessible, supported API | Rebuild custom widget just for appearance |

## Quality gate / stop conditions
**Block a feature as incomplete** when it has: clipped critical content; irretrievable offscreen actions; unlabeled interactive controls; keyboard traps; inaccessible form errors; essential info conveyed only by color; broken mobile/zoom layout; inaccessible modal focus; broken primary flow; console/runtime exceptions; or a failing relevant regression test.

**Do not claim perfection**. Use targeted automation plus manual inspection on real supported platforms. Follow `references/06-quality-assurance.md` for risk-based coverage.

## Recommended default values, not mandates
- Spacing scale (logical units): `0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96`. Use named tokens, not raw numbers at call sites.
- Web body text: `16px/1.5` as a readable default; `14px` only for appropriate secondary UI; avoid dense, essential 12px text. Native platforms follow dynamic/system text styles.
- Cards: `16–24` units padding depending on density/context; `12–16` units radius only if it fits the visual language; `12–24` gap. These are opinionated starting values.
- Content: comfortable reading line lengths roughly `60–75ch`; constrain forms and prose rather than making every input span a 4K monitor.
- Touch: iOS/iPadOS commonly target `44×44pt`, Android `48×48dp`; Web WCAG 2.2 AA target-size minimum is `24×24 CSS px` **with exceptions**, but aim larger (`44×44 CSS px`) for touch-friendly web controls.
- Web contrast: normal text at least `4.5:1`, large text `3:1`, necessary non-text UI indicators `3:1`, subject to WCAG scope/exceptions.
- Web performance field targets (75th percentile): LCP ≤ `2.5s`, INP ≤ `200ms`, CLS ≤ `0.1`.

See `references/07-sources.md` for which values are official versus local recommendations. The portable sample tokens are in `assets/design-tokens.json` and `assets/web-theme.css`; **use them only if the project lacks a better established design system**.
