from lib.routes.ResponseRoute import ResRoute

class Routes:
    def __init__(self):
        self.routes = {}
    
    def AddNewRoute(self, resData):
        try:
            # Check if the method key exists, and create an empty list if not
            self.routes[resData["method"]]
        except KeyError:
            self.routes[resData["method"]] = []

        # Append a new ResRoute instance to the method
        self.routes[resData["method"]].append(ResRoute(resData))