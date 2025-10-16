"""
Simple test handler for Vercel
"""
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head><title>Test</title></head>
        <body>
            <h1>🎉 IT WORKS!</h1>
            <p>If you see this, Vercel is working!</p>
        </body>
        </html>
        """
        
        self.wfile.write(html.encode())
        return
