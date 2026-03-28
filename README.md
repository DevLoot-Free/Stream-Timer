# Stream Timer 2.0.1

**v2.0.1** — Browser-based stream overlay timer. Transparent background, OBS-ready, no install needed.

---

## What's new in 2.0.1

- 🎯 **"Until Time" mode** — set a target time like 18:00 and the timer counts down to it automatically
- 📡 **Remote Control** — control everything from your tablet or phone over local WiFi
- 🎧 **Spotify Now Playing widget** — show current track on stream
- 📝 **News ticker** — scrolling messages at the bottom
- 🇩🇪 🇬🇧 **DE/EN language toggle** in settings panel
- 🎬 **Video playlist** — multiple videos with loop, shuffle, mute
- 🎞 **GIF background** support
- ✨ **Animated border** styles (Glow, Pulse, Spin, Dash)
- 💥 **5 skins** — Default, Neon, Retro, Minimal, Brutal
- 🔥 **13 finish effects** + **13 background effects**

---

## Files

| File | Description |
|------|-------------|
| `stream_timer.html` | Main timer — goes into OBS as Browser Source |
| `remote.html` | Remote control UI for tablet/phone |
| `server.py` | WebSocket + HTTP server for remote control |

---

## Timer Modes

| Mode | Description |
|------|-------------|
| ⬇ Countdown | Counts down to zero |
| ⏱ Stopwatch | Counts up from zero |
| 🔄 Loop | Auto-restarts, shows loop count |
| ⏰ Clock | Shows current live time (21 timezones) |
| 🎯 Until Time | Counts down to a specific time e.g. 18:00 |

---

## Visuals

- 5 skins: Default, Neon, Retro, Minimal, Brutal
- Custom font color + glow (2 colors, intensity slider)
- Timer size slider (40px – 300px)
- Drop shadow (color, blur, X/Y offset)
- Animated border (Glow, Pulse, Spin, Dash) with 2 custom colors
- Progress bar with custom gradient

---

## Finish Effects (at 00:00)

🎊 Confetti · 🎉 Fireworks · ⚡ Lightning · 🌀 Tornado · 💥 Explosion · 🪄 Magic · 🌊 Tsunami · 🔮 Matrix · ⚡ Flash · 〰 Waves · ✨ Particles · 🔥 Fire

## Background Effects

⭐ Stars · 🌈 Aurora · 🔵 Particles · 🌧 Rain · 💜 Pulse · 🌌 Galaxy · 🔥 Flames · ⚡ Plasma · 🌊 Ocean · ❄️ Snow · 💚 Matrix · 🌈 Rainbow

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `#` | Open / close settings |
| `P` | Start / pause |
| `R` | Reset |
| `V` | Toggle video on/off |
| `N` | Next video in playlist |

---

## OBS Setup

1. Add a **Browser Source** in OBS
2. Tick **"Local file"** → select `stream_timer.html`
3. Set resolution to match your canvas (e.g. 1920×1080)
4. Uncheck **"Shutdown source when not visible"**

Background is transparent out of the box — no chroma key needed. To click things without switching focus: right-click the source → **Interact**.

---

## Remote Control

Control everything from your tablet without anything showing on stream.

**Requirements:** Python 3 · same WiFi network

### Setup

**1. Install dependency**
```
pip install websockets
```

**2. Start the server**
```
python server.py
```
Your IP(s) will be listed in the console. Use the one that starts with `192.168.x.x`.

> Everyone's IP is different — use the one shown in your console, not from any example.

**3. Connect the timer**

Open `stream_timer.html` → press `#` → scroll to **Remote Control** → enter:
```
ws://YOUR_IP:8765
```

**4. Open the remote on your tablet**

In Firefox on your tablet:
```
http://YOUR_IP:8080/remote.html
```
The WebSocket URL is filled in automatically — just tap **Verbinden**.

> Use **Firefox** on the tablet. Chrome blocks unencrypted WebSocket connections from HTTP pages.

**Firewall fix (if tablet can't connect)**

Run in CMD as Administrator:
```
netsh advfirewall firewall add rule name="StreamTimer HTTP" protocol=TCP dir=in localport=8080 action=allow
netsh advfirewall firewall add rule name="StreamTimer WS" protocol=TCP dir=in localport=8765 action=allow
```

### What the remote controls

- Start / Pause / Reset / Toggle
- Set time + start immediately
- Switch mode, skin, finish effect, background effect
- Change label and finish text
- Spotify widget (track, artist, cover, spin, show/hide)
- Ticker (messages, speed, show/hide)
- Video on/off, restart, next track
- Live timer display on tablet

---

## Security

Scanned and clean:

- VirusTotal: https://www.virustotal.com/gui/file/663fc2dedcde30b98254e0a5ce616acd4f06e9286e5e7e575eb6f02346f54d20
- Hybrid Analysis: https://hybrid-analysis.com/sample/663fc2dedcde30b98254e0a5ce616acd4f06e9286e5e7e575eb6f02346f54d20

Source code is fully open — read every line yourself.

---

## Changelog

### v2.0.1
- Added "Until Time" countdown mode
- Fixed remote control WebSocket connection issues
- Fixed HTTP server stability
- Auto-fill WebSocket URL on remote page
- Removed all code comments

### v2.0.0
- Remote control system (WebSocket + HTTP server)
- Spotify Now Playing widget
- News ticker
- DE/EN language toggle
- Video playlist with loop/shuffle
- GIF background support
- Animated border effects
- 5 timer skins
- Timer size, glow, shadow customization
- 4 additional timer modes (Stopwatch, Loop, Clock, Until Time)
- 13 finish effects
- 13 background effects

### v1.0.0
- Initial release

---

## License

MIT — free to use, modify and share.
