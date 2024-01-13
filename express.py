from lib.http_server import Server,routes
from lib.utils.express import ServerListenerHandler

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
        ServerListenerHandler(self, port, *args,Server=Server)