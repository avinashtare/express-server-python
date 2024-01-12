from lib.http_server import Server

class express:
    def get(self,path,handlers):
          handlers("req","res","next")
          
    def listen(self,port,*args):
        argsLen = len(args)
        server = None
        if(argsLen == 0):
            server =  Server(port)
        elif(argsLen == 1):
                arg_1 = type(args[0]).__name__
                if(arg_1== 'str'):
                      server =  Server(port,host=args[0])
                elif(arg_1 == "function"):
                          server =  Server(port,listenerHandler=args[0])
        elif(argsLen==2):
                arg_1 = type(args[0]).__name__
                arg_2 = type(args[1]).__name__

                if(arg_1 == "str" and arg_2 == "function"):
                    server =  Server(port,host=args[0],listenerHandler=args[1])
        
        server.start()