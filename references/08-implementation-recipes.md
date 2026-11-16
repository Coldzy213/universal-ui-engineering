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
