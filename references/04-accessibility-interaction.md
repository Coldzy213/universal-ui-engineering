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
