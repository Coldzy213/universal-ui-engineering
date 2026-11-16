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
