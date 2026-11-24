#!/usr/bin/env python3
"""Генерирует assets/stats.svg и assets/langs.svg для профиля systemAdmin-ai.

Данные берутся из GitHub API (REST + GraphQL), поэтому карточки всегда
актуальны и не зависят от сторонних сервисов вроде github-readme-stats.

Запуск:  GITHUB_TOKEN=... python3 scripts/gen_stats.py
Локально: python3 scripts/gen_stats.py  (возьмёт токен из `gh auth token`)
"""

from __future__ import annotations

import json
import os
import ssl
import subprocess
import sys
import urllib.request
from pathlib import Path

LOGIN = os.environ.get("PROFILE_LOGIN", "systemAdmin-ai")
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

BG = "#0a0f18"
BORDER = "#1b2740"
TEXT = "#a9bcd8"
DIM = "#6d7f9c"
BRIGHT = "#e8f1ff"
GREEN = "#3ddc97"
CYAN = "#63e6d2"
VIOLET = "#7c5cff"
PALETTE = [CYAN, VIOLET, GREEN, "#f2b84b", "#ff7a9c", "#4da3ff", "#9fb2d0"]

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"


def token() -> str:
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t
    try:
        return subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    except Exception:
        sys.exit("Нет токена GitHub: задайте GITHUB_TOKEN")


def ssl_context() -> ssl.SSLContext:
    """macOS/python.org сборки не всегда знают системные корневые сертификаты."""
    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:  # noqa: BLE001
        return ssl.create_default_context()


CTX = ssl_context()


def api(path: str, tok: str):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={"Authorization": f"bearer {tok}", "Accept": "application/vnd.github+json",
                 "User-Agent": "profile-readme-generator"},
    )
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        return json.load(r)


def graphql(query: str, tok: str, variables: dict | None = None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql", data=body,
        headers={"Authorization": f"bearer {tok}", "Content-Type": "application/json",
                 "User-Agent": "profile-readme-generator"},
    )
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        return json.load(r)


def collect(tok: str) -> dict:
    user = api(f"/users/{LOGIN}", tok)
    repos = api(f"/users/{LOGIN}/repos?per_page=100&type=owner", tok)
    own = [r for r in repos if not r["fork"]]

    stars = sum(r.get("stargazers_count", 0) for r in own)
    forks = sum(r["forks_count"] for r in own)

    langs: dict[str, int] = {}
    for r in own:
        try:
            for name, size in api(r["languages_url"].replace("https://api.github.com", ""), tok).items():
                langs[name] = langs.get(name, 0) + size
        except Exception as exc:  # noqa: BLE001
            print(f"  ! языки {r['name']}: {exc}", file=sys.stderr)

    payload = graphql(
        """query($login:String!){ user(login:$login){
             contributionsCollection{
               totalCommitContributions totalPullRequestContributions
               totalIssueContributions totalRepositoriesWithContributedCommits
             }
             repositories(first:100, ownerAffiliations:OWNER, privacy:PUBLIC){ totalCount }
           }}""",
        tok,
        {"login": LOGIN},
    )
    if "data" not in payload:
        sys.exit(f"GraphQL error: {json.dumps(payload, ensure_ascii=False)[:400]}")
    gql = payload["data"]["user"]
    cc = gql["contributionsCollection"]

    return {
        "repos": gql["repositories"]["totalCount"],
        "stars": stars,
        "forks": forks,
        "followers": user["followers"],
        "commits": cc["totalCommitContributions"],
        "prs": cc["totalPullRequestContributions"],
        "issues": cc["totalIssueContributions"],
        "active": cc["totalRepositoriesWithContributedCommits"],
        "langs": dict(sorted(langs.items(), key=lambda kv: -kv[1])),
    }


def human(n: int) -> str:
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def stats_svg(d: dict) -> str:
    cells = [
        ("PUBLIC REPOS", str(d["repos"]), CYAN),
        ("STARS EARNED", str(d["stars"]), GREEN),
        ("COMMITS · 12 MO", str(d["commits"]), VIOLET),
        ("PULL REQUESTS", str(d["prs"]), CYAN),
        ("REPOS TOUCHED", str(d["active"]), GREEN),
        ("FOLLOWERS", str(d["followers"]), VIOLET),
    ]
    out = []
    for i, (label, value, color) in enumerate(cells):
        col, row = i % 3, i // 3
        x, y = 34 + col * 190, 128 + row * 92
        out.append(f"""
    <g transform="translate({x} {y})"><g style="animation:fade .9s ease forwards {0.12 + i * 0.1:.2f}s">
      <rect x="0" y="0" width="168" height="72" rx="14" fill="#0c1422" stroke="#1a2438" stroke-width="1"/>
      <rect x="0" y="0" width="4" height="72" rx="2" fill="{color}" opacity="0.85"/>
      <text x="20" y="28" font-family="{MONO}" font-size="10" letter-spacing="1.4" fill="{DIM}">{label}</text>
      <text x="20" y="58" font-family="{MONO}" font-size="26" font-weight="700" fill="{BRIGHT}">{value}</text>
    </g></g>""")

    return f"""<svg width="620" height="330" viewBox="0 0 620 330" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="GitHub stats for {LOGIN}">
  <title>GitHub stats for {LOGIN}</title>
  <defs>
    <linearGradient id="sbg" x1="0" y1="0" x2="620" y2="330" gradientUnits="userSpaceOnUse">
      <stop stop-color="{BG}"/><stop offset="1" stop-color="#070a12"/>
    </linearGradient>
    <linearGradient id="sneon" x1="0" y1="0" x2="620" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{GREEN}"/><stop offset="0.5" stop-color="{CYAN}"/><stop offset="1" stop-color="{VIOLET}"/>
    </linearGradient>
    <clipPath id="sclip"><rect x="1" y="1" width="618" height="328" rx="22"/></clipPath>
    <style>
      @keyframes fade {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
      .run {{ stroke-dasharray:280 1500; animation:run 7.5s linear infinite; }}
      @keyframes run {{ 0% {{ stroke-dashoffset:1780; }} 100% {{ stroke-dashoffset:0; }} }}
      .dot {{ animation:dot 2.6s ease-in-out infinite; }}
      @keyframes dot {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:.3; }} }}
      @media (prefers-reduced-motion: reduce) {{ .run,.dot {{ animation:none; }} }}
    </style>
  </defs>
  <g clip-path="url(#sclip)">
    <rect width="620" height="330" fill="url(#sbg)"/>
    <text x="34" y="52" font-family="{MONO}" font-size="12" letter-spacing="2.6" fill="{DIM}">BY THE NUMBERS</text>
    <circle class="dot" cx="586" cy="47" r="3.4" fill="{GREEN}"/>
    <text x="34" y="92" font-family="{SANS}" font-size="25" font-weight="700" fill="{BRIGHT}">Building in public, one release at a time</text>
    <text x="34" y="112" font-family="{MONO}" font-size="11.5" fill="{DIM}">auto-updated from the GitHub API · {LOGIN}</text>
    {''.join(out)}
    <rect x="1" y="1" width="618" height="328" rx="22" fill="none" stroke="{BORDER}" stroke-width="1.3"/>
    <rect class="run" x="1" y="1" width="618" height="328" rx="22" fill="none" stroke="url(#sneon)" stroke-width="1.6"/>
  </g>
</svg>
"""


def langs_svg(d: dict) -> str:
    langs = list(d["langs"].items())[:6]
    total = sum(d["langs"].values()) or 1
    rows = []
    for i, (name, size) in enumerate(langs):
        pct = size / total * 100
        y = 138 + i * 30
        color = PALETTE[i % len(PALETTE)]
        w = max(4.0, 396 * pct / 100)
        rows.append(f"""
    <g>
      <text x="34" y="{y}" font-family="{MONO}" font-size="12.5" fill="{TEXT}">{name}</text>
      <rect x="140" y="{y - 10}" width="396" height="9" rx="4.5" fill="#111a2a"/>
      <rect x="140" y="{y - 10}" width="{w:.1f}" height="9" rx="4.5" fill="{color}" opacity="0.9"
            style="transform-origin:140px {y-5}px; animation:grow .9s ease forwards {0.1 + i * 0.09:.2f}s; transform:scaleX(0)"/>
      <text x="586" y="{y}" text-anchor="end" font-family="{MONO}" font-size="11.5" fill="{DIM}">{pct:.1f}%</text>
    </g>""")

    return f"""<svg width="620" height="330" viewBox="0 0 620 330" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Languages used by {LOGIN}">
  <title>Languages used by {LOGIN}</title>
  <defs>
    <linearGradient id="lbg" x1="0" y1="0" x2="620" y2="330" gradientUnits="userSpaceOnUse">
      <stop stop-color="#080d15"/><stop offset="1" stop-color="#070a12"/>
    </linearGradient>
    <linearGradient id="lneon" x1="0" y1="0" x2="620" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="{VIOLET}"/><stop offset="0.5" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}"/>
    </linearGradient>
    <clipPath id="lclip"><rect x="1" y="1" width="618" height="328" rx="22"/></clipPath>
    <style>
      @keyframes grow {{ from {{ transform:scaleX(0); }} to {{ transform:scaleX(1); }} }}
      .run {{ stroke-dasharray:240 1500; animation:run 8.5s linear infinite; }}
      @keyframes run {{ 0% {{ stroke-dashoffset:1740; }} 100% {{ stroke-dashoffset:0; }} }}
      @media (prefers-reduced-motion: reduce) {{ .run {{ animation:none; }} }}
    </style>
  </defs>
  <g clip-path="url(#lclip)">
    <rect width="620" height="330" fill="url(#lbg)"/>
    <text x="34" y="52" font-family="{MONO}" font-size="12" letter-spacing="2.6" fill="{DIM}">LANGUAGES BY CODE</text>
    <text x="34" y="92" font-family="{SANS}" font-size="25" font-weight="700" fill="{BRIGHT}">Swift first, then whatever ships it</text>
    <text x="34" y="112" font-family="{MONO}" font-size="11.5" fill="{DIM}">bytes of code across public repositories</text>
    {''.join(rows)}
    <rect x="1" y="1" width="618" height="328" rx="22" fill="none" stroke="{BORDER}" stroke-width="1.3"/>
    <rect class="run" x="1" y="1" width="618" height="328" rx="22" fill="none" stroke="url(#lneon)" stroke-width="1.6"/>
  </g>
</svg>
"""


def main() -> None:
    tok = token()
    data = collect(tok)
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "stats.svg").write_text(stats_svg(data), encoding="utf-8")
    (ASSETS / "langs.svg").write_text(langs_svg(data), encoding="utf-8")
    print(json.dumps({k: v for k, v in data.items() if k != "langs"}, ensure_ascii=False))
    print("langs:", ", ".join(f"{k} {human(v)}" for k, v in list(data["langs"].items())[:6]))


if __name__ == "__main__":
    main()
