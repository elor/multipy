from http.server import BaseHTTPRequestHandler, HTTPServer
from multipy_common import get_data, serialize


def compute_result():
    return serialize(get_data())


class RequestHandler(BaseHTTPRequestHandler):

    # GET method
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Call the function to get the result
        result = compute_result()

        # Send the response message
        self.wfile.write(result.encode())
        return


def serve(host='127.0.0.1', port=8000):
    print(f'Serving on {host}:{port}')
    server = HTTPServer((host, port), RequestHandler)

    server.serve_forever()
