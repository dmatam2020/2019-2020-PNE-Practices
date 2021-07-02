import http.server
import socketserver
import termcolor
import pathlib
import json

PORT = 8080

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        if self.path == '/':
            contents = read_html_file('./html/index.html')
        elif self.path == '/info/A':
            contents = read_html_file('./html/info/A.html')
        elif self.path == '/info/C':
            contents = read_html_file('./html/info/C.html')
        elif self.path == '/info/G':
            contents = read_html_file('./html/info/G.html')
        elif self.path == '/info/T':
            contents = read_html_file('./html/info/T.html')
        elif self.path.endswith('.html'):
            try:
                contents = read_html_file('./html' + self.path)
            except FileNotFoundError:
                contents = read_html_file('./html/error.html')
        else:
            contents = read_html_file('./html/error.html')

        self.send_response(200)  # -- Status line: OK!

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

        return



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)


    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()