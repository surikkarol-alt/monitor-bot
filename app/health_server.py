import json
import os
from http.server import BaseHTTPRequestHandler

from app.health_checks import check_filesystem, check_telegram


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_response(404)
            self.end_headers()
            return

        checks = {}

        fs_ok, fs_msg = check_filesystem()
        checks["filesystem"] = fs_msg

        tg_ok, tg_msg = check_telegram(os.getenv("BOT_TOKEN", ""))
        checks["telegram"] = tg_msg

        overall_ok = fs_ok and tg_ok

        if overall_ok:
            self.send_response(200)
        else:
            self.send_response(500)

        self.send_header("Content-Type", "application/json")
        self.end_headers()

        response = {
            "status": "ok" if overall_ok else "error",
            "checks": checks,
        }

        self.wfile.write(json.dumps(response).encode())
