import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            status = 200
            body = {"status": "ok"}
        elif self.path == "/version":
            status = 200
            body = {"version": os.getenv("APP_VERSION", "dev")}
        else:
            status = 404
            body = {"error": "Not found"}

        response = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8080), Handler)
    print("Listening on http://127.0.0.1:8080", flush=True)
    server.serve_forever()
