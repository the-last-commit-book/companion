# audit_api_server.py
# A tiny stand-in for a cloud audit-log service.
#
# In a real investigation this API lives on the mainland, run by the cloud
# provider, and you could not edit it even if you wanted to. That is the whole
# point of Chapter 24: some records live somewhere the suspect cannot reach.
#
# Run it in one terminal:
#     python audit_api_server.py
# Then, in another terminal:
#     python chapter_24_the_mainland_copy.py
#
# It serves two read-only endpoints and requires a bearer token:
#     GET /audit   -> the audit events
#     GET /tokens  -> which token belongs to whom
#
# The standard library includes a working web server. You do not need Flask,
# FastAPI, or any install to stand up a real HTTP endpoint for learning.

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"
READ_TOKEN = "READONLY-EVIDENCE-TOKEN"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


class AuditHandler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        # Every real API checks who is asking before it answers.
        authorization = self.headers.get("Authorization", "")
        if authorization != f"Bearer {READ_TOKEN}":
            self._send(401, {"error": "unauthorized", "detail": "missing or wrong bearer token"})
            return

        if self.path == "/audit":
            self._send(200, load("cloud_audit_log.json"))
        elif self.path == "/tokens":
            self._send(200, load("token_registry.json"))
        else:
            self._send(404, {"error": "not_found", "path": self.path})

    def log_message(self, *args):
        pass  # keep the terminal quiet


def main(host="127.0.0.1", port=8080):
    server = ThreadingHTTPServer((host, port), AuditHandler)
    print(f"Glasshouse audit API listening on http://{host}:{port}")
    print("Endpoints: GET /audit, GET /tokens (Bearer token required). Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
