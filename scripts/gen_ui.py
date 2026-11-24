#!/usr/bin/env python3
"""Статичная графика профиля: бейджи стека, кнопки-ссылки, печатающийся текст.

Всё рисуется локально, потому что GitHub проксирует внешние картинки через
camo.githubusercontent.com — а он в некоторых сетях подменён DNS и не грузится.
Локальные SVG отдаются с github.com и работают всегда.

Запуск: python3 scripts/gen_ui.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# (файл, подпись, цвет акцента)
BADGES = [
    ("badge-swift.svg", "Swift", "#F05138"),
    ("badge-swiftui.svg", "SwiftUI", "#63E6D2"),
    ("badge-macos.svg", "macOS", "#C8D3E6"),
    ("badge-shell.svg", "Shell", "#4EAA25"),
    ("badge-javascript.svg", "JavaScript", "#F7DF1E"),
    ("badge-cloudflare.svg", "Cloudflare Workers", "#F38020"),
    ("badge-actions.svg", "GitHub Actions", "#2088FF"),
]

# (файл, подпись, фон, текст, рамка, глиф)
BUTTONS = [
    ("btn-download.svg", "DOWNLOAD DMG", "#0F2A22", "#63E6D2", "#2F6F57", "download"),
    ("btn-site.svg", "WEBSITE", "#0D1626", "#CFDCF2", "#24334F", "globe"),
    ("btn-demo.svg", "INTERACTIVE DEMO", "#0D1626", "#CFDCF2", "#24334F", "play"),
    ("btn-source.svg", "SOURCE", "#0D1626", "#CFDCF2", "#24334F", "code"),
    ("btn-skinradar.svg", "OPEN SKINRADAR", "#1A1230", "#C4B5FD", "#4B3A8A", "target"),
]

PHRASES = [
    "macOS apps in Swift and SwiftUI",
    "building the notch control center",
    "shipping it in the open",
    "finding cheaper CS2 skins",
]


def glyph(kind: str, color: str, x: float, y: float) -> str:
    """Маленькая иконка 12x12 с центром в (x, y)."""
    c = color
    if kind == "download":
        return (f'<path d="M{x:.1f} {y-6:.1f} V{y+1:.1f}" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>'
                f'<path d="M{x-3.2:.1f} {y-1.6:.1f} L{x:.1f} {y+1.6:.1f} L{x+3.2:.1f} {y-1.6:.1f}" stroke="{c}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
                f'<path d="M{x-5:.1f} {y+5:.1f} H{x+5:.1f}" stroke="{c}" stroke-width="1.6" stroke-linecap="round"/>')
    if kind == "globe":
        return (f'<circle cx="{x}" cy="{y}" r="5.4" stroke="{c}" stroke-width="1.3" fill="none"/>'
                f'<ellipse cx="{x}" cy="{y}" rx="2.4" ry="5.4" stroke="{c}" stroke-width="1.1" fill="none"/>'
                f'<path d="M{x-5.4:.1f} {y} H{x+5.4:.1f}" stroke="{c}" stroke-width="1.1"/>')
    if kind == "play":
        return f'<path d="M{x-3.6:.1f} {y-5.2:.1f} L{x+4.6:.1f} {y} L{x-3.6:.1f} {y+5.2:.1f} Z" fill="{c}"/>'
    if kind == "code":
        return (f'<path d="M{x-2:.1f} {y-4.4:.1f} L{x-6:.1f} {y} L{x-2:.1f} {y+4.4:.1f}" stroke="{c}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="M{x+2:.1f} {y-4.4:.1f} L{x+6:.1f} {y} L{x+2:.1f} {y+4.4:.1f}" stroke="{c}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    if kind == "target":
        return (f'<circle cx="{x}" cy="{y}" r="5.6" stroke="{c}" stroke-width="1.3" fill="none" opacity="0.9"/>'
                f'<circle cx="{x}" cy="{y}" r="2.6" stroke="{c}" stroke-width="1.2" fill="none" opacity="0.8"/>'
                f'<circle cx="{x}" cy="{y}" r="0.9" fill="{c}"/>')
    return ""


def badge_svg(label: str, accent: str) -> str:
    w = 30 + int(len(label) * 7.0) + 12
    return f"""<svg width="{w}" height="28" viewBox="0 0 {w} 28" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">
  <title>{label}</title>
  <rect x="0.6" y="0.6" width="{w-1.2}" height="26.8" rx="7" fill="#0C1422" stroke="#22304A" stroke-width="1.2"/>
  <circle cx="15" cy="14" r="3.2" fill="{accent}"/>
  <text x="25" y="18.5" font-family="{MONO}" font-size="12" letter-spacing="0.4" fill="#CFDCF2">{label}</text>
</svg>
"""


def button_svg(label: str, bg: str, fg: str, border: str, icon: str) -> str:
    w = 60 + int(len(label) * 9.1)
    return f"""<svg width="{w}" height="40" viewBox="0 0 {w} 40" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label.title()}">
  <title>{label.title()}</title>
  <rect x="0.7" y="0.7" width="{w-1.4}" height="38.6" rx="9" fill="{bg}" stroke="{border}" stroke-width="1.4"/>
  {glyph(icon, fg, 22, 20)}
  <text x="38" y="25" font-family="{MONO}" font-size="12.5" font-weight="600" letter-spacing="1.1" fill="{fg}">{label}</text>
</svg>
"""


def typing_svg() -> str:
    w, h = 720, 46
    char_w = 11.6  # приблизительная ширина символа при font-size 20 в моноширинном
    blocks = []
    clips = []
    for i, text in enumerate(PHRASES):
        end = 24 + len(text) * char_w + 6
        blocks.append(f"""
    <g clip-path="url(#tc{i})">
      <text x="34" y="29" font-family="{MONO}" font-size="20" fill="#CFDCF2">{text}</text>
      <rect x="{end:.1f}" y="12" width="11" height="22" rx="2.5" fill="#63E6D2"/>
    </g>""")
        clips.append(f"""
      <clipPath id="tc{i}"><rect class="grow{i}" x="0" y="0" width="{w}" height="{h}"/></clipPath>""")

    styles = "\n".join(
        f"""      .grow{i} {{ transform-origin: 0 0; animation: t{i} 16s steps(28, end) infinite; }}
      @keyframes t{i} {{ 0% {{ transform: scaleX(0); }} 23% {{ transform: scaleX(1); }} 25% {{ transform: scaleX(0); }} 100% {{ transform: scaleX(0); }} }}"""
        for i in range(len(PHRASES))
    )
    delays = "\n".join(f"      .grow{i} {{ animation-delay: -{i*4}s; }}" for i in range(len(PHRASES)))

    return f"""<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="what I do">
  <title>macOS apps in Swift and SwiftUI</title>
  <defs>
    <style>
{styles}
{delays}
      @media (prefers-reduced-motion: reduce) {{
        .grow0, .grow1, .grow2, .grow3 {{ animation: none; transform: scaleX(1); }}
      }}
    </style>
{''.join(clips)}
  </defs>
  <path d="M14 17 L22 24 L14 31" stroke="#63E6D2" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.85"/>
{''.join(blocks)}
</svg>
"""


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for fname, label, accent in BADGES:
        (ASSETS / fname).write_text(badge_svg(label, accent), encoding="utf-8")
    for fname, label, bg, fg, border, icon in BUTTONS:
        (ASSETS / fname).write_text(button_svg(label, bg, fg, border, icon), encoding="utf-8")
    (ASSETS / "typing.svg").write_text(typing_svg(), encoding="utf-8")
    print(f"готово: {len(BADGES)} бейджей, {len(BUTTONS)} кнопок, typing.svg")


if __name__ == "__main__":
    main()
