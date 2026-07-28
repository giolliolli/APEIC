import http.server
import socketserver
import os
import sys

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent caching for development ease
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server():
    # Force working directory to script location
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    handler = MyHandler
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"==================================================", flush=True)
        print(f" APEIC Local Dev Server running at:", flush=True)
        print(f" http://localhost:{PORT}/", flush=True)
        print(f"==================================================", flush=True)
        print(f"Press Ctrl+C to stop.", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...", flush=True)
            sys.exit(0)

if __name__ == "__main__":
    run_server()
