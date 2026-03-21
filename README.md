# 🎬 Stream Timer

A lightweight, fully browser-based countdown timer built for live streamers. No installation, no dependencies — just open the HTML file and go.

> Transparent background out of the box. Drop it straight into OBS as a Browser Source — no chroma key needed.

---

## ✨ Features

- **Countdown & Stopwatch** — switch between counting down or up
- **Custom Label** — display text above the timer like *"STREAM STARTING SOON"*
- **Custom Finish Text** — show a message when the timer hits 00:00
- **🎨 Timer Color & Glow** — fully customizable timer color, glow color and glow intensity
- **✍️ Custom Font** — load any Google Font live (e.g. Orbitron, Audiowide, Press Start 2P)
- **🔊 Finish Sound** — play your own audio file (MP3/WAV/OGG) when the timer ends
- **Progress Bar** — with fully customizable gradient colors
- **5 Finish Effects** — trigger an animation when the timer ends
- **6 Background Effects** — subtle animated effects while the timer runs
- **Video Background** — upload any MP4/WebM/MOV as a background
- **💬 Twitch Chat Overlay** — show live chat messages next to your timer (no token needed)
- **📱 Remote Control** — control the timer from your phone via QR code
- **100% Transparent** — works natively in OBS without any green screen setup
- **No install, no server** — single `.html` file, runs in any browser

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `#` | Open / Close Settings |
| `P` | Start / Pause |
| `R` | Reset |

---

## 🎆 Finish Effects

| Effect | Description |
|--------|-------------|
| 🎊 Confetti | Colorful confetti rains down the screen |
| ⚡ Flash | Screen flashes white multiple times |
| 🌊 Waves | Expanding ripple waves from the center |
| ✨ Particles | Burst of colorful particles from the center |
| 🔥 Fire | Fire simulation rises from the bottom |

---

## 🌌 Background Effects

| Effect | Description |
|--------|-------------|
| ⭐ Stars | Softly twinkling stars |
| 🫧 Bubbles | Floating translucent bubbles |
| 💚 Matrix | Falling katakana characters |
| 🌈 Neon | Flowing neon wave lines |
| ❄️ Snow | Falling snowflakes |

---

## 💬 Twitch Chat Overlay

1. Open Settings (`#`)
2. Enter your Twitch channel name
3. Click **Verbinden**
4. Enable **Chat-Overlay anzeigen**

Chat messages appear on the right side of the screen and fade out automatically. No API token or authentication required — anonymous read-only connection.

---

## 📱 Remote Control

Control the timer from your phone without touching your PC:

1. Open Settings (`#`)
2. Scroll to **Remote Control** → click **QR-Code anzeigen**
3. Scan the QR code with your phone
4. A controller page opens with Play/Pause, Reset and Stop buttons

> **Note:** Both devices must use the same browser (e.g. Chrome) for the BroadcastChannel to work.

---

## 🎨 Timer Color & Glow

- **Timer Color** — pick any color for the digits
- **Glow Color** — set the color of the glow/bloom effect
- **Glow Strength** — slider from 0 (off) to 10 (intense)

---

## ✍️ Custom Font

Load any font from [Google Fonts](https://fonts.google.com):

1. Open Settings (`#`)
2. Enter the exact font name (e.g. `Orbitron`, `Audiowide`, `Press Start 2P`)
3. Choose whether it applies to the timer digits, the label, or both
4. Click **Vorschau** — the font loads live

---

## 🔊 Finish Sound

1. Open Settings (`#`)
2. Click the audio upload area under **Sound bei Finish**
3. Select a `.mp3`, `.wav` or `.ogg` file
4. Use the **Test** button to preview, adjust volume with the slider

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
3. Press # to open settings
4. Press P to start
```

No npm, no build step, no internet required after the first load.

---

## 📄 License

MIT — free to use, modify and share.

---

## 🤝 Part of [DevLoot-Free](https://github.com/DevLoot-Free)

A collection of free, open-source tools for developers and streamers.
