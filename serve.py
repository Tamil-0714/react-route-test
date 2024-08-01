import http.server
import socketserver
import os

class SPARequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/"):
            self.path = '/index.html'
        return super().do_GET()

# Set the directory you want to serve
web_dir = os.path.join(os.path.dirname(__file__), 'dist')
os.chdir(web_dir)

PORT = 8000
Handler = SPARequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
