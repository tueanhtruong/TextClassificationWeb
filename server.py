import http.server
import socketserver


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html charset=utf-8")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        # content = f"<html><body><h1>{message}</h1></body></html>"
        index = open("index.html", encoding="utf8").read().format(
            Ket_Qua=message)
        # return content.encode("utf8")  # NOTE: must return a bytes object!
        return index.encode("utf8")

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            self.wfile.write(self._html('Ket Qua'))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        stri = self.data_string.decode('utf8')
        param = [st.split("=")[1] for st in stri.split("&")]
        print(self.data_string.decode('utf8'))
        self.wfile.write(self._html("Nothing"))


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)
print("RUn")
# Star the server
my_server.serve_forever()
