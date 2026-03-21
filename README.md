# 🎬 Stream Timer

A lightweight, fully browser-based countdown timer built for live streamers. No installation, no dependencies — just open the HTML file and go.

> Transparent background out of the box. Drop it straight into OBS as a Browser Source — no chroma key needed.

---

## ✨ Features

- **Countdown & Stopwatch** — switch between counting down or up
- **Custom Label** — display text above the timer like *"STREAM STARTING SOON"*
- **Custom Finish Text** — show a message when the timer hits 00:00
- **Progress Bar** — with fully customizable gradient colors
- **5 Finish Effects** — trigger an animation when the timer ends
- **5 Background Effects** — subtle animated effects while the timer runs
- **Video Background** — upload any MP4/WebM/MOV as a background
- **100% Transparent** — works natively in OBS without any green screen setup
- **No install, no server** — single `.html` file, runs in any browser

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `P` | Start / Pause |
| `R` | Reset |
| `#` | Open / Close Settings |

---

## 🎆 Finish Effects

Triggered automatically when the countdown reaches `00:00`:

| Effect | Description |
|--------|-------------|
| 🎊 Confetti | Colorful confetti rains down the screen |
| ⚡ Flash | Screen flashes white multiple times |
| 🌊 Waves | Expanding ripple waves from the center |
| ✨ Particles | Burst of colorful particles from the center |
| 🔥 Fire | Fire simulation rises from the bottom |

---

## 🌌 Background Effects

Subtle animations displayed while the timer is running. Intensity is adjustable via slider:

| Effect | Description |
|--------|-------------|
| ⭐ Stars | Softly twinkling stars |
| 🌈 Aurora | Flowing aurora borealis waves |
| 🔵 Particles | Slowly drifting colored particles |
| 🌧 Rain | Falling rain streaks |
| 💜 Pulse Glow | Expanding glow rings from center |

---

## 🎬 Video Background

Upload a local video file (MP4, WebM or MOV) directly in the settings panel. Control the opacity with a slider and toggle it on or off without removing it.

---

## 🖥️ OBS Setup

1. In OBS, add a new **Browser Source**
2. Check **"Local file"** and select `stream_timer.html`
3. Set width & height to match your canvas (e.g. `1920 x 1080`)
4. Make sure **"Shutdown source when not visible"** is unchecked
5. Done — the background is already transparent

---

## 🚀 Usage

```
1. Download stream_timer.html
2. Open it in your browser
3. Press # to open settings and configure your timer
4. Press P to start
```

No npm, no build step, no internet required after the first load (Google Fonts loads once).

---

## 📄 License

MIT — free to use, modify and share.
