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
