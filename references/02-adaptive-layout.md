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
