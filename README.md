<div align="center">

<img src="assets/hero.svg" width="100%" alt="systemAdmin-ai — native macOS apps in Swift"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3400&pause=900&color=63E6D2&center=true&vCenter=true&width=720&lines=macOS+apps+in+Swift+and+SwiftUI;building+the+notch+control+center;shipping+it+in+the+open;finding+cheaper+CS2+skins" alt="what I do"/>

<br/>

[![Profile views](https://komarev.com/ghpvc/?username=systemAdmin-ai&label=profile+views&color=63e6d2&style=flat-square)](https://github.com/systemAdmin-ai)

**English** · [Русский](README.ru.md)

</div>

## Ahoy 👋

I write **native macOS apps in Swift** — no Electron, no wrappers, just AppKit and SwiftUI talking to the system directly.

My main project is **[NotchDeck](#-notchdeck--a-control-center-in-the-notch)** — a neon control center that lives in the MacBook notch. I built it, I ship it, I keep it alive. Right now I'm also building **[SkinRadar](#-skinradar--cheaper-cs2-skins-in-development)**, a search engine that hunts for cheaper CS2 skins across marketplaces.

<table>
<tr>
<td width="50%"><img src="assets/card-notchdeck.svg" width="100%" alt="NotchDeck"/></td>
<td width="50%"><img src="assets/card-skinradar.svg" width="100%" alt="SkinRadar"/></td>
</tr>
</table>

---

## ⚓ NotchDeck — a control center in the notch

The strip of black plastic at the top of a MacBook is dead space. NotchDeck turns it into a live panel: system metrics, media, quick notes, screen recording — one click or one hover away.

| | |
|---|---|
| **What it is** | Native SwiftUI app for Apple Silicon MacBooks, macOS 14+ |
| **Status** | Actively maintained — v2.2.0 is out, releases ship often |
| **License** | MIT |
| **Under the hood** | Swift, SwiftUI, AppKit, IOKit, ScreenCaptureKit, a Homebrew cask, signed local builds |

**What's inside**

- 📊 Live system metrics at a glance, no menu bar clutter
- 🎛 App shortcuts, task profiles and eight neon themes
- ⌨️ **Keyboard mode** — Windows keyboard habits on a Mac keyboard (left Ctrl → Command, Alt+Shift toggle)
- 🎥 Screen recording and screenshots into your own folder
- 🎵 Compact now-playing, quick notes, charging glow, low-battery pulse, configurable alerts
- 🌗 Light, dark and auto materials that follow the wallpaper

```bash
brew install --cask systemAdmin-ai/notchdeck/notchdeck
```

Every release ships `SHA256SUMS.txt` and a signed checksum — the build can be verified with `shasum -a 256 -c SHA256SUMS.txt` or `gh attestation verify`.

<div align="center">

[![Download DMG](https://img.shields.io/badge/Download-DMG-3ddc97?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/systemAdmin-ai/NotchDeck/releases/latest/download/NotchDeck.dmg)
[![Website](https://img.shields.io/badge/Website-0b0e14?style=for-the-badge&logo=gitbook&logoColor=63e6d2)](https://systemAdmin-ai.github.io/NotchDeck/)
[![Demo](https://img.shields.io/badge/Interactive_demo-0b0e14?style=for-the-badge&logo=html5&logoColor=63e6d2)](https://systemAdmin-ai.github.io/NotchDeck/demo.html)
[![Source](https://img.shields.io/badge/Source-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/systemAdmin-ai/NotchDeck)

</div>

---

## 🛰 SkinRadar — cheaper CS2 skins, in development

CS2 skins are traded on five marketplaces at once, and the spread between them is where the money hides. SkinRadar puts them side by side: one query, every listing, the cheapest one on top.

- 🔎 One search across five CS2 marketplaces
- 💸 Price spread, marketplace fees and the cheapest listing per skin
- 📉 Watchlist and price history for the skins you actually trade
- 🔐 **Steam password is never requested** — user passwords are stored only as a PBKDF2-SHA256 hash

Static site and account area are live; the search core is being rebuilt. It's an early preview, expect rough edges.

<div align="center">

[![Open SkinRadar](https://img.shields.io/badge/Open-SkinRadar-7c5cff?style=for-the-badge&logo=target&logoColor=white)](https://systemAdmin-ai.github.io/skinradar-site/)
[![Status](https://img.shields.io/badge/status-in_development-a78bfa?style=for-the-badge)](https://systemAdmin-ai.github.io/skinradar-site/)

</div>

---

## 🧰 Toolbox

<div align="center">

![Swift](https://img.shields.io/badge/Swift-F05138?logo=swift&logoColor=white&style=for-the-badge)
![SwiftUI](https://img.shields.io/badge/SwiftUI-0b0e14?logo=swift&logoColor=63e6d2&style=for-the-badge)
![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white&style=for-the-badge)
![Shell](https://img.shields.io/badge/Shell-4EAA25?logo=gnubash&logoColor=white&style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge)
![Cloudflare Workers](https://img.shields.io/badge/Cloudflare_Workers-F38020?logo=cloudflare&logoColor=white&style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white&style=for-the-badge)

</div>

---

## 📊 By the numbers

<div align="center">

<table>
<tr>
<td width="50%"><img src="assets/stats.svg" width="100%" alt="GitHub stats"/></td>
<td width="50%"><img src="assets/langs.svg" width="100%" alt="Languages"/></td>
</tr>
</table>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=systemAdmin-ai&hide_border=true&background=0A0F18&stroke=1B2740&ring=63E6D2&fire=7C5CFF&currStreakLabel=63E6D2&sideLabels=A9BCD8&dates=6D7F9C&currStreakNum=E8F1FF&sideNums=E8F1FF" width="620" alt="streak"/>

</div>

> Cards on the left are generated from the GitHub API by [`scripts/gen_stats.py`](scripts/gen_stats.py) and refreshed nightly — no third-party image services.

---

## 🐍 Contributions

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/systemAdmin-ai/systemAdmin-ai/output/github-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/systemAdmin-ai/systemAdmin-ai/output/github-snake.svg"/>
  <img src="https://raw.githubusercontent.com/systemAdmin-ai/systemAdmin-ai/output/github-snake.svg" width="100%" alt="contribution snake"/>
</picture>

</div>

---

<div align="center">

<img src="assets/footer.svg" width="100%" alt="footer"/>

<sub>Build things that feel native. Ship them in the open.</sub>

</div>
