# 🎬 Stream Timer Ultimate

A fully browser-based, feature-packed countdown timer built for live streamers. No installation, no server, no dependencies — just open the HTML file and go.

> **100% transparent background.** Drop it into OBS as a Browser Source — no chroma key needed.

---

## ✨ Feature Overview

### ⏱ Timer Modes
| Mode | Description |
|------|-------------|
| ⬇ Countdown | Counts down to zero |
| ⏱ Stopwatch | Counts up from zero |
| 🔄 Loop | Restarts automatically, tracks loop count |
| ⏰ Clock | Shows the current live time |

### 🌍 Timezone Support (Clock Mode)
21 selectable timezones — from 🌺 Hawaii (UTC-12) to 🇳🇿 Auckland (UTC+12), including 🇺🇸 New York, 🇬🇧 London, 🇩🇪 Berlin, 🇯🇵 Japan, 🇦🇺 Sydney and more.

---

## 🎨 Visuals & Design

- **5 Timer Skins** — Default, ⚡ Neon, 🖥️ Retro, ◻ Minimal, 💥 Brutal
- **Custom font color** — pick any color for the timer digits
- **Custom glow** — two glow colors + intensity slider
- **Timer size** — slider from 40px to 300px
- **Drop shadow** — color, blur size, X and Y offset
- **Animated border** — Glow, Pulse, Spin, Dash styles with 2 custom colors
- **Progress bar** — custom gradient colors (start → end)

---

## 🎆 Finish Effects (triggers at 00:00)

🎊 Confetti · 🎉 Fireworks · ⚡ Lightning · 🌀 Tornado · 💥 Explosion · 🪄 Magic · 🌊 Tsunami · 🔮 Matrix · ⚡ Flash · 〰 Waves · ✨ Particles · 🔥 Fire

---

## 🌌 Background Effects (runs while timer is active)

⭐ Stars · 🌈 Aurora · 🔵 Particles · 🌧 Rain · 💜 Pulse Glow · 🌌 Galaxy · 🔥 Flames · ⚡ Plasma · 🌊 Ocean Waves · ❄️ Snow · 💚 Matrix Code · 🌈 Rainbow Shift

All effects have an **intensity slider**.

---

## 🎬 Video & Media

- **Video Playlist** — add multiple MP4/WebM/MOV files, plays through automatically
- **Loop** — repeat the playlist endlessly
- **Shuffle** — randomize playback order
- **Mute toggle** — silence video audio
- **Opacity slider** — blend the video into the background
- **GIF Background** — upload any GIF as a background layer with opacity control
- **Quick toggle button** — visible on screen, no need to open settings

---

## 🎧 Spotify „Now Playing" Widget

Shows current track, artist, album cover and a progress bar in the bottom-left corner. Cover can spin in vinyl style. Adapts to the active skin.

> For automatic track updates, use tools like **Snip** (Windows) alongside the widget.

---

## 📝 News Ticker

A scrolling text banner at the bottom of the screen. Add as many messages as you want (one per line). Adjustable scroll speed. Fully styled per skin.

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `#` | Open / Close settings |
| `P` | Start / Pause timer |
| `R` | Reset timer |
| `V` | Toggle video on / off |
| `N` | Skip to next video in playlist |

---

## 🖥️ OBS Setup

1. In OBS, add a **Browser Source**
2. Check **"Local file"** and select `stream_timer.html`
3. Set width & height to match your canvas (e.g. `1920 × 1080`)
4. Uncheck **"Shutdown source when not visible"**
5. Done — background is transparent out of the box

> **OBS tip:** Right-click the source → **"Interact"** to click buttons inside the timer without switching focus.

---

## 🚀 Usage

```
1. Download stream_timer.html
2. Open it in your browser or add it to OBS as a Browser Source
3. Press # to open settings
4. Configure your timer, effects, skin, and media
5. Press P to start
```

No npm. No build step. No internet required after the first load (Google Fonts loads once).

---

## 📄 License

MIT — free to use, modify and share.
