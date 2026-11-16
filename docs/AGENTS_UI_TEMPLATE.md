# UI Engineering Rules — Project `AGENTS.md` Snippet

For tasks involving user interfaces, component implementation, responsiveness, accessibility, visual consistency, typography, spacing, design tokens, forms, cards, tables, navigation, or UI regressions:

1. Invoke the `universal-ui-engineering` skill (`$universal-ui-engineering`) when it is available. The skill can be installed globally in the user's `~/.agents/skills/universal-ui-engineering/` folder or in this repository at `.agents/skills/universal-ui-engineering/`. Read only the relevant reference files for the task.
2. Preserve project-specific brand, current design-system tokens, functionality, business logic, routes, and framework versions. Use the skill's suggested measurements only where the project has no established rule.
3. Inspect existing components and check narrow/medium/wide layouts before modifying UI; include accessible interactive states and error/empty/loading states when appropriate.
4. Apply WCAG 2.2 AA requirements where applicable to web experiences and platform-native guidance for iOS/Android/desktop. Do not treat CSS px, iOS pt, Android dp/sp, or Flutter logical pixels as interchangeable.
5. Test or reason explicitly about text scaling, keyboard/focus behavior, touch target sizes, responsive reflow, slow network behavior, safe areas, and layout shifts. Run the project-specific automated checks available.
6. Report precisely which checks were actually executed, what passed/failed, what was untested, and any remaining risks. Never claim complete accessibility certification from static tooling alone.

If the skill is not available, consult the standalone guidance in `docs/UNIVERSAL_UI_UX_ENGINEERING_STANDARDS.md` **only if that document is present in this project**. Do not silently invent a replacement design system.
