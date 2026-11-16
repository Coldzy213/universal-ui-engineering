#!/usr/bin/env python3
"""Validate sample token syntax and primary text/control contrast (stdlib only).

This is a limited static contrast smoke test, not a WCAG audit or native-platform test.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKENS = ROOT / "assets" / "design-tokens.json"


def luminance(hexcolor):
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", hexcolor):
        raise ValueError(f"Expected #RRGGBB: {hexcolor!r}")
    rgb = [int(hexcolor[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in rgb]
    return sum(a * b for a, b in zip(linear, [0.2126, 0.7152, 0.0722]))


def ratio(a, b):
    x, y = sorted([luminance(a), luminance(b)], reverse=True)
    return (x + 0.05) / (y + 0.05)


def get(group, key):
    return group[key]["$value"]


def main():
    data = json.loads(TOKENS.read_text(encoding="utf-8"))
    failures = []
    for theme in ("light", "dark"):
        c = data["color"][theme]
        checks = [
            ("primary text/surface", "textPrimary", "surface", 4.5),
            ("secondary text/surface", "textSecondary", "surface", 4.5),
            ("primary text/canvas", "textPrimary", "canvas", 4.5),
            ("primary action label", "onAction", "action", 4.5),
            ("hover action label", "onAction", "actionHover", 4.5),
            ("input border/surface", "borderStrong", "surface", 3.0),
            ("focus ring/surface", "focus", "surface", 3.0),
            ("danger text/surface", "dangerText", "surface", 4.5),
            ("success text/surface", "successText", "surface", 4.5),
            ("warning text/surface", "warningText", "surface", 4.5),
        ]
        for label, foreground, background, min_ratio in checks:
            result = ratio(get(c, foreground), get(c, background))
            ok = result >= min_ratio
            print(f"{theme:5} {label:28} {result:5.2f}:1  target {min_ratio:.1f}  {'PASS' if ok else 'FAIL'}")
            if not ok:
                failures.append((theme, label, result, min_ratio))
    if failures:
        print(f"Failed {len(failures)} contrast tests; fix starter palette.", file=sys.stderr)
        return 1
    print("Sample token smoke test passed. This does not certify full accessibility.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
