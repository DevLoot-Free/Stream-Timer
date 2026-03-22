# Stream Timer V2.0.0 🎬

A stream overlay timer that runs as a single HTML file. Transparent background, works directly in OBS as a Browser Source. No install, no setup, just open it and go.

---

## Files

- `stream_timer.html` — the actual timer, goes into OBS
- `remote.html` — remote control page for tablet/phone
- `server.py` — runs on your PC to connect timer and remote

---

## What it can do

**Timer modes**
- Countdown
- Stopwatch (counts up)
- Loop (auto-restarts, shows loop count)
- Clock (shows live time, 21 timezones)

**Visuals**
- 5 skins: Default, Neon, Retro, Minimal, Brutal
- Custom font color, glow color, glow intensity
- Resize the timer with a slider
- Drop shadow with X/Y offset
- Animated border: Glow, Pulse, Spin, Dash
- Custom progress bar with gradient colors

**Finish effects** (play when timer hits 00:00)

Confetti, Fireworks, Lightning, Tornado, Explosion, Magic, Tsunami, Matrix, Flash, Waves, Particles, Fire

**Background effects** (loop while timer runs)

Stars, Aurora, Particles, Rain, Pulse, Galaxy, Flames, Plasma, Ocean, Snow, Matrix, Rainbow — all with intensity slider

**Media**
- Video playlist — add multiple MP4/WebM/MOV files, loops or shuffles automatically
- GIF background with opacity control
- Both have opacity sliders

**Extras**
- Spotify Now Playing widget (manual input, bottom left)
- News ticker at the bottom with custom messages and speed
- DE / EN language toggle in the settings panel

---

## Keyboard shortcuts

| Key | What it does |
|-----|-------------|
| `#` | Open/close settings |
| `P` | Start/pause |
| `R` | Reset |
| `V` | Toggle video on/off |
| `N` | Next video in playlist |

---

## OBS setup

1. Add a Browser Source in OBS
2. Tick "Local file" and pick `stream_timer.html`
3. Set the size to match your canvas (e.g. 1920x1080)
4. Uncheck "Shutdown source when not visible"

Background is already transparent, no chroma key needed. To click things inside the timer without alt-tabbing, right-click the source → Interact.

---

## Remote control (tablet/phone)

Control the timer from your tablet without anything showing up on stream.

**Requirements:** Python 3, same WiFi network on both devices.

**1. Install websockets**
```
pip install websockets
```

**2. Start the server**
```
python server.py
```
Your IP will show up in the console — something like `192.168.x.x`. Everyone's IP is different, use whatever yours says.

**3. Connect the timer**

Open `stream_timer.html` → press `#` → scroll down to Remote Control → paste your IP:
```
ws://YOUR_IP:8765
```

**4. Open the remote on your tablet**

In the browser on your tablet:
```
http://YOUR_IP:8080/remote.html
```
Then enter the WebSocket URL in the field at the top and hit connect.

**Firewall issues?**

If the tablet can't connect, run this in CMD as Administrator:
```
netsh advfirewall firewall add rule name="StreamTimer HTTP" protocol=TCP dir=in localport=8080 action=allow
netsh advfirewall firewall add rule name="StreamTimer WS" protocol=TCP dir=in localport=8765 action=allow
```

**What you can control from the remote:**
- Start, pause, reset
- Set time and start immediately
- Switch mode, skin, finish effect, background effect
- Change label and finish text
- Video on/off, restart, next track
- Live timer display on the tablet

---

## License

MIT

---

## Security

Both `stream_timer.html` and `server.py` have been scanned and are clean.

- VirusTotal: https://www.virustotal.com/gui/file/663fc2dedcde30b98254e0a5ce616acd4f06e9286e5e7e575eb6f02346f54d20
- Hybrid Analysis: https://hybrid-analysis.com/sample/663fc2dedcde30b98254e0a5ce616acd4f06e9286e5e7e575eb6f02346f54d20

The source code is fully open — read every line yourself if you want.
