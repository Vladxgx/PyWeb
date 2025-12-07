from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 80

if __name__ == "__main__":
    print("Web server running on port:", PORT)
    httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    httpd.serve_forever()
