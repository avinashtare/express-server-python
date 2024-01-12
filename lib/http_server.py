from http.server import BaseHTTPRequestHandler, HTTPServer

class MyRequestHandler(BaseHTTPRequestHandler):
    # get request 
    def do_GET(self):
        # Define routes based on the requested path
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, this is the home page!')

    # default server log
    def log_message(self, format, *args):
        # Suppress log messages
        pass

class Server:
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