from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver
import threading


class ThreadedHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    """Веб-сервер із підтримкою багатопоточності."""
    pass


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        """Обробка GET-запиту."""
        self.send_response(200)  # Код відповіді 200 OK
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        # Відповідь клієнту
        response = f"<html><body><h1>Привіт! Ви звернулися до {self.path}</h1></body></html>"
        self.wfile.write(response.encode("utf-8"))
        print(f"[INFO] Оброблено запит: {self.path}")


if __name__ == "__main__":
    host = "localhost"
    port = 8080

    server = ThreadedHTTPServer((host, port), CustomHandler)
    print(f"Сервер запущено на {host}:{port}")

    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nЗупинка сервера...")
        server.shutdown()
        server.server_close()
