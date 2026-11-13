
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from datetime import datetime, timezone
from html import escape
import json
import os

ESTUDIANTE = os.getenv("ESTUDIANTE_NOMBRE", "Laura Garcia")
PORT = int(os.getenv("PORT", "8080"))


def audit(event, path, status, client):
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "method": "GET",
        "path": path,
        "status": status,
        "client": client
    }
    print("[AUDIT] " + json.dumps(record), flush=True)


class CustomHandler(BaseHTTPRequestHandler):

    def respond(self, status, content, content_type="text/plain"):
        body = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        client = self.client_address[0]

        if path in ("/", "/index.html"):
            audit("PAGE_ACCESS", path, 200, client)

            html = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Servidor Web DMZ</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background: #f4f4f9;
                        margin: 40px;
                    }}
                    .container {{
                        max-width: 720px;
                        margin: auto;
                        background: white;
                        padding: 30px;
                        border-radius: 12px;
                        box-shadow: 0 2px 8px #ddd;
                    }}
                    h1 {{ color: #2c3e50; }}
                    .status {{
                        color: #27ae60;
                        font-weight: bold;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Servidor Objetivo DMZ</h1>
                    <p>Estado:
                       <span class="status">ONLINE / ACTIVO</span>
                    </p>
                    <h2>Servidor DMZ Activo -
                        Laboratorio de {escape(ESTUDIANTE)}
                    </h2>
                    <p>
                        Unidad 2 - Seguridad en redes
                        y aplicaciones web.
                    </p>
                    <p>
                        Servidor utilizado para simulaciones
                        controladas y análisis de logs.
                    </p>
                </div>
            </body>
            </html>
            """
            self.respond(200, html, "text/html")

        elif path == "/health":
            audit("HEALTH_CHECK", path, 200, client)
            self.respond(
                200,
                json.dumps({"status": "ok"}),
                "application/json"
            )

        elif path == "/login":
            audit("AUTH_ENDPOINT_ACCESS", path, 401, client)
            self.respond(401, "Autenticacion requerida")

        else:
            audit("UNKNOWN_PATH", path, 404, client)
            self.respond(404, "Recurso no encontrado")


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", PORT), CustomHandler)
    print(
        f"Servidor DMZ iniciado en puerto {PORT}",
        flush=True
    )
    server.serve_forever()
