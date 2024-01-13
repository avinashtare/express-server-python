from http.server import BaseHTTPRequestHandler, HTTPServer
from lib.routes.main import Routes
from lib.routes.handleRoutes import HandleRoutes

# all routes 
routes = Routes()
routesHandler = HandleRoutes()

class MyRequestHandler(BaseHTTPRequestHandler):

    # get request 
    def do_GET(self):
        try:
            routesHandler.handle_get_request(self,routes)
        except:
            pass
       
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        print(self.rfile.read(length).decode("utf-8"))

    # default server log
    def log_message(self, format, *args):
        # Suppress log messages
        pass
    def handle_error(self, request, client_address):
        pass


class Server(MyRequestHandler):
    def __init__(self, port=3000, host="localhost",listenerHandler=None):
        self.port = port
        self.host = host
        self.listenerHandler = self.DefaultListenerHandler if listenerHandler is None else listenerHandler
        
    # default listener
    def DefaultListenerHandler(self,error):
        if(not error):
            print(f"Server Running At http://{self.host}:{self.port}")

    def start(self):
        server_address = (self.host, self.port)
        try:
            httpd = HTTPServer(server_address, MyRequestHandler)
            
            # handle server listen 
            self.listenerHandler(None)

            httpd.serve_forever()
        except Exception as error:
            self.listenerHandler(error)
        except KeyboardInterrupt:
                print('\nServer is shutting down...')
                httpd.server_close()