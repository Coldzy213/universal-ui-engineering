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
