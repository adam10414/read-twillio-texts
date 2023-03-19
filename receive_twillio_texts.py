# A _quick_ and _dirty_ script to post the body of a message from Twillio.
# Simple documentation to get you started: https://pythonbasics.org/webserver/
# Thank you https://gist.github.com/hawkins/36b7d781d8fa5277d4cb29b6906abe57
# Python doc: https://docs.python.org/3/library/http.server.html#module-http.server

from http.server import BaseHTTPRequestHandler, HTTPServer

# 0.0.0.0 makes this reachable via internet.
# For local testing use 'localhost'
host_name = "0.0.0.0"
server_port = 42069


class Server(BaseHTTPRequestHandler):

    def do_POST(self):
        print("hello")
        content_length = int(self.headers['Content-Length'])
        # post_data comes in as bytesarray, so we decode to utf8 string.
        post_data = self.rfile.read(content_length).decode('utf8')
        self._set_headers()

        # quick and dirty parsing to pull the message body.
        parsed_post_data = post_data.split("&")
        parsed_post_dict = {}
        for kv in parsed_post_data:
            key_value = kv.split("=")
            key = key_value[0]
            try:
                val = key_value[1]
            except IndexError:
                val = ""

            parsed_post_dict[key] = val

        # The "Body" key:value contains the message.
        print(parsed_post_dict["Body"])
        # To see the entire payload print(parsed_post_body_dict)

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


twillio_message_server = HTTPServer((host_name, server_port), Server)
print("server started...")

try:
    twillio_message_server.serve_forever()
except KeyboardInterrupt:
    pass

twillio_message_server.server_close()
print("server stopped...")