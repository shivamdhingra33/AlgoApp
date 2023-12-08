from http.server import HTTPServer, BaseHTTPRequestHandler
from furl import furl
from connect import setKiteAccessToken, isAccessTokenEmpty

HOST = '127.0.0.1'
PORT = 5555

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if isAccessTokenEmpty:
            f = furl(self.path) 
            requestToken = f.args['request_token']
            # print("request_token ---> ", requestToken)
            self.send_response(200)
            self.end_headers()
        
            setKiteAccessToken(requestToken)

class RequestTokenRetrievalServer:
    def __init__(self):
        self.server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    
    def start(self):
        self.server.serve_forever()
    
    def stop(self):
        self.server.shutdown()
