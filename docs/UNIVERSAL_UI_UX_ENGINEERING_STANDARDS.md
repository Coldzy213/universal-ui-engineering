# Universal UI/UX Engineering Standards — Web, Mobile, Tablet, and Desktop

**Edition:** 2026-11-16  
**Use:** Standalone code review / AI assistant instructions / project design-system standard.  
**Coverage:** HTML/CSS, React/Next.js, Vue/Angular, Laravel/Blade, Tailwind, React Native/Expo, Flutter, SwiftUI, Android Compose, .NET MAUI, and Windows native apps.  
**Status:** Reusable engineering recommendations informed by primary sources; this document does **not** itself certify legal accessibility compliance or universal platform correctness.

## How to use this document

- Give this file to an engineering assistant as a persistent project reference, or place the folder version (`SKILL.md` + `references/`) under Codex's `.agents/skills/universal-ui-engineering/`.
- For a new application, start with the workflow and token decisions. For an existing application, **preserve its current brand/components** and use these standards primarily for consistency, accessibility, adaptability, and tests.
- The `references/XX-...md` filenames mentioned below correspond to the embedded sections later in this combined document.
- Official WCAG/platform requirements and this skill's optional preferred dimensions are explicitly distinguished in the sources and sizing matrix.
- Each UI request should end with what was actually tested, how, and what remains unverified.

---

## Skill workflow / operating contract

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


---

# 01 — Foundations and Design Tokens

> Scope: shared decisions across web, mobile, desktop, and cross-platform products. Numeric values in this document are **recommended starting points**, not universal platform standards. Use a product's established tokens and host-platform APIs first.

## 1. Core design tenets

1. **Task before decoration.** Prioritize useful content, obvious controls, and one unambiguous primary action per task area.
2. **Structure before color.** Get hierarchy, alignment, typography, proximity, and whitespace correct before visual effects.
3. **Consistency is a contract.** The same UI role gets the same appearance, semantics, behavior, and state treatment within a product.
4. **Native when appropriate.** Native pickers, controls, keyboard behavior, safe areas, system fonts, pointer/remote behavior, and platform navigation often outperform custom imitations.
5. **Adaptive, not shrunk.** A 3-column desktop composition should transform, not merely scale down, on a phone.
6. **Accessible by default.** Accessibility is an interaction and information-quality requirement, not an afterthought.
7. **Content is unpredictable.** Design for long translations, 200% text, numbers, empty values, multiple lines, dynamic updates, and localization.
8. **State is part of design.** A component contract includes interactive, empty, loading, error, success, disabled, focus, and offline states where applicable.
9. **Lower visual noise.** Avoid obligatory gradients, neon shadows, inflated blank cards, needless pill shapes, and gratuitous badges. Express product identity through consistent type, brand, and composition.
10. **Measure and iterate.** Run code quality, visual, interaction, performance, and accessibility checks; test real user flows.

## 2. Three levels of tokens

| Level | Example | Purpose |
|---|---|---|
| Primitive | `space.4 = 16`, `blue.700 = #1D4ED8` | A limited vocabulary of raw values |
| Semantic | `color.action.primary`, `space.card.padding`, `type.body` | Express intent, enable themes and platform variation |
| Component | `button.primary.height`, `card.compact.padding`, `input.focus.ring` | Specific, reusable component recipes |

Prefer semantic variables in application code. A component can use a component token with fallback to a semantic token. Do not couple every button to `blue.700` or every screen to `16px` directly. When adding a token: define intent, name, light/dark and contrast variants, and platform mapping; avoid duplicates. Theme overrides should alter semantic tokens, not one-off selectors.

## 3. Spacing system

Recommended 4-unit foundation, with most primary layout increments divisible by 8:

| Token | Value | Typical use |
|---|---:|---|
| `space.0` | 0 | Reset |
| `space.0_5` | 2 | Optical alignment only |
| `space.1` | 4 | Tight icon/caption relationship |
| `space.2` | 8 | Icon-to-label, tightly related controls |
| `space.3` | 12 | Compact fields, dense card internal gap |
| `space.4` | 16 | Default mobile gutters, standard card padding |
| `space.5` | 20 | Medium card padding |
| `space.6` | 24 | Comfortable card padding, grid gap |
| `space.8` | 32 | Section separation, desktop gutter |
| `space.10` | 40 | Major section gap |
| `space.12` | 48 | Hero-to-section separation |
| `space.16` | 64 | Large editorial whitespace |
| `space.20` | 80 | Large-screen section spacing |
| `space.24` | 96 | Exceptional large separation |

Relationship model:
- Within one labeled control: usually 4–8.
- Between directly related controls or fields: usually 12–16.
- Between independent card groups: 16–24.
- Between distinct sections: 24–48, adjusted for density.
- Title-to-description usually closer than section-to-section spacing.

**Never enforce grid purity at the expense of good optical alignment or OS controls.** Native system gaps, text metrics, platform density, and user-adjusted text may require exceptions.

## 4. Typography scale

### Default web scale (example, not official minimums)

| Role | Suggested size | Weight | Line height | Notes |
|---|---:|---:|---:|---|
| Display | `clamp(2.25rem, 4vw, 3.5rem)` | 650–750 | 1.1–1.15 | Marketing only, sparse |
| Screen H1 | `clamp(1.75rem, 3vw, 2.25rem)` | 650–750 | 1.15–1.25 | One clear screen title |
| H2 | `1.5rem` / 24px | 600–700 | 1.25–1.35 | Section label |
| H3 / card title | `1.125–1.25rem` / 18–20px | 600–700 | 1.3–1.4 | Dense dashboards may use 16–18 |
| Body | `1rem` / 16px | 400–500 | 1.5–1.6 | Default long-form/readable UI |
| Compact body / label | `0.875rem` / 14px | 450–600 | 1.4–1.5 | Secondary/dense UI, not critical tiny text |
| Helper / caption | `0.8125–0.875rem` / 13–14px | 400–500 | 1.4–1.5 | Avoid essential minuscule copy |
| Large metric | `1.75–2rem` / 28–32px | 650–750 | 1.1–1.2 | Keep digits tabular where useful |

Use actual `rem`/relative sizing on web. Do not reset the root font size to 10px or block zoom. Native: use iOS Dynamic Type/text styles, Android `sp` and scalable typography, Flutter system text scaling, React Native font scaling. System text settings must be respected even when custom fonts are used.

Other typography standards:
- Prefer system font stack unless the brand has a licensed, accessible typeface with multiple weights.
- Use max widths for reading text around 60–75 characters; headlines can be shorter. This is a heuristic, not a WCAG success criterion.
- Avoid excessive tracking, very light weights, long all-caps text, and center-aligned long paragraphs.
- Use `tabular-nums` for comparable financial/time metrics; right-align numeric table values.
- Do not truncate critical labels; if truncation is unavoidable, provide a full accessible name or reveal mechanism and test it on touch/keyboard.
- Account for typographic differences in languages and scripts; test English and long localized strings at minimum.
- WCAG 1.4.12 does **not** require authors to set 1.5 line-height in all UI: it requires text to survive user overrides for line/paragraph/letter/word spacing without losing content.

## 5. Color and contrast

Define semantic roles, not fixed colors for arbitrary components:

`surface.canvas`, `surface.card`, `surface.raised`, `text.primary`, `text.secondary`, `text.inverse`, `border.default`, `border.strong`, `action.primary`, `action.primary-hover`, `focus.ring`, `status.success`, `status.warning`, `status.danger`, `status.info`, `overlay.scrim`, `chart.series.N`.

Rules:
- Web WCAG 2.2 AA normal text >= 4.5:1; large text (at least 18pt, or 14pt bold in WCAG's definition) >= 3:1; required non-text UI/graphic boundaries >= 3:1, with applicable exceptions.
- Test each text-background and icon-background pair in actual states, including hovered, selected, disabled (disabled UI has exceptions, but should remain comprehensible), error, and dark mode.
- Never communicate success/error/required status only via red/green. Pair color with clear text, icon shape, or position.
- Do not infer accessible contrast from a color palette name: verify contrast computationally, then inspect visually.
- Dark themes require intentional foreground/surface/elevation tokens. Simply invert all colors is not sufficient.
- Prefer non-transparent semantic surfaces behind essential text to prevent contrast variation against unknown imagery.

The sample `assets/design-tokens.json` includes an intentionally restrained light/dark palette. It is a **starter** and is not proof of accessibility for every composition.

## 6. Shape, borders, shadows, icons, and imagery

| Element | Starting point | Reason |
|---|---|---|
| Small control radius | 6–10 units | Distinct from full pills |
| Card radius | 12–16 units | Cohesive surfaces without inflated look |
| Dialog / large surface | 12–20 units | Could be zero for desktop/system surfaces |
| Borders | 1px web / appropriate hairline or stroke native | Often more stable than many shadows |
| Elevation | 0–2 levels for routine screens | Too many shadow styles create noise |
| Icon visual size | 16, 20, 24 units | Independent from hit area |
| Avatar | 32, 40, 48, 64 units | Size chosen for context; provide fallback initials/label |
| Media | Aspect-ratio controlled | Avoid layout shifts/distortion |

- Icon family, stroke weight, optical size, and baseline must be consistent. Use recognizable symbols; add text labels when meaning is ambiguous.
- Never treat a decorative icon's glyph bounds as the touch target.
- Elevation communicates layering when relevant; avoid using four different shadow recipes to show normal card hierarchy.
- Prefer actual media with preserved aspect ratio (`object-fit`/`BoxFit`) and defined width/height/aspect-ratio on web.
- Animations are for orientation and feedback, not constant activity. Respect OS motion preferences.

## 7. Density modes

For content-heavy enterprise apps, define `comfortable` and optionally `compact` semantic variants. Compact may reduce card padding, row height, and gaps on pointer-first desktop. **Do not reduce touch targets under platform guidelines in touch contexts.** Re-evaluate typography and target sizes separately from decorative density. Avoid automatically switching to compact merely because the viewport is narrow.

## 8. Naming and governance

- Components: `Button`, `IconButton`, `TextField`, `Card`, `MetricCard`, `ListItem`, `Dialog`, `EmptyState`, `DataTable`, `Skeleton`.
- Slots: header / description / media / body / actions / footer; use predictable APIs.
- Variants: `appearance` (solid/outline/ghost), `intent` (neutral/primary/danger), `size` (sm/md/lg), `density`, `state`.
- Prefer *one component with limited variants* over many near-duplicate components.
- Create a documented exception only when the pattern actually differs; return recurring exceptions to tokens.
- Whenever a token changes, review **all consumers**, light/dark themes, and compact/wide behavior; add a visual regression baseline for important shared components.

## 9. Anti-pattern review

Reject arbitrary font sizes, five unrelated radii, padded icon boxes on every label, repeated primary CTA colors on low-priority actions, multiple accent colors without meaning, all-section cards with empty internal space, fixed hero heights on short devices, decorative charts with no accessible data, and tiny gray-on-gray helper labels. Prefer purposeful density and product-specific identity over templated visual flourishes.

**Sources:** USWDS design tokens and typography; Atlassian spacing; Apple design principles and accessibility; WCAG 2.2. URLs and normative notes in `07-sources.md`.


---

# 02 — Adaptive and Responsive Layout

## Guiding distinction
**Responsive**: fit content in the current available space. **Adaptive**: select an arrangement, navigation pattern, or input method suitable for that space and input context. Device detection alone is an unreliable substitute for measuring the available app window. Support resizable desktop windows, tablet split views, foldables, external displays, virtual keyboards, and increased system text.

## 1. Breakpoints and layout modes

Android's current adaptive width classes are: compact `<600dp`, medium `600–839dp`, expanded `840–1199dp`, large `1200–1599dp`, extra large `>=1600dp`. The thresholds classify **app window width in Android dp**, not physical screen resolution. Other platforms should use their own adaptive constraints; do **not** equate CSS px, dp, iOS pt, and Flutter logical pixels simply because the numbers look similar.

For **web design**, the following CSS-pixel thresholds are a useful *optional starting map*, not an official cross-platform spec:

| Available content viewport width | Suggested behavior |
|---|---|
| 0–359px | Very narrow; single column, avoid side-by-side field actions |
| 360–599px | Compact; stacked cards, lightweight header, bottom/overflow nav where appropriate |
| 600–839px | Medium; two-column cards when card width still works; mixed navigation |
| 840–1199px | Expanded; rail/sidebar or two-pane master/detail |
| 1200–1599px | Large; full desktop shell, optional third context pane |
| 1600px+ | Extra large; maintain useful maximum widths instead of stretching text indefinitely |

**Breakpoint rule:** switch when *content needs it*, not because of a device marketing category. For widgets inside sidebars and dashboards, container queries are often better than viewport breakpoints.

## 2. Overall shell and spacing

Recommended starting outer horizontal gutters, adjusted for density and platform safe areas:
- Small content width: 16 units; 12 only when space is severely constrained and touch/readability remains good.
- Medium: 20–24 units.
- Wide: 24–40 units.
- Very wide: center primary content with max width about 1200–1440 units for general apps; large data dashboards may intentionally use more.
- Reading column: around `60–75ch` for sustained prose; forms often `420–560px` max width on web, with full-width behavior on compact screens.
- Desktop sidebars: size based on labels and minimum main content width, not a mandatory fixed number. A 240–280px starting point often works; collapsed rail 64–80px if product supports it. Native components take precedence.

Use a grid or flex container with `minmax(0,1fr)` and `min-width:0` on children prone to overflow. Avoid hardcoded pixel heights on text-bearing content. Never use `100vw` for content inside a viewport that may include scrollbars, creating needless horizontal overflow.

## 3. Layout recipes

**Authentication:** single primary column, centered/max-width around 360–440px when wide, aligned toward top/center depending keyboard and content; logo, concise heading, labels, inline errors, primary action, supporting link. On compact widths use full width minus safe gutters; avoid cramped desktop-style side-by-side visuals and fixed-height center containers that disappear under the keyboard.

**Dashboard:** screen title + context/action toolbar; primary KPI cards; highest-value trend/chart; main data; recent actions. Compact: vertical sequence and 1-column or 2-up metrics only where each remains readable. Medium: 2-column cards. Expanded: 3–4 cards if widths permit. Avoid 4 tiny cards on 320px or a 1,800px-wide single card with one number.

**List/detail:** single pane + navigation on compact; two panes on expanded; preserve item selection and scroll/restoration when transitioning between modes. Don't render hidden duplicates accessible to screen readers.

**Settings:** grouped rows, descriptions, toggles and dangerous actions clearly separated. Allow long labels and large text; use dividers sparingly, not cards around every line item.

**Editor/workbench:** prioritize the canvas/task area, permit resizable panels on desktop, dock/overlay secondary options on small devices with keyboard/back support; keep undo and primary actions accessible.

**Data table:** maintain true tabular relationships for compare-heavy data; on small widths either (a) provide a responsive summary list with explicit labels and access to complete details or (b) scroll the table *within a labeled region*, not the whole page. Preserve sorting, row actions, and meaningful column context. Tables can be exceptions to reflow when two-dimensional layout is essential, but that is not a blanket exemption for poorly planned tables.

**Dialog/sheet:** ensure max-height relative to currently visible region and internal scroll when truly needed; keep title, dismiss, and key actions accessible. On mobile a bottom sheet/fullscreen form can be better than a fixed desktop modal. Honor safe area and software keyboard.

## 4. Adaptive navigation

- Compact: bottom navigation can suit a small set of primary destinations; use 3–5 well-labeled items as a heuristic, not a hard universal law. Use top-bar actions or a menu for secondary tasks.
- Medium: consider navigation rail, compact drawer, or adaptive top nav where appropriate.
- Large: labeled persistent sidebar, rail, or top nav based on app type. Provide visible selected state and page title.
- Preserve deep linking, back behavior, active destination, and keyboard focus after navigation changes.
- Do not move a critical function to a hidden icon-only menu solely to make a screenshot look clean.
- Desktop apps should support keyboard shortcuts where appropriate; touch/remote/pen users need equivalent visible interactions.
- Apple navigation and Android adaptive layouts use their own established patterns; do not force a web sidebar onto iOS or permanently keep phone bottom tabs on a large tablet.

## 5. Responsive components

A card should choose stack vs split by **its container width** and content demands, e.g. a 300px card in a 1200px page still needs the narrow layout. Define `min-width:0` for text columns, `max-width:100%` for media, and allow actions to wrap or stack. Do not shrink all contents until they fit; reflow relationships instead.

Avoid fixed aspect ratios for text-only cards. If card height is equalized within a row, use a flexible body and anchored footer **without clipping dynamic text**. Only clip text if a legitimate preview contract exists and a full description remains accessible.

## 6. Safe areas, keyboards, viewport units, notches

- iOS: align functional controls inside safe areas, support Dynamic Type, keyboard, home indicator, and split-view/multitasking; use SwiftUI safe-area APIs rather than status-bar padding hacks.
- Android: respect system insets, edge-to-edge behavior, IME insets, display cutouts, gesture navigation, and foldable hinges with Jetpack APIs.
- React Native/Expo: use project-supported safe-area insets, keyboard-aware patterns, and `useWindowDimensions` (reacts to font scale and window resizing); do not rely on `Dimensions.get` once at launch.
- Flutter: use `SafeArea`, `MediaQuery.sizeOf`/`LayoutBuilder`, and adaptive platform UI. Avoid choosing layout from device type or orientation alone.
- Web: test `100svh` / `100dvh` (dynamic resizing can be jumpy), virtual keyboard, sticky footer collisions, and `env(safe-area-inset-*)` on full-bleed PWA views where applicable. Avoid rigid `100vh` login screens hiding the submit button on mobile browser chrome/keyboard.
- Wearable, TV, automotive, and spatial UI have specialized focus/navigation/size guidance; do not apply phone-only geometry indiscriminately.

## 7. Edge-case matrix

Test, at minimum, these cases for every changed important screen:

| Case | Expected behavior |
|---|---|
| 320 CSS-px width on web | No loss of function and no two-axis scrolling for ordinary vertically scrolling content (WCAG 1.4.10 exceptions apply) |
| 360–390 narrow phone | All actions tappable, no clipped nav/CTA |
| 600–840 medium width | Grid/nav reflow does not create awkward orphaned columns |
| 1024–1440 desktop | Side panel and content coexist without overflow |
| Ultra-wide display | Content not needlessly stretched; secondary panels rational |
| Short landscape height | Dialog/menu and key actions can be reached |
| Web text zoom 200% / 400% | Content/interaction survives; reflow requirements respected |
| Largest system native text | No clipped labels, stacked controls as needed |
| Long localized strings | Wrap/reflow, no overlap, sensible RTL where supported |
| Software keyboard shown | Focused field and submit action reachable, safe insets handled |
| Slow images/network | Space reserved; stable loading/empty/retry states |
| Split-screen/fold | No reliance on initial screen width, hinge occlusion avoided |

## 8. Layout decisions that reduce bugs

- Prefer modern CSS Grid and Flexbox, container queries, intrinsic sizing, and wrap. Use absolute positioning for overlays only.
- Avoid sticky header/fixed footer combinations that obscure focused fields; use `scroll-padding`, safe area offsets, and test Tab navigation.
- Set media dimensions and predictable skeleton dimensions to limit CLS.
- Use `min-height` instead of fixed height for text-bearing card/list rows.
- Limit nested scroll containers; if necessary, ensure scroll ownership and keyboard navigation are clear.
- Preserve state on resize; avoid remounting the app tree because of one breakpoint change.
- Beware overflow from long URLs, large charts, tooltips, icons, and unbroken labels; allow wrapping or `overflow-wrap:anywhere` where semantically appropriate.

**Sources:** Android window size classes, Android navigation, Flutter adaptive design, Apple layout, MDN container queries/viewport units, WCAG 1.4.10. See `07-sources.md`.


---

# 03 — Component Specifications and Interaction States

> All dimensions below are starting recommendations **unless explicitly labeled WCAG or platform guidance**. Components inherit project tokens and native conventions. Contracts include behavior, semantics, responsive layout, and UI state; matching colors alone is not consistency.

## 0. Shared component contract

For each reusable component define: purpose, required props, slots, allowed variants, size/density, visual/accessible name, default/hover/pressed/focus/selected/disabled/loading/error/success states as appropriate, keyboard and screen reader behavior, truncation/overflow, responsive behavior, dark/high-contrast behavior, test IDs only when needed, visual and accessibility tests.

### Universal state matrix

| State | Expected UI behavior |
|---|---|
| Default | Discoverable affordance, readable content |
| Hover | Subtle emphasis when pointer exists; not exclusive signal |
| Press / active | Immediate response to input, no duplicate dispatch |
| Focus-visible | High-contrast visible focus; never removed |
| Selected | Persistent state distinct from hover/focus; announced programmatically |
| Disabled | Correct disabled semantics, explain prerequisite where useful |
| Loading | Content stability, progress indication, block duplicate mutating actions |
| Empty | Context, next step, optional relevant CTA |
| Error | Plain-language cause/recovery action, preserve user data |
| Success | Clear completion feedback, updated UI, no misleading toast |
| Offline/timeout | Explain limitation, retry and recovery, avoid data loss |

## 1. Buttons and icon buttons

**Anatomy:** label or icon + accessible name; optional supporting icon; interactive container; progress indicator. Primary button for the key action, secondary/outline for supporting action, destructive intent for irreversible action, ghost/text for tertiary actions.

- Recommended web touch-friendly min hit box: 44×44 CSS px; Android recommended 48×48dp; iOS common 44×44pt. Native pointer-first desktop controls can be visually smaller per OS but must remain accessible.
- Typical comfortable button visual height 40–48 logical units; if the rendered button is smaller, enlarge the hit target without creating overlaps.
- Horizontal padding around 12–20, icon-text gap 8, icon 16–20 visual units; avoid universal fixed width unless necessary.
- Use descriptive verbs: `Save changes`, `Add item`, `Try again`, not generic `Submit` where context is ambiguous.
- Prevent double submission with a pending state and state-aware async behavior; keep user informed about outcome.
- Keyboard: Enter/Space activate according to native control. Focus not trapped. Icon-only buttons need explicit accessible label and optional tooltip, not tooltip-only naming.
- For dangerous actions, convey impact and give cancellation/undo or confirmation when warranted; avoid confirmation for harmless routine tasks.
- Don't use a button for navigation when the semantic action is a link on the web.

## 2. Cards

**Card contract:** coherent group of related content; optional overline/status, title, metadata, body, media, footer, actions. Do not nest cards just to add decoration.

Recommended variants:

| Variant | Layout | Padding | Content |
|---|---|---:|---|
| Content card | vertical | 16–24 | Title, body, optional action |
| Metric card | vertical | 16–24 | Short metric label, 24–32 value, context/comparison |
| Media card | image + content | 0 for media, 16–24 for body | Preserve aspect ratio, fallback |
| Compact list card | row or stack | 12–16 | Condensed summary and trailing action |
| Interactive card | whole-surface primary action if it truly is one | 16–24 | Clear hover/focus, nested actions avoided |

- Radius around 12–16 if aligned with product style; use subtle border or elevation; do not stack strong border + strong shadow + solid gradient by default.
- Typical gap internal 8–16; between cards 16–24. Use alignment/spacing relationships, not vertical emptiness, to create structure.
- Make the entire card clickable **only** if it represents a single navigation action and won't contain nested controls. Otherwise keep action controls individually interactive.
- Card title must wrap as needed; no fixed card height that clips long descriptions or large fonts.
- Status: use text plus color/icon; don't create colored status pills for decorative metadata.
- Responsive media: stack image/content on narrow container; never crop essential image text.
- Metric cards: use a clear unit, timeframe, comparison direction, and empty/zero behavior; don't color a negative percentage as 'bad' when a decrease is desirable.

## 3. Text fields, textareas, selects, checkboxes, radios, switches

**Text input:** persistent visible label, optional hint, control, validation/error text, character count only when useful. Placeholder is an example, **not a substitute for label**. Native keyboard type/autocomplete appropriate to data.

- Example comfortable field min-height 44–48 touch units, padding around 12–16. On web use `min-height` and allow labels/hints to grow.
- Labels commonly 14–16 web px, body/input text 16px on mobile web as a safe default to avoid iOS focus zoom; verify native text styles separately.
- Clear purpose before format; use correct semantic `type`, `autocomplete`, `inputmode`, content types, and autofill.
- Mark required inputs textually and programmatically. Avoid `*` alone unless legend explains it.
- Validate thoughtfully: on submit, or after field interaction where useful; do not shout errors before users have typed.
- Error text: explain what is wrong and how to fix it, near input and programmatically associated. Preserve entered values and focus first invalid field or error summary appropriately.
- Textareas grow or scroll gracefully; don't hard-cap height without showing overflow. Avoid automatic resizing that makes surrounding layout jump unnecessarily.
- Switch = immediate on/off state, checkbox = selection or independently toggleable settings, radio = mutually exclusive options, select/combobox = choice among options. Don't use switch to represent 'accept terms' where checkbox semantics suit better.
- Touch/focus targets for radios/checks include their labels; keep row spacing to avoid activating adjacent options.
- Avoid custom dropdowns/pickers unless native/library controls cannot meet the user need; implement ARIA APG keyboard model for custom widgets.

## 4. Navigation, tabs, breadcrumbs, sidebars, menus

- Make current page/tab clear by text and persistent visual state; announce `aria-current` or selected roles as applicable.
- Tabs switch sibling content views, navigation links change location. Do not mix semantics merely because both look like underlined labels.
- Bottom nav suits a small set of primary phone destinations; adapt to rail/sidebar at wider widths as appropriate.
- Breadcrumbs benefit deep hierarchies on large screens, but don't duplicate every tiny screen's back affordance.
- Menus must support dismissal, keyboard navigation, Escape, focus restoration, outside-click behavior, and viewport collision handling; use tested library components.
- Sidebar collapse should preserve findability, labels/tooltips, selected navigation, and keyboard order.

## 5. Dialogs, bottom sheets, drawers, popovers, tooltips

- Dialogs interrupt a flow; use only when necessary. Include concise purpose, content, sensible primary/secondary actions, and a way to dismiss except for rare truly non-cancelable operations.
- Modal dialog keyboard focus stays inside until dismissed, moves inside on open, returns appropriately on close; background is inert/inaccessible while modal.
- Don't place destructive default focus or Enter action where accidental activation is risky.
- On narrow/short screens, dialog content and controls remain reachable with scrolling and keyboard open. Bottom sheets must respect gesture navigation and safe areas.
- Popovers are lightweight context; dismiss on Escape and avoid hiding current focus. Use anchor positioning/collision avoidance.
- Tooltips provide supplemental information, not primary instructions; support keyboard focus and dismissibility, not hover alone.
- Toast: concise non-blocking feedback, not the only place to show errors, no essential information that disappears before it can be read; provide live-region semantics as appropriate.

## 6. Tables, filters, sorting, pagination

- Use a table only when relationships across columns matter. Align labels left, numbers right, use tabular numerals, clear units and locale formatting.
- Sticky table headers must not obscure focus; column headers remain identifiable to assistive technology.
- Sorting explicitly reflects direction and state, not icon color only; preserve filters in URL/state if relevant.
- Table action menus have sufficient focus/target sizes and are not visible only on hover.
- Responsive: convert to labeled summary cards when comparison isn't essential, or scroll **table region only** with affordance; don't hide critical data without an alternative.
- Empty filtered results: distinguish no data from no results under current filters. Offer `Clear filters`.
- Infinite scroll needs accessible announcements/navigation and recovery; pagination is often more predictable for management systems.

## 7. Alerts, validation, status, loading

- **Inline error:** explain field mistake with linked semantics.
- **Page error:** identify failed operation, give retry/back, preserve context; authorization errors shouldn't leak secrets.
- **Banner/notice:** persistent when the user must act; otherwise dismissible and non-obstructive.
- **Snackbar/toast:** transient confirmations; allow enough time and avoid obscuring bottom controls.
- **Skeleton:** reserve realistic dimensions; no rapidly flashing shimmer; screen-reader handling should not announce dozens of placeholders.
- **Progress:** determinate when measurable; indeterminate when not; avoid arbitrary pseudo-progress. Announce meaningful status changes.
- **Empty state:** plain title (`No invoices yet`), short explanation, task-relevant next action. No oversized illustration required.

## 8. Search, autocomplete and command interfaces

- Search box labeled, with clear behavior for clearing and submitting; do not confuse filtering and navigation.
- Debounce when appropriate, cancel stale requests, and never allow old results to overwrite newer queries.
- Provide loading/no-results/error states and query persistence as needed.
- Autocomplete must implement correct combobox semantics, keyboard arrows/Enter/Escape, and screen-reader announcements or use a proven library.
- Keep filter chips/removable tags keyboard accessible with explicit accessible removal labels.

## 9. Charts, data visualization, dashboards

- Begin with the question the chart answers. Give axes, labels, units, legends, and contextual time range.
- Avoid relying solely on color to distinguish series; provide accessible summary/data table if chart conveys essential information.
- Provide descriptive empty/error states, scale that doesn't mislead, and data provenance. Check contrast for grid, lines, and points that convey meaning.
- Pie charts for many categories and 3D charts routinely reduce comparison clarity; prefer clearer alternatives.
- Responsive chart content must retain readable tick labels and controls; reduce ticks or offer drilldown instead of shrinking the whole chart to unreadable text.

## 10. Lists, avatars, chips, accordions, and media

- List rows: stable reading order, primary label prominent, optional metadata secondary, clear tap target and trailing action.
- Avatars: fall back gracefully; provide person names in accessible content rather than relying on initials or photo alone.
- Chips: distinguish filter, input tag, and passive status. Passive status must not visually promise click behavior.
- Accordions: button semantics, `aria-expanded`, controlled panel association, usable keyboard navigation, sensible initial state.
- Image/media: descriptive alternative text only when informative; decorative images have empty alt; preserve media ratio and dimensions; provide captions and appropriate controls.

## 11. Authentication and sensitive flows

- Make sign-in recovery and account switching discoverable. Use proper `autocomplete` (username/password/one-time-code) and allow password managers.
- Don't block pasting into credentials or one-time-code fields. Support show/hide password via labeled accessible control.
- Show real input validation errors near fields; avoid generic popups for each mistake.
- Don't expose private account detail in front-end notifications. Preserve intended return destination when authorized.
- Prefer security-safe server error handling, rather than conflating wrong credentials with a UI glitch.

## 12. Component acceptance checklist

Before shipping any new shared component, verify: correct semantic control; consistent token use; default/hover/active/focus/selected/disabled/loading/error where relevant; accessible name; keyboard path; contrast; hit area; 200% text/zoom; narrow container; dark mode; RTL/locales if supported; long text; motion preference; touch and pointer behavior; screenshot or story tests.

**Sources:** WAI ARIA APG, WCAG 2.2, Apple HIG, Android UI, W3C forms tutorials, USWDS. See `07-sources.md`.


---

# 04 — Accessibility, Input, and Interaction

**Web baseline:** aim to satisfy **WCAG 2.2 Level AA** for applicable web experiences; review jurisdictional/legal requirements separately. Accessibility evaluation includes judgment and manual assistive-technology use—axe/Lighthouse automation is not a certification. For native apps, follow platform accessibility semantics and controls while borrowing relevant accessibility principles.

## 1. Essential WCAG 2.2 checkpoints

| Area | Criterion | Required behavior / note |
|---|---|---|
| Non-text alternatives | 1.1.1 (A) | Informative images and icon controls have meaningful text equivalents; decorative media excluded appropriately |
| Info/relationships | 1.3.1 (A) | Structure, labels, grouping, table relationships expressed semantically |
| Meaningful sequence | 1.3.2 (A) | DOM/screen-reader reading order sensible |
| Orientation | 1.3.4 (AA) | Don't lock orientation unless essential |
| Identify input purpose | 1.3.5 (AA) | Use semantic autocomplete for common personal inputs where applicable |
| Color-independent meaning | 1.4.1 (A) | Don't encode errors/selection/status through color alone |
| Contrast, text | 1.4.3 (AA) | Normal text at least 4.5:1; defined large text at least 3:1, with exceptions |
| Resize text | 1.4.4 (AA) | Text at 200% without loss of content or functionality, with exceptions |
| Reflow | 1.4.10 (AA) | Ordinary vertical content usable at 320 CSS-px equivalent without two-axis scrolling; defined exceptions for 2D content |
| Non-text contrast | 1.4.11 (AA) | Necessary UI boundaries/graphics at least 3:1 against adjacent color(s), with exceptions |
| Text spacing overrides | 1.4.12 (AA) | No loss when user overrides line/paragraph/letter/word spacing per standard; **not** a mandate to set those values by default |
| Hover/focus content | 1.4.13 (AA) | Additional content is dismissible, hoverable, persistent where required |
| Keyboard | 2.1.1 (A), 2.1.2 (A) | Everything operable by keyboard, no keyboard trap |
| Timing and motion | 2.2.x, 2.3.x | Respect time limits, avoid harmful flashing; provide motion alternatives when required |
| Navigation | 2.4.3 (A), 2.4.7 (AA) | Logical focus order, visible focus |
| Focus not obscured | 2.4.11 (AA) | Focused component not *entirely* hidden by authored content. Stronger preferred outcome: fully visible |
| Pointer gestures | 2.5.1 (A) | Complex gestures have single-pointer alternative except essential cases |
| Target size | 2.5.8 (AA) | 24×24 CSS-px target minimum or satisfy a specified exception (spacing/equivalent/inline/essential/user-agent control) |
| Dragging | 2.5.7 (AA) | Drag operations have a non-dragging alternative unless essential |
| Error identification | 3.3.1 (A), 3.3.3 (AA) | Identify input error and suggest correction when known/appropriate |
| Redundant entry | 3.3.7 (A) | Don't repeatedly request same information within process without allowed exceptions |
| Accessible authentication | 3.3.8 (AA) | Avoid cognitive-function tests without permitted alternatives/assistive mechanisms |
| Name/role/value | 4.1.2 (A) | Programmatically discernible role, states, values |
| Status messages | 4.1.3 (AA) | Convey important dynamic status without necessarily moving focus |

This is a high-impact checklist, **not** an exhaustive enumeration of all WCAG success criteria. Consult the official quick reference for a complete conformance evaluation.

## 2. Target sizes: units and nuance

- **Web WCAG 2.2 AA:** at least 24×24 **CSS pixels**, with documented exceptions. Meeting 24×24 is a minimum accessibility test, not the best ergonomic design for all touch devices. Target 44×44 CSS pixels for comfortable general-purpose touch web controls whenever layout permits (product recommendation, not WCAG AA mandate).
- **iOS/iPadOS:** Apple recommends comfortable touch controls around 44×44 **points** in its design tips; newer platform guidance specifies platform default and smaller allowed minimums in some contexts. Use Apple system controls and spacing guidance rather than assuming every rendered control must visibly be 44pt tall.
- **Android:** recommended 48×48 **dp** touch targets. The glyph itself may be smaller if the actual interactive region is 48dp.
- **Pointer-first desktop and TV/wearable:** use platform-specific selection, focus, remote, or gaze targets. Don't blindly transpose phone defaults.
- Avoid adjacent invisible hit areas overlapping in a way that activates the wrong target.

## 3. Keyboard and focus

- Prefer native HTML `<button>`, `<a href>`, `<input>`, `<select>`, `<dialog>` where appropriate: built-in roles, focus and keyboard behavior reduce defects.
- Tab/Shift+Tab travel in logical reading order; `Enter`/`Space` behavior follows control conventions; Escape closes temporary overlays where appropriate.
- Use `:focus-visible` and a ring that is genuinely visible against the surrounding surface. Do not globally set `outline: none` without a proper replacement.
- Focus must not be hidden by sticky navigation, headers, cookie notices, sheets, or popovers. Use scroll padding/scroll margin and explicit focus management.
- Distinguish keyboard focus from selection/activation; when a dialog closes, return focus to a sensible point.
- Avoid positive `tabindex` values or extra tab stops on non-interactive surfaces.
- For advanced widgets (tabs, tree, combobox, menu, grid, dialog), use tested accessible libraries and WAI-ARIA Authoring Practices keyboard patterns. ARIA roles without behavior are insufficient.
- Accessible drag-and-drop requires buttons/keyboard alternatives for reordering.

## 4. Screen reader / semantics

- Web: semantic landmarks (`header`, `nav`, `main`, `footer`), meaningful heading order, descriptive links, actual lists/tables, label association, conditional live regions only for important updates.
- Native: expose element role, label, value, hint, and grouping correctly; ensure accessible reading order matches visual task order.
- Avoid duplicate announcements from icon plus redundant visible text or skeleton placeholders.
- For images: useful alt for informative media; `alt=""` for decorative images. Don't prepend 'image of' needlessly.
- Do not hide critical instructions only in inaccessible tooltip, placeholder, or gesture.
- Test the *entire flow* with VoiceOver, TalkBack, and desktop screen reader (such as NVDA/VoiceOver) as supported, not only individual controls.

## 5. Forms and errors

- Labels are persistent; hints/format requirements precede errors. Keep user input after failed validation.
- Use programmatic `required`, `invalid`, `describedby` and equivalent platform semantics, with matching visible text.
- Provide concise remediation: `Enter a valid email address, such as name@example.com`, not just `Invalid`.
- On failed submit, use field-level errors plus an error summary for long forms; move focus predictably to summary/first error when appropriate. Do not scream during every keystroke.
- Validate on server even when client provides friendly immediate feedback.
- For sensitive/destructive workflows, confirmations or undo should prevent accidental data loss; prevent duplicate submit while pending.
- Do not require users to memorize previously entered data or defeat password managers/paste to enforce authentication rituals.

## 6. Contrast, motion, and preferences

- Test actual color pairs, including gradients and imagery. Required text/buttons should not become unreadable on hover, pressed, disabled transitions, or dark theme.
- Respect reduced motion/animation OS preferences. Remove non-essential parallax, sweeping transitions, large motion; essential state changes must remain comprehensible.
- Avoid auto-rotating content without pause/stop; consider timing and cognitive load.
- Support high-contrast/forced-colors modes when relevant; do not rely on background-color alone for selection.
- Respect text scaling, bold text, display zoom, OS dark mode as product settings require, and reduced transparency where applicable.
- Sound should not be the sole success/error indicator; use text and visual signals.

## 7. Internationalization, locale, RTL

- Strings can expand 30–100% depending on language; test rather than relying on an exact expansion rule.
- Use locale-sensitive numbers, currencies, dates, and collation. Don't concatenate translated fragments or assume order of personal names.
- Use logical CSS properties (`margin-inline-start`, etc.) and platform equivalents for bi-directional layouts; mirror directional icons where semantically appropriate.
- Format hints must reflect region; don't force US phone, postal code, or date assumptions on global apps.
- Respect composition/IME for CJK and other scripts; defer destructive normalization until composition ends.

## 8. Manual accessibility pass (one complete flow)

1. Start at top of page; keyboard only; reach every useful control; visible focus throughout.
2. Open/close menu, dialog, tooltip, combobox, tab controls; confirm Escape, focus containment/return.
3. Increase browser text zoom to 200% and narrow to 320 CSS px equivalent for applicable content; inspect clipping and reflow.
4. Apply user text-spacing override, high contrast/forced colors, reduced motion, and dark mode where supported.
5. Use screen reader and confirm headings, link destinations, field labels/errors, control states, status messages, and reading order.
6. Attempt the flow with a touch screen; check target selection, screen keyboard, scrolling, and rotation.
7. Test both failed and successful submissions; verify notices are understandable without relying on color.
8. Record defects with screen, steps, expected/actual, platform, viewport, text scale, and severity.

**Sources:** W3C WCAG 2.2 and WAI-ARIA APG, Apple HIG Accessibility, Android app accessibility, Flutter accessibility, MDN reduced motion. See `07-sources.md`.


---

# 05 — Platform Implementation Map

**Principle:** share *semantics, intent, tokens, design decisions, accessibility goals and tests*, but allow the OS/framework to implement its native unit system and interaction idioms. Copying the same pixels everywhere is not cross-platform consistency.

| Platform | Spacing/sizing unit | Typography | Responsive primitives | Interaction/accessibility |
|---|---|---|---|---|
| HTML/CSS web | CSS px/rem/em, `%`, grid tracks, container queries | `rem`, fluid type, OS/browser font scaling | Grid, Flexbox, `@media`, `@container`, `min()`, `clamp()` | Semantic HTML, WCAG 2.2, focus-visible, keyboard, ARIA APG |
| React/Next/Vue/Angular | CSS rules, existing design-system tokens | Follow web/browser rules | Component-driven CSS/utility patterns | Reuse semantic components and test flows |
| Laravel Blade/Livewire/Inertia | CSS/Tailwind/Bootstrap or other existing tokens | Follow web rules | Shared Blade/JS UI building blocks | Server validation, progressive enhancement, focus after updates |
| React Native/Expo | density-independent layout units (dp-like) | `Text` and font scaling; honor OS settings | `useWindowDimensions`, flexbox, safe areas | `Pressable`, native labels/roles, TalkBack/VoiceOver, keyboard |
| Flutter | logical pixels | `TextTheme`, `MediaQuery.textScaler` / platform scaling | `LayoutBuilder`, `MediaQuery.sizeOf`, `SafeArea`, adaptive widgets | Semantics, focus/shortcuts, material/cupertino selection |
| iOS/iPadOS SwiftUI | points | Dynamic Type and text styles | flexible stacks/grids, GeometryReader only as needed, size classes, safe areas | VoiceOver, keyboard, standard navigation/controls |
| Android Compose | dp for layout, sp for text | Material typography, `sp`, fontScale | window size classes, adaptive navigation/scaffold, insets | TalkBack, semantics, 48dp hit areas, system back |
| .NET MAUI | device-independent units | platform font scaling and semantic styles | Grid/FlexLayout/VisualStateManager, size changes | SemanticProperties, safe areas, platform gestures |
| Windows / WinUI | effective pixels and Fluent styles | Fluent system text styles | Grid, adaptive triggers, NavigationView | keyboard, pointer, screen reader and platform accessibility |

## Web / React / Next.js

- Detect existing UI library, Tailwind version, CSS Modules, Sass and tokens before adding alternative framework.
- Map semantic tokens to CSS custom properties with dark-mode `[data-theme="dark"]` or established theme mechanism. Use logical padding/margins for RTL.
- Prefer `font-size:1rem` / default browser root semantics rather than forced root sizes. For fluid headlines use bounded `clamp`, not unrestricted viewport width.
- Default image style: `display:block; max-width:100%; height:auto` and reserve width/height/aspect ratio.
- CSS Grid for page/multi-column composition, Flexbox for linear control groups, container queries for reusable card behavior.
- Use `min-width:0` for nested text/flex children to prevent overflow; `minmax(0,1fr)` for grid tracks.
- In React, preserve stable `key`s, don't mutate shared state, cleanup effects, abort outdated async fetches; don't remount subtrees on breakpoint changes.
- In Next.js, use optimized images thoughtfully, minimize client components where unnecessary, and reserve layout dimensions to avoid CLS.
- Keep validation on server; accessible client feedback is additive.
- Use Playwright screenshot/flow tests and axe auditing if project supports them.

## Tailwind / component libraries

- Use existing Tailwind tokens via project theme or config, not arbitrary `px-[17px]` everywhere.
- Respect installed Tailwind major version when changing config or CSS directives; do not paste v3 configuration into v4 blindly.
- Centralize variant definitions using components, not 80-class duplicates on each page.
- Library defaults (e.g. Radix/shadcn, MUI, Bootstrap, Ant Design) may have their own accessibility conventions; extend their theme rather than conflicting external overrides. Do not mix several component libraries without reason.
- Verify responsive class behavior, hover-only actions, focus, disabled/loading state, and browser zoom.

## Laravel / Blade / Inertia / Livewire

- Extract repeated cards, form fields, alerts, and table actions into Blade components or current framework's shared component system.
- Reuse server-side validation error bags and `old()` values for form persistence; associate errors with controls.
- Avoid double-binding events when Livewire/Alpine/jQuery rehydrate components.
- Avoid layout shift from deferred loading, images, or Ajax fragment replacements. Maintain loading and error placeholders.
- Make pagination, sorting, filters, modals, destructive actions work correctly after partial updates; preserve focus/scroll where appropriate.
- Don't change controllers/endpoints or query behavior while restyling unless explicitly part of task.

## React Native / Expo

- Use `useWindowDimensions()` for live window width/height/fontScale; don't size everything off physical screen dimensions measured once.
- Use `flexShrink`, `flexWrap`, flexible layouts and `maxWidth` rather than hardcoded height/width for text regions.
- Preserve `allowFontScaling` unless a justified accessibility-compatible exception exists; test largest system font sizes and screen reader.
- Use `Pressable` accessible roles/names/state. Size hit boxes with `minWidth`/`minHeight` or `hitSlop` where appropriate without overlapping neighbors.
- Use safe-area primitives and keyboard-aware scroll/avoidance appropriate to the installed navigation/Expo version. Test Android navigation bar and iOS home indicator.
- Adapt navigation for tablet/large windows and split-screen rather than relying on phone detection. Ensure hardware keyboard support where relevant.
- Use native platform visual semantics when they matter (e.g. iOS back behavior, Android ripple/back handling).

## Flutter

- Use a themed `ThemeData` / `ColorScheme`, `TextTheme`, and shared widgets; avoid random per-widget `TextStyle` and `EdgeInsets`.
- Choose `LayoutBuilder` or current `MediaQuery.sizeOf`/constraints for adaptive layout; don't classify device by screen orientation or `Platform.isIOS` as a proxy for space.
- Use `SafeArea`; account for view insets/keyboard. At large text scale allow rows to grow and stack.
- Avoid deeply nested giant widgets; break into simpler reusable widgets and preserve state with appropriate keys.
- Test text scale, accessibility semantics, TalkBack/VoiceOver, physical keyboard, desktop pointer, and window resize.

## SwiftUI / Apple platforms

- Prefer system text styles (`.font(.body)`, `.headline`, etc.) and Dynamic Type; never assume a fixed 17pt layout will remain readable at larger sizes.
- Use SwiftUI stacks, grids, layout priority, safe areas and scalable text; avoid absolute coordinates for screen structure.
- Respect iOS/iPadOS size classes, multitasking, keyboard, and window sizing. Use system navigation/pickers/control appearances when possible.
- Test VoiceOver reading order, focus, hit areas, accessibility labels, increased contrast, reduced motion, and dark appearance.
- Apple platforms differ: macOS is pointer/keyboard-first; tvOS and watchOS have specialized focus, target, and density guidance.

## Android / Jetpack Compose

- Use `dp` dimensions, `sp` text, Material theme tokens, `WindowSizeClass` for available window width/height, and adaptive navigation patterns.
- Don't hide content under status/navigation bars; handle insets and IME.
- Use `Modifier.sizeIn(minWidth=48.dp,minHeight=48.dp)` or component behavior to ensure accessible hit targets for custom controls.
- Prefer Material components with built-in semantics; label custom clickable icons and include state descriptions when needed.
- Avoid fixed height text rows that break at large `fontScale`. Test TalkBack, dark mode, edge-to-edge, back gesture, and foldable states.

## .NET MAUI / WinUI / desktop

- Prefer shared Styles/ResourceDictionary and platform-specific handlers for OS interaction differences.
- Use Grid/FlexLayout and adaptive VisualStates; avoid pixel-perfect absolute positioning.
- Respect Windows text scale, DPI scaling, window resize, keyboard focus and pointer hover; Windows typically supports denser UI than phones without forcing tiny touch controls.
- In MAUI use `SemanticProperties.Description`, heading levels, and screen-reader verification; respect safe areas on mobile.
- Use Fluent/WinUI native control conventions and system navigation patterns when building Windows-native UI.

## Cross-platform anti-patterns

- Using CSS `px` values as a mandated identical number in iOS `pt` and Android `dp`.
- Hardcoding device-model names or viewport orientation to determine layout.
- Disabling OS font scaling to prevent clipped labels.
- Assuming desktop has hover or mobile has no keyboard.
- Rendering two hidden versions of the same content so assistive tech encounters duplicates.
- Mixing platform back gestures, system bars and safe areas without tests.
- Replacing native pickers and modals with inaccessible custom clones solely to match screenshots.

**Sources:** React Native, Flutter, Android Developers, Apple HIG, Microsoft Learn, MDN. See `07-sources.md`.


---

# 06 — Quality Assurance, Performance, and Release Gates

Consistency and bug prevention require executable evidence. This plan is **risk-based**: apply deeper coverage to shared components, authentication, payments, data editing, destructive actions, and screens used across many sizes.

## 1. Definition of done for UI work

- **Functional:** primary task and relevant secondary actions work with keyboard/touch/pointer; async state is correct; no duplicate submit, stale responses, or accidental data loss.
- **Visual:** existing product identity preserved; tokens used consistently; no unnecessary gradients/overlays/shadows; text never overlaps; spacing visually systematic.
- **Adaptive:** no lost functionality at supported widths, text scales, orientations, split-screen, safe areas, and browser zoom; responsive composition is intentional.
- **Accessible:** WCAG 2.2 AA web checks targeted; native semantics follow platforms; keyboard and screen reader paths reviewed; contrast measured; target sizes checked.
- **Resilient:** supports long content, empty/error/slow/offline states, large text, localization, failed network, permissions, and loading placeholders.
- **Performant:** no unbounded re-renders, jank, obvious layout shift, or large asset regressions. Core Web Vitals targeted for web.
- **Proven:** relevant tests run; actual results stated; regression baselines updated only after human review of intended differences.

## 2. Test pyramid

| Level | What to test | Suggested implementation |
|---|---|---|
| Static checks | formatting, lint, types, token usage, imports, CSS mistakes | existing lint/typecheck/build; stylelint/ESLint/tsc as configured |
| Unit | validation, selectors, state machines, data transforms | project's current unit test runner |
| Component | controls, states, accessible names, wrap, variants, focus | Storybook/Testing Library/Compose UI tests/Flutter widget tests as appropriate |
| Integration | form submit, loading/error paths, navigation state, dialogs, filtering | app-specific integration test APIs |
| End-to-end | key user journeys at relevant widths and input modes | Playwright/Cypress/web, Detox/Maestro/native UITest/XCTest/Compose/Flutter integration where installed |
| Visual regression | shared components and top routes in light/dark/compact/wide | Playwright snapshots, Storybook visual tools, native screenshot tests |
| Accessibility manual | keyboard, screen readers, scaling, contrast, motion | VoiceOver/TalkBack/NVDA, device/system settings |
| Real hardware | touch, IME, safe areas, pointer, platform rendering | at least one representative real device per materially different platform |

**Do not introduce a whole testing stack just for a minor CSS fix** if the repository already has suitable tools. When new tooling is truly needed, propose it before dependency changes and keep setup minimal.

## 3. UI regression matrix

Create a lightweight matrix for each top user flow; rerun affected rows on shared component changes.

| Dimension | Coverage |
|---|---|
| Web viewport width | 320, 375/390, 600/768, 1024, 1280/1440, 1920 CSS px as supported |
| Height | Short phone landscape, normal portrait, short desktop window |
| Scale | Browser text 200%; web reflow at 320 CSS-px equivalent (often 400% zoom at 1280 wide); native largest system font |
| Input | Pointer, touch, keyboard only, screen reader; pen/remote where relevant |
| Theme | Light, dark, forced colors/increased contrast where supported |
| Network | Fast, throttled/slow, offline, timeout, HTTP error, partial response |
| Content | None, one, many, very long strings, very large values, RTL where supported |
| State | default, hover, focus, pressed, selected, loading, disabled, validation failure, successful completion |
| Platform | Browsers actually supported + targeted iOS/Android/desktop releases |

Testing the 320px-equivalent behavior is a WCAG reflow conformance scenario for applicable web content, **not a requirement to design every native app for a 320-device-pixel screen**.

## 4. Web performance targets

Use **real-user field data when available**, evaluated at the 75th percentile:

| Metric | Good threshold | Primary action |
|---|---|---|
| Largest Contentful Paint (LCP) | ≤2.5 s | Limit render blocking, prioritize hero media, server/cache optimization |
| Interaction to Next Paint (INP) | ≤200 ms | Break long tasks, avoid re-render storms, debounce expensive work |
| Cumulative Layout Shift (CLS) | ≤0.1 | Define media space, reserve skeleton/layout, avoid late banners/fonts causing reflow |

These are **web** Core Web Vitals thresholds, not universal native performance standards. For native, instrument startup time, frame rendering/jank, memory, dropped frames, and important interactions on target hardware; use existing product budgets.

Other performance checks:
- Stable list keys and virtualization for truly large lists.
- Avoid `layout thrashing` by reading/writing layout repeatedly per frame; animate transforms/opacity when appropriate.
- Lazy-load below-the-fold media but not the primary LCP image by default.
- Prefer responsive images with explicit dimensions; reduce oversized assets and unnecessary animations.
- Ensure network responses arriving out of order cannot overwrite newer UI state.
- Avoid giant fixed skeletons for short content and animated skeletons that consume CPU or harm vestibular comfort.
- Run real profiling before applying speculative micro-optimizations.

## 5. Defect severity and blocking policy

| Severity | Example | Ship decision |
|---|---|---|
| P0 critical | Primary flow unusable; unrecoverable data loss; systemic crash; sensitive info exposure | Must fix before release |
| P1 high | Keyboard trap; unreachable submit at mobile zoom; destructive button falsely triggered; form error unavailable; main screen clipped | Fix before release of affected feature |
| P2 medium | Inconsistent card padding, moderate dashboard wrap defect at one width, noncritical tooltip issue | Fix promptly or track with reason |
| P3 low | Minor optical misalignment, tiny nonfunctional visual variance | Queue/document |

Severity depends on frequency, impact, affected users, and whether a workaround exists; accessibility defects should not be silently downgraded because they don't affect a developer's mouse-only test.

## 6. Sample release gate commands and what they prove

Use commands **actually installed in the repository**:

```bash
# Illustrative only; adapt to package.json / project tooling.
npm run lint
npm run typecheck
npm run test
npm run build
npx playwright test
```

- `lint`: code/style conventions, not visual/accessibility certification.
- `typecheck`: type consistency, not correct interaction.
- `test`: coverage depends on the authored tests.
- `build`: compilation and packaging, not actual user experience.
- Screenshot tests: catch unexpected visual differences but cannot replace manual accessibility tests.
- Axe: catches some classes of accessibility defects, **not** full WCAG conformance.

For native use existing Gradle/Xcode/Flutter/MAUI tooling; never claim the app was tested on iOS just because a cross-platform JS build passed.

## 7. Screenshot review workflow

1. Freeze a predictable test environment: browser/OS/fonts, viewport, DPR, reduced-motion, animations/data mocks.
2. Capture important components in compact, medium, wide and at least one large-text scenario, plus dark mode where supported.
3. Review changed screenshots **by eye**, ideally using image diff. A green CI test is not enough if the approved baseline is wrong.
4. Check geometry: text overlaps, card alignment, padding, dropdown overflow, focus rings, action visibility, scroll clipping.
5. Approve and update baselines only for intentional changes; don't auto-accept all diffs.
6. Run representative user flows after styling to ensure event handling and state remain intact.

Playwright `toHaveScreenshot()` works for stable visual comparisons, but results vary across OS/browsers/font rendering; keep baseline environment consistent.

## 8. UI bug root-cause checklist

**Glitches/flicker:** conditional remounts, hydration mismatch, animation/layout races, missing async cleanup, conflicting framework reactivity, image size changes, CSS transition on layout, cumulative layout shift.

**Mobile overflow:** fixed min widths, `100vw` with scrollbars, flex child missing `min-width:0`, long unbroken token, absolutely positioned toolbar, wide table, sticky footer, iOS keyboard, chart library fixed width.

**Strange spacing:** mixed CSS tokens/utility versions, collapsed margins, component default margin, nested padding, font metrics, global selector leakage, lack of consistent `box-sizing`.

**Inconsistent cards:** multiple local implementations, fixed heights, varied media ratio, padding arbitrary values, controls not aligned to meaningful content.

**Input/validation bugs:** stale server errors, duplicate submit, disabled while still loading indefinitely, focus lost on re-render, masked values not matching actual submitted values, incorrect programmatic labels.

**Accessibility regression:** refactor changed `<button>` to `<div>`, outline removed, modal doesn't restore focus, hidden duplicate content still in accessibility tree, status conveyed by color only.

## 9. Deliverable review template

```markdown
### UI changes
- Scope: [screens/components]; reused [existing components/tokens].
- New/modified design contracts: [states, layout rules, tokens].

### Verified
- Commands run: [exact commands and results].
- Viewports and modes: [actually inspected].
- Interactions: [flows, keyboard, touch, assistive technology actually checked].

### Remaining checks
- Not tested: [platform/device/assistive technology].
- Known deviations/risks: [what, impact, next check].
```

**Sources:** Playwright screenshot comparisons; Google Core Web Vitals; W3C WCAG; Flutter/React Native/Android accessibility docs. See `07-sources.md`.


---

# 07 — Official Sources, Evidence, and Maintenance

**Research/review date:** 2026-11-16. These links favor primary standards bodies, OS/framework maintainers, and established design-system publishers. They are authoritative about **their own platforms**, not universal prescriptions. Numerical dimensions outside official criteria are clearly presented as **skill defaults or heuristics** elsewhere.

## A. Normative web accessibility and recommended techniques

1. **W3C WCAG 2.2** — https://www.w3.org/TR/WCAG22/ — Success criteria and conformance levels for applicable web content; primary baseline used here.
2. **W3C WCAG 2.2 Quick Reference** — https://www.w3.org/WAI/WCAG22/quickref/ — Complete criteria list and technology-neutral techniques; confirm scope/exceptions.
3. **WCAG 2.5.8 Target Size (Minimum)** — https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum — 24×24 CSS-pixel minimum, specified alternatives/exceptions; this is **not** 44×44.
4. **WCAG 1.4.3 Contrast (Minimum)** — https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum — 4.5:1 normal text, 3:1 specified large text, applicable exceptions.
5. **WCAG 1.4.10 Reflow** — https://www.w3.org/WAI/WCAG22/Understanding/reflow — 320 CSS-pixel width equivalent for vertically scrolling content and exceptions for essential two-dimensional layout.
6. **WCAG 1.4.11 Non-text Contrast** — https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast — 3:1 required graphics/UI indicators with exceptions.
7. **WCAG 1.4.12 Text Spacing** — https://www.w3.org/WAI/WCAG22/Understanding/text-spacing — content must survive user-imposed 1.5 line/2 paragraph/0.12 letter/0.16 word spacing; not required authored defaults.
8. **WCAG 2.4.11 Focus Not Obscured (Minimum)** — https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum — focused component not completely hidden by authored content.
9. **WAI-ARIA Authoring Practices Guide** — https://www.w3.org/WAI/ARIA/apg/ — tested reference patterns for custom widget roles and keyboard interactions.
10. **WAI-ARIA keyboard practice** — https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/ — robust focus/keyboard guidance.
11. **WAI-ARIA combobox** — https://www.w3.org/WAI/ARIA/apg/patterns/combobox/ — custom autocomplete behavior and keyboard model.
12. **WAI form validation** — https://www.w3.org/WAI/tutorials/forms/validation/ — accessible errors and server-side validation.
13. **WAI form notifications** — https://www.w3.org/WAI/tutorials/forms/notifications/ — field errors, error summaries, and status feedback.

## B. Platform-specific primary guidance

14. **Apple Human Interface Guidelines** — https://developer.apple.com/design/human-interface-guidelines/ — Apple native patterns, typography, materials, interaction and platform differences.
15. **Apple design principles** — https://developer.apple.com/design/human-interface-guidelines/design-principles/ — consistency, purpose, platform fit, accessibility.
16. **Apple layout** — https://developer.apple.com/design/human-interface-guidelines/layout — safe areas, adaptable layouts, Dynamic Type, window sizes.
17. **Apple accessibility** — https://developer.apple.com/design/human-interface-guidelines/accessibility — font scaling and platform-specific default/minimum control sizes. **Important nuance:** Apple's iOS/iPadOS accessibility reference distinguishes default `44×44pt` and lower minimum `28×28pt` in some contexts; this skill recommends default comfortable targets, not an absolute 44pt legal minimum in every context.
18. **Apple UI Design Dos and Don'ts** — https://developer.apple.com/design/tips/ — prominent 44×44pt touch guideline and legibility guidance.
19. **Android adaptive window size classes** — https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes — compact `<600dp`, medium `600–839dp`, expanded `840–1199dp`, large `1200–1599dp`, extra large `>=1600dp` app-window width.
20. **Android layout and navigation patterns** — https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns — adaptive navigation rail vs bottom navigation, actions and FAB.
21. **Android accessible app Views** — https://developer.android.com/guide/topics/ui/accessibility/views/apps-views — recommended minimum 48×48dp touch target; native accessibility.
22. **Android Compose accessibility codelab** — https://developer.android.com/codelabs/jetpack-compose-accessibility — 48dp clickable regions, semantic labels.
23. **Flutter adaptive/responsive design** — https://docs.flutter.dev/ui/adaptive-responsive — adapting to display size/available input methods.
24. **Flutter adaptive best practices** — https://docs.flutter.dev/ui/adaptive-responsive/best-practices — constraints, platform strengths, avoid device/orientation-based layout decisions.
25. **Flutter accessible UI design** — https://docs.flutter.dev/ui/accessibility/ui-design-and-styling — support OS font scaling, test at large text.
26. **React Native useWindowDimensions** — https://reactnative.dev/docs/usewindowdimensions — updates window dimensions and font scaling dynamically.
27. **Windows UI overview / Fluent controls** — https://learn.microsoft.com/en-us/windows/apps/develop/user-interface — native Windows design, controls, navigation and responsive layout.

## C. Design systems / craftsmanship (guidelines, not law)

28. **U.S. Web Design System tokens** — https://designsystem.digital.gov/design-tokens/ — primitive/style token discipline.
29. **USWDS spacing units** — https://designsystem.digital.gov/design-tokens/spacing-units/ — examples of discrete spacing scales and design-system governance.
30. **USWDS typography and font scaling** — https://designsystem.digital.gov/design-tokens/typesetting/font/ — semantic typescale, relative rem and optical size.
31. **USWDS typography component guidance** — https://designsystem.digital.gov/components/typography/ — whitespace/reading hierarchy examples.
32. **Atlassian spacing foundation** — https://atlassian.design/foundations/spacing/ — 8px-based spacing system; inspiration for systematic spacing, *not a universal mandate*.
33. **Nielsen Norman Group usability heuristics** — https://www.nngroup.com/articles/ten-usability-heuristics/ — status visibility, consistency, error prevention, user control, etc. Heuristics rather than numerical standards.

## D. Responsive CSS, performance, and verification

34. **MDN CSS container queries** — https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries — components responsive to container widths.
35. **MDN viewport units** — https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length — `svh`/`dvh`/`lvh`, browser chrome behavior.
36. **MDN reduced motion** — https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion — media preference and accessible animation.
37. **Google Core Web Vitals** — https://developers.google.com/search/docs/appearance/core-web-vitals — LCP 2.5s, INP 200ms, CLS 0.1, measured in real-world conditions.
38. **Playwright visual comparisons** — https://playwright.dev/docs/test-snapshots — `toHaveScreenshot` and environment-stability caveats.

## E. Codex skills packaging

39. **OpenAI Skills format/documentation** — https://learn.chatgpt.com/docs/build-skills — required `SKILL.md`, name/description, optional references/scripts, repository/user skill discovery and invocation.
40. **OpenAI skill creator example** — https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md — progressive disclosure, focused instructions, validation and avoid documentation bloat.
41. **OpenAI Codex skill creator** — https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md — Codex-specific skill scaffolding and test/eval approach.

## F. Evidence classification for numeric values

| Value / pattern | Classification | Authority / caveat |
|---|---|---|
| 24×24 CSS-px or qualifying exception | Normative WCAG 2.2 AA target-size requirement | Source 3; exceptions matter |
| Web text 4.5:1; large text 3:1 | Normative WCAG 2.2 AA contrast requirement | Sources 1, 4; exceptions matter |
| Non-text UI contrast 3:1 | Normative WCAG 2.2 AA for necessary visual indicators | Source 6; exceptions matter |
| 320 CSS-px reflow-equivalent | Normative WCAG 2.2 AA case with exceptions | Source 5; not a native pixel target |
| 44×44pt preferred iOS touch target | Apple platform design guidance | Sources 17, 18; newer accessibility doc distinguishes default/minimum |
| 48×48dp preferred Android target | Android platform guidance | Sources 21, 22 |
| Android window classes `<600 / 600–839 / ...` | Official Android window classification | Source 19; in Android dp, not CSS px |
| Core Web Vitals LCP/INP/CLS targets | Google defined web performance targets | Source 37; field data preferred |
| 4/8-based spacing, card padding 16–24 | This skill's opinionated design-system defaults | Inspired by 28, 29, 32; not a law |
| Body web 16px, card radii 12–16 | This skill's opinionated defaults | Adapt to brand, optics, content, OS |
| Web breakpoints 600/840/1200/1600 CSS px | This skill's optional starting design map | Inspired by Android classification but **no numeric unit equivalence implied** |
| Content max width 1200–1440 and 60–75ch reading measure | This skill's starting heuristics | Depends on task and typeface; not WCAG rule |

## G. When to revisit these rules

- At each major OS or component-library upgrade, revisit native APIs/behavior and avoid deprecated guidance.
- Before accessibility compliance claims, recheck the latest WCAG and applicable jurisdictional rules; conduct an expert/manual audit.
- If a new brand/theme is introduced, revise semantic tokens but keep contracts/behavior stable.
- If accessibility study, usability testing, or telemetry conflicts with a recommended default, prefer evidence from actual users and document the override.
- For framework-specific APIs, read the **installed version's** documentation, not an example copied from a different major version.


---

# 08 — Implementation Recipes and Safe Examples

These examples are **recipes, not drop-in replacements for an existing framework**. First inspect the repository's versions, tokens, UI library, and state management. Use the samples only when compatible with the project. A code example cannot certify WCAG compliance by itself.

## 1. A resilient responsive web page and card grid

```css
/* Example: requires tokens from assets/web-theme.css or equivalent app tokens. */
.page-shell {
  width: min(100% - 2 * var(--space-4), 80rem);
  margin-inline: auto;
  padding-block: var(--space-6);
}
.page-header {
  display: flex;
  gap: var(--space-4);
  align-items: start;
  justify-content: space-between;
  flex-wrap: wrap;
  margin-block-end: var(--space-6);
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: var(--space-4);
}
.card { min-width: 0; }
.card__body { min-width: 0; }
.card__title { overflow-wrap: anywhere; }
.card__actions { display: flex; flex-wrap: wrap; gap: var(--space-2); }
@media (min-width: 48rem) {
  .page-shell { width: min(100% - 2 * var(--space-6), 80rem); }
}
```

Why: auto-fit keeps a minimum card width while letting content stack; `min(100%,17rem)` prevents a `minmax` track from forcing the page wider than its container; flex wrap avoids clipped toolbars.

## 2. Container-aware card composition

```css
.card-container { container-type: inline-size; }
.profile-card { display: grid; grid-template-columns: 1fr; gap: 1rem; }
.profile-card__media { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }
@container (min-width: 34rem) {
  .profile-card { grid-template-columns: minmax(8rem, 12rem) minmax(0, 1fr); }
  .profile-card__media { height: 100%; }
}
```

Why: the card adapts to *its own allocated width* even if mounted in a desktop sidebar. Ensure content does not become inaccessible when the media/text relationship changes.

## 3. Semantic form field with error

```html
<div class="field">
  <label for="email">Email address</label>
  <input
    id="email"
    name="email"
    type="email"
    autocomplete="email"
    required
    aria-invalid="true"
    aria-describedby="email-help email-error"
  />
  <p id="email-help">We'll send your receipt here.</p>
  <p id="email-error">Enter a valid email address.</p>
</div>
```

**State-dependent requirement:** render `aria-invalid="true"` and the error description only when validation has actually failed; dynamically update `aria-describedby` so it references only existing elements. Server-side validation remains mandatory. Don't suppress browser autofill or paste.

## 4. Visible focus and reduced motion

```css
:where(button, a, input, select, textarea, [tabindex]):focus-visible {
  outline: 2px solid var(--focus-ring, #1d4ed8);
  outline-offset: 3px;
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Use the broad motion override only when the app's animations are non-essential and this doesn't break animation-dependent UI. Prefer targeted alternative transitions for complex products.

## 5. React/TypeScript safe request handling

```tsx
import { useEffect, useState } from 'react';

type Item = { id: string; label: string };
export function SearchResults({ query }: { query: string }) {
  const [data, setData] = useState<Item[]>([]);
  const [status, setStatus] = useState<'idle'|'loading'|'success'|'error'>('idle');

  useEffect(() => {
    const q = query.trim();
    if (!q) { setData([]); setStatus('idle'); return; }
    const controller = new AbortController();
    setStatus('loading');
    fetch(`/api/search?q=${encodeURIComponent(q)}`, { signal: controller.signal })
      .then((r) => { if (!r.ok) throw new Error('Request failed'); return r.json(); })
      .then((rows: Item[]) => { if (!controller.signal.aborted) { setData(rows); setStatus('success'); } })
      .catch(() => { if (!controller.signal.aborted) setStatus('error'); });
    return () => controller.abort();
  }, [query]);

  if (status === 'idle') return <p>Enter a search term.</p>;
  if (status === 'loading') return <p role="status">Searching…</p>;
  if (status === 'error') return <p role="alert">Search failed. Try again.</p>;
  if (data.length === 0) return <p>No results for this search.</p>;
  return <ul>{data.map((item) => <li key={item.id}>{item.label}</li>)}</ul>;
}
```

Why: aborts superseded requests so older results cannot overwrite newer ones. Production apps should match their established fetching/cache patterns; this is a small illustration, not a recommended replacement for their data layer.

## 6. React Native / Expo adaptive width and scalable text

```tsx
import { View, Text, Pressable, useWindowDimensions } from 'react-native';

export function ActionPanel({ onSave }: { onSave: () => void }) {
  const { width } = useWindowDimensions();
  const split = width >= 840; // App-level heuristic in RN layout units; tune to content.
  return (
    <View style={{ flexDirection: split ? 'row' : 'column', gap: 16, padding: 16 }}>
      <View style={{ flex: 1, minWidth: 0 }}>
        <Text accessibilityRole="header" style={{ fontSize: 24, fontWeight: '700' }}>
          Review changes
        </Text>
        <Text style={{ fontSize: 16, lineHeight: 24 }}>Confirm the details before saving.</Text>
      </View>
      <Pressable
        accessibilityRole="button"
        accessibilityLabel="Save changes"
        onPress={onSave}
        style={{ minHeight: 48, minWidth: 48, paddingHorizontal: 16, justifyContent: 'center' }}
      >
        <Text>Save changes</Text>
      </Pressable>
    </View>
  );
}
```

Actual app: use theme tokens, accessibility contrast, `Pressable` pressed/focus states, safe areas, and platform font scaling; consider `fontScale` when a horizontal row would cease to fit.

## 7. Flutter adaptive structure

```dart
LayoutBuilder(
  builder: (context, constraints) {
    final wide = constraints.maxWidth >= 840; // Content heuristic, not device ID.
    final form = const MyForm();
    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: wide
            ? Row(children: [Expanded(child: form), const SizedBox(width: 24), const Expanded(child: ContextPanel())])
            : form,
      ),
    );
  },
)
```

Illustrative only: `MyForm`/`ContextPanel` stand for existing app widgets. In production, manage text scaling, scrolling, keyboard/IME, and state across transitions; prefer `ThemeData` token use to raw `16`.

## 8. Android Compose custom icon target

```kotlin
IconButton(
    onClick = onOpen,
    modifier = Modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp)
) {
    Icon(
        imageVector = Icons.Default.MoreVert,
        contentDescription = "More options"
    )
}
```

Use Material components and their built-in semantics; avoid stacking multiple accessibility announcements. For adaptive top-level navigation, rely on window size classes and current Material adaptive APIs.

## 9. SwiftUI text scaling / touch-friendly control

```swift
VStack(alignment: .leading, spacing: 16) {
    Text("Review changes").font(.title2).fontWeight(.semibold)
    Text("Confirm the details before saving.").font(.body)
    Button("Save changes", action: onSave)
        .frame(minHeight: 44)
}
.padding(16)
```

Do not use `.font(.system(size: 14))` everywhere or fixed-height text containers merely to mirror a web screenshot. Honor Dynamic Type, VoiceOver, safe areas, and iPad window size changes.

## 10. Playwright responsive/overflow and screenshot smoke tests

```ts
import { test, expect } from '@playwright/test';

for (const width of [320, 390, 768, 1280]) {
  test(`main screen fits at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 800 });
    await page.goto('/'); // adapt to representative route and authenticated test data
    await expect(page.locator('main')).toBeVisible();
    const overflow = await page.evaluate(() =>
      document.documentElement.scrollWidth > document.documentElement.clientWidth + 1
    );
    expect(overflow).toBe(false); // scope exceptions carefully (wide table may scroll internally)
    await expect(page).toHaveScreenshot(`home-${width}.png`, {
      animations: 'disabled',
    });
  });
}
```

Update for the app's test fixtures, stable fonts/data, browser baseline environment, and proper scope. The 320px test is one reflow smoke test, not a complete WCAG audit. Add keyboard/form/screen-reader tests separately.

## 11. Lightweight review plan template

```markdown
Screen: [route/screen]
Primary task: [one action]
Shared UI: [existing tokens + components]
Compact layout: [content order, nav, actions]
Expanded layout: [grid, sidebar, max widths]
Input modes: [touch, keyboard, pointer, screen reader]
States: [default, empty, loading, error, success]
Accessibility risks: [contrast, labels, focus, hit areas, large text]
Performance risks: [images, async response races, hydration, animations]
Verification: [exact test commands + viewport/device matrix]
```

## 12. Code-review self-check

Ask: Would a user understand where to act? Is every spacing choice explainable by a token and relationship? Is the component usable without hover? Does it work with large fonts and long text? Does the screen change structure instead of shrinking? Does focus survive modals and dynamic updates? Are failures recoverable? Did the actual tests run? What evidence would convince a skeptical reviewer that the change won't break on phone, tablet, and desktop?


---

# 09 — Component Sizing and Spacing Matrix

**Use this matrix only when the project has no established component system.** These are **suggested logical design-system values for a comfortable-density UI**, not WCAG mandates or direct equivalents across CSS px, iOS pt, Android dp, Flutter logical px, and Windows effective px. When using web values, assume 1 design-system unit maps to a CSS px at the default browser root size; keep typography in `rem` so zoom/text preferences work. Map roles to OS-native defaults for native apps.

## A. Component defaults

| Component / role | Suggested visual size (logical units) | Inside padding / gap | Radius / border | Responsive and interaction rule |
|---|---|---|---|---|
| Page horizontal gutter | 16 compact, 24 medium, 32–40 wide | — | — | Add platform safe-area insets; never squeeze essential content |
| Major section spacing | 24 compact, 32–48 wide | — | — | Keep headings closer to own content than previous section |
| Grid gap | 12–16 compact, 16–24 wide | — | — | Reflow card columns by min card width |
| Default card | auto height, content-led | 16 compact, 20–24 wide | 12–16 radius; thin border or subtle elevation | No fixed content height; allow wraps |
| Compact card/list card | auto height | 12–16 | 8–12 radius | Same semantic content in short form |
| KPI metric card | auto height; metric 28–32 text | 16–24; 8–12 vertical | match card | 1-column on narrow; 2-up only if metrics remain legible |
| Interactive card | content-led; large hit region | 16–24 | match card | Only whole-card activation for single action; avoid nested clickables |
| Primary button | visual height about 44–48 | 12–20 horizontal; icon gap 8 | 6–10 | Web touch hit region at least 44×44 preferred; native guidance prevails |
| Secondary/outline button | same as primary | 12–20 | same family | Muted appearance, identical keyboard semantics |
| Compact icon button | visual icon 18–24 | Expand hit box | 6–10 | Web hit region 44×44 preferred, iOS common 44pt, Android 48dp |
| Text field/select | min-height 44–48 | 12–16 horizontal, adaptable vertical | 6–10; discernible border | Label visible; errors below; dynamic type can increase height |
| Textarea | min-height 96–128 | 12–16 | same as input | Grow/scroll without hiding text or action |
| Input label | 14–16 web font | 4–8 gap to input | — | Visible even when input populated |
| Field hint/error | 13–14 web font | 4–8 after input | — | Never color only; readable contrast; programmatic association |
| Form field vertical separation | — | 16–24 | — | Error text can grow without overlapping next field |
| Checkbox/radio row | content-led | 8–12 icon-to-label, >=8 between groups | OS-native | Whole associated label/row clickable where semantically safe |
| Switch setting row | content-led | 12–16 vertical | OS-native | Label+description wrap; control stays reachable |
| Chip/tag | content-led | 6–12 horizontal, 4–8 vertical | product-specific | Interactive chip hit region independent from chip decoration |
| Badge/status | compact content-led | 4–8 horizontal, 2–4 vertical | 4–999 | Status only when meaningful; text + color/icon |
| Avatar | 32 compact, 40 default, 48 large | — | circle/shape style | Name still readable/accessibly available |
| List row | 48–72 comfortable, may grow | 12–16 vertical, 16 horizontal | none or grouped | Wrap text; don't fix height under large text |
| Tab strip | content-led; touch hit >= platform guidance | 12–16 horizontal | indicator 2–3px | Underline current/selected; keyboard APG where custom |
| Top app bar/header | content-led; often 56–72 | 16–24 | subtle separator optional | Account for safe area and 200% text; avoid fixed title height |
| Bottom navigation | OS-native / layout-aware | system-defined | OS-native | Phone only if appropriate; adapt to rail/sidebar on wide windows |
| Navigation rail | app/platform-defined | OS-native | — | Provide names/accessible labels; not just icons on large screen |
| Sidebar | width by content, often 240–280 web px | 12–20 | — | Collapsible where needed, min main content preserved |
| Modal/dialog | max-width 480–640 web px for standard form | 20–24 | 12–20 | Max-height fits visible viewport; actions reachable with keyboard/IME |
| Popover/menu | min-content, max width governed by content/viewport | 8–12 | 8–12 | Reposition to avoid clipping; Escape/focus restore |
| Tooltip | max width about 240–320 web px | 8–12 | 6–8 | Supplemental only, keyboard/pointer support |
| Toast/snackbar | content-led, readable not tiny | 12–16 | 8–12 | Never obscure mobile bottom actions; optional close/undo |
| Data table row | content-led; often 44–56 web | 12–16 cells | row separators | Allow multi-line content; large text; mobile alternative |
| Data table header | content-led | 12–16 | — | Clear sort and scope; visible/announced |
| Empty state | content-led | 16–24 | — | Title, guidance, relevant CTA; no mandatory big illustration |
| Skeleton | matches final layout dimensions | matches component | matches component | Prevent CLS, no excessive shimmer |
| Chart module | enough height for readable labels, commonly 240–360 web | 16–24 | card as applicable | Reduce ticks/rearrange legend; accessible data alternative |
| Thumbnail/media | set ratio 1:1, 4:3, 16:9, or project ratio | — | inherit container | Reserve space; crop only when non-essential |
| Breadcrumb | content-led | 8 between segments | — | Wrap or collapse context without losing wayfinding |
| Search field | 44–48 min height | 12–16 | same as input | Clear, label, loading/no-result states |
| Segmented control | OS-native / touch appropriate | 8–12 | native | Don't overcrowd options on narrow view |
| Accordion row | content-led, comfortable >=44–48 for touch | 12–16 | project style | Button role/expanded semantics; all content reachable |
| Floating action button | Android/OS-native conventions | native | OS-native | Only for contextually dominant action; avoid blocking content |

## B. Typography roles by interface density (web starter)

| Role | Comfortable | Compact desktop (where justified) | Must still support |
|---|---:|---:|---|
| Body | 16px / 1.5 | 14–16px / 1.4–1.5 | 200% text, wrapping, no lost function |
| Small metadata | 14px / 1.4 | 13–14px / 1.4 | Sufficient contrast; noncritical only |
| Card title | 18–20px | 16–18px | 2+ lines possible |
| Section title | 24px | 20–24px | Clear hierarchy |
| Page title | 28–36px | 24–32px | Responsive, no fixed line clamp |
| Metric | 28–32px | 24–30px | Units/labels, long values |

Native designs should use their own platform text styles and scale settings rather than copying this entire web table.

## C. Content-aware card sizing examples

- For a 360px viewport with 16px gutters and a 16px gap, available inner width is 328px. A single card with 16px internal padding yields about 296px content width. **One card per row** is usually right unless cards are exceptionally simple.
- At a 768px viewport with 24px gutters, available width is 720px. Two cards with a 16px gap give about `(720−16)/2 = 352px` each, typically suitable for small content cards.
- At a 1280px viewport with 32px gutters, max content width about 1216px. Three cards with 24px gaps yield about `(1216−48)/3 ≈ 389px` each. Four give `(1216−72)/4 = 286px`, appropriate only for compact metrics or cards with intentionally short content.
- These are **examples**; `CSS grid auto-fit/minmax` or parent constraints should decide actual layout, not hardcoded device category alone.

## D. Consistency rules to enforce in review

1. Card title to body gap = one consistent token, not variable arbitrary margins between modules.
2. Card body to actions gap = consistently larger than label-to-value gap.
3. All form fields in one section share label style, height class, border/outline, errors, and spacing.
4. One defined horizontal gutter strategy across screen sections; avoid nested accidental double padding.
5. Primary actions align to the task region, not whichever container has extra space.
6. Alignment follows content meaning: decimal/numeric values align for comparison, textual labels align for scanning.
7. Component height is content-led; minimum hit target size is handled separately.
8. Responsive layout changes **structure** and secondary content priority, not readable font size reductions.
9. Tables and charts remain usable by keyboard and screen reader; offer alternatives when needed.
10. Platform-native system chrome/safe areas override generic visual measurements.

## E. Example design decision record

```markdown
Component: Invoice summary card
Intent: Show total, due date, status, and one primary action.
Mode: comfortable / compact desktop
Tokens: card padding 16 (compact) or 24 (wide), title/body gap 8,
        row gap 12, card gap 16, radius 12, border subtle.
Layout: compact = stacked; wide container >= 34rem = 2 columns.
States: skeleton, no invoice, paid, overdue, loading payment, payment failed.
A11y: status text not only color; action named; all numbers localized;
      focus ring and label contrast tested; 200% text no clipping.
Regression: 320/390/768/1280 CSS-px, dark mode, keyboard, no payment double-submit.
```

**References:** The numerical component recipes are skill defaults derived from the discipline of design systems (USWDS, Atlassian, Apple/Android platform patterns). Their existence does not make them formal W3C/Apple/Google required sizes. See `07-sources.md` for official numerical requirements.

