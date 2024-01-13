from lib.http_server import Server,routes

class express:
    # get request 
    def get(self,path,handlers):
        resData = {"path": path,"method": "GET","handlers": handlers}
        routes.AddNewRoute(resData)
    def post(self,path,handlers):
        resData = {"path": path,"method": "POST","handlers": handlers}
        routes.AddNewRoute(resData)
        
    # express.listen()
    def listen(self, port, *args):
        args_len = len(args)

        if args_len == 0:
            server = Server(port)
        elif args_len == 1 and isinstance(args[0], str):
            server = Server(port, host=args[0])
        elif args_len == 1 and callable(args[0]):
            server = Server(port, listenerHandler=args[0])
        elif args_len == 2 and isinstance(args[0], str) and callable(args[1]):
            server = Server(port, host=args[0], listenerHandler=args[1])
        
        # run server 
        server.start()