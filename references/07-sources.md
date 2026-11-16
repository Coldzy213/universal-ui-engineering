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
