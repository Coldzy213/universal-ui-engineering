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
