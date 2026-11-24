<div align="center">

<img src="assets/hero.svg" width="100%" alt="systemAdmin-ai — нативные macOS-приложения на Swift"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3400&pause=900&color=63E6D2&center=true&vCenter=true&width=720&lines=macOS+%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F+%D0%BD%D0%B0+Swift;%D1%87%D1%91%D0%BB%D0%BA%D0%B0+%D0%BA%D0%B0%D0%BA+%D1%86%D0%B5%D0%BD%D1%82%D1%80+%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F;%D0%B2%D1%81%D1%91+%D0%B2+%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%BE%D0%BC+%D0%BA%D0%BE%D0%B4%D0%B5;%D0%BF%D0%BE%D0%B8%D1%81%D0%BA+%D0%B4%D0%B5%D1%88%D1%91%D0%B2%D1%8B%D1%85+%D1%81%D0%BA%D0%B8%D0%BD%D0%BE%D0%B2+CS2" alt="чем занимаюсь"/>

<br/>

[![Просмотры профиля](https://komarev.com/ghpvc/?username=systemAdmin-ai&label=profile+views&color=63e6d2&style=flat-square)](https://github.com/systemAdmin-ai)

[English](README.md) · **Русский**

</div>

## Привет 👋

Пишу **нативные приложения для macOS на Swift** — без Electron и обёрток, только AppKit и SwiftUI, работающие с системой напрямую.

Главный проект — **[NotchDeck](#-notchdeck--центр-управления-в-чёлке)**: центр управления, который живёт прямо в чёлке MacBook. Я его разработал и продолжаю поддерживать. Параллельно делаю **[SkinRadar](#-skinradar--дешёвые-скины-cs2-в-разработке)** — поиск дешёвых скинов CS2 по торговым площадкам.

<table>
<tr>
<td width="50%"><img src="assets/card-notchdeck.svg" width="100%" alt="NotchDeck"/></td>
<td width="50%"><img src="assets/card-skinradar.svg" width="100%" alt="SkinRadar"/></td>
</tr>
</table>

---

## ⚓ NotchDeck — центр управления в чёлке

Полоска чёрного пластика в верхней части MacBook обычно простаивает. NotchDeck превращает её в живую панель: системные метрики, медиа, быстрые заметки и запись экрана — в одном клике или наведении.

| | |
|---|---|
| **Что это** | Нативное приложение на SwiftUI для Apple Silicon, macOS 14+ |
| **Статус** | Активно поддерживается — вышел 2.2.0, релизы выходят часто |
| **Лицензия** | MIT |
| **Внутри** | Swift, SwiftUI, AppKit, IOKit, ScreenCaptureKit, Homebrew cask, локальная подпись сборок |

**Что умеет**

- 📊 Системные метрики в реальном времени, без засорения строки меню
- 🎛 Ярлыки приложений, профили задач и восемь неоновых тем
- ⌨️ **Режим клавиатуры** — привычки Windows-клавиатуры на Mac (левый Ctrl → Command, переключение Alt+Shift)
- 🎥 Запись экрана и снимки в собственную папку
- 🎵 Компактный now-playing, быстрые заметки, подсветка при зарядке, пульс низкого заряда, настраиваемые оповещения
- 🌗 Светлые, тёмные и автоматические материалы, подстраивающиеся под обои

```bash
brew install --cask systemAdmin-ai/notchdeck/notchdeck
```

К каждому релизу прилагается `SHA256SUMS.txt` и подписанная контрольная сумма — сборку можно проверить через `shasum -a 256 -c SHA256SUMS.txt` или `gh attestation verify`.

<div align="center">

[![Скачать DMG](https://img.shields.io/badge/Скачать-DMG-3ddc97?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/systemAdmin-ai/NotchDeck/releases/latest/download/NotchDeck.dmg)
[![Сайт](https://img.shields.io/badge/Сайт-0b0e14?style=for-the-badge&logo=gitbook&logoColor=63e6d2)](https://systemAdmin-ai.github.io/NotchDeck/)
[![Демо](https://img.shields.io/badge/Интерактивное_демо-0b0e14?style=for-the-badge&logo=html5&logoColor=63e6d2)](https://systemAdmin-ai.github.io/NotchDeck/demo.html)
[![Исходники](https://img.shields.io/badge/Исходники-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/systemAdmin-ai/NotchDeck)

</div>

---

## 🛰 SkinRadar — дешёвые скины CS2, в разработке

Скины CS2 торгуются сразу на пяти площадках, и разница в цене между ними — как раз то, на чём зарабатывают. SkinRadar ставит их рядом: один запрос, все предложения, самое дешёвое сверху.

- 🔎 Один поиск по пяти площадкам CS2
- 💸 Разброс цен, комиссии площадок и самое выгодное предложение по скину
- 📉 Список отслеживания и история цен по нужным скинам
- 🔐 **Пароль Steam не запрашивается** — пароли пользователей хранятся только как хеш PBKDF2-SHA256

Сайт и личный кабинет уже работают, поисковое ядро переписывается. Это ранняя версия — шероховатости возможны.

<div align="center">

[![Открыть SkinRadar](https://img.shields.io/badge/Открыть-SkinRadar-7c5cff?style=for-the-badge&logo=target&logoColor=white)](https://systemAdmin-ai.github.io/skinradar-site/)
[![Статус](https://img.shields.io/badge/статус-в_разработке-a78bfa?style=for-the-badge)](https://systemAdmin-ai.github.io/skinradar-site/)

</div>

---

## 🧰 Инструменты

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

## 📊 В цифрах

<div align="center">

<table>
<tr>
<td width="50%"><img src="assets/stats.svg" width="100%" alt="Статистика GitHub"/></td>
<td width="50%"><img src="assets/langs.svg" width="100%" alt="Языки"/></td>
</tr>
</table>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=systemAdmin-ai&hide_border=true&background=0A0F18&stroke=1B2740&ring=63E6D2&fire=7C5CFF&currStreakLabel=63E6D2&sideLabels=A9BCD8&dates=6D7F9C&currStreakNum=E8F1FF&sideNums=E8F1FF" width="620" alt="серия коммитов"/>

</div>

> Карточки слева собирает [`scripts/gen_stats.py`](scripts/gen_stats.py) из GitHub API, обновление — каждую ночь. Никаких сторонних картинок-сервисов.

---

## 🐍 Вклады

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/systemAdmin-ai/systemAdmin-ai/output/github-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/systemAdmin-ai/systemAdmin-ai/output/github-snake.svg"/>
  <img src="https://raw.githubusercontent.com/systemAdmin-ai/systemAdmin-ai/output/github-snake.svg" width="100%" alt="змейка вкладов"/>
</picture>

</div>

---

<div align="center">

<img src="assets/footer.svg" width="100%" alt="подвал"/>

<sub>Делать вещи, которые ощущаются нативными. И выпускать их в открытом коде.</sub>

</div>
