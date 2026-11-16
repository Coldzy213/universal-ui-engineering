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
