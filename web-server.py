from http.server import HTTPServer, BaseHTTPRequestHandler

from queue_writer import *
from queue_reader import *

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        print("get")
        message = queue_read()
        self.wfile.write(str(message))		

    def do_POST(self):
      #  content_length = int(self.headers['Content-Length'])
      #  body = self.rfile.read(content_length)
        self.send_response(200)
      #  self.end_headers()
     #   response = BytesIO()
     #   response.write(b'This is POST request. ')
     #   response.write(b'Received: ')
     #   response.write(body)
     #   self.wfile.write(response.getvalue())
        print("post")
        queue_write()


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
