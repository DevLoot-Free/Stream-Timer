import asyncio
import json
import websockets
import socket
import os
import threading

clients = set()
timer_clients = set()
remote_clients = set()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "127.0.0.1"
    finally:
        s.close()

async def handler(websocket):
    global clients, timer_clients, remote_clients
    clients.add(websocket)
    client_ip = websocket.remote_address[0]
    is_timer = False
    print(f"[+] Verbunden: {client_ip} ({len(clients)} Clients)")

    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                msg_type = data.get('type', '')
                cmd = data.get('cmd', '')

                if msg_type == 'state':
                    if not is_timer:
                        is_timer = True
                        timer_clients.add(websocket)
                        remote_clients.discard(websocket)
                        print(f"[~] {client_ip} -> TIMER")
                    dead = set()
                    for rc in remote_clients:
                        try:
                            await rc.send(message)
                        except:
                            dead.add(rc)
                    remote_clients -= dead

                elif cmd:
                    if not is_timer and websocket not in remote_clients:
                        remote_clients.add(websocket)
                        print(f"[~] {client_ip} -> REMOTE")
                    print(f"[CMD] {cmd} von {client_ip}")
                    dead = set()
                    for tc in timer_clients:
                        try:
                            await tc.send(message)
                        except:
                            dead.add(tc)
                    timer_clients -= dead

            except json.JSONDecodeError:
                print(f"[WARN] Ungueltige Nachricht von {client_ip}")

    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        clients.discard(websocket)
        timer_clients.discard(websocket)
        remote_clients.discard(websocket)
        print(f"[-] Getrennt: {client_ip} ({len(clients)} Clients)")

def start_http_server(port, directory):
    import http.server

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)
        def log_message(self, format, *args):
            print(f"[HTTP] {args[0]} {args[1]}")

    httpd = http.server.HTTPServer(('0.0.0.0', port), Handler)
    print(f"[HTTP] Port {port} bereit")
    httpd.serve_forever()

async def main():
    ws_port = 8765
    http_port = 8080
    local_ip = get_local_ip()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    http_thread = threading.Thread(
        target=start_http_server,
        args=(http_port, script_dir),
        daemon=True
    )
    http_thread.start()

    print("=" * 54)
    print("  Stream Timer Remote Control Server")
    print("=" * 54)
    print(f"")
    print(f"  1) stream_timer.html im Browser oeffnen")
    print(f"     Panel (#) > Remote Control > URL eingeben:")
    print(f"     ws://{local_ip}:{ws_port}")
    print(f"")
    print(f"  2) Tablet/Handy Browser oeffnen:")
    print(f"     http://{local_ip}:{http_port}/remote.html")
    print(f"     WebSocket URL: ws://{local_ip}:{ws_port}")
    print(f"")
    print(f"  Beide muessen im selben WLAN sein!")
    print(f"")
    print("=" * 54)
    print("  Strg+C zum Beenden")
    print("=" * 54)

    async with websockets.serve(handler, '0.0.0.0', ws_port, logger=None):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer gestoppt.")
