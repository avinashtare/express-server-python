class ResRoute:
    def __init__(self,data):
        self.path = data["path"]
        self.method = data["method"]
        self.AllHandlers = [data["handlers"]]
        self.text = ''
        self.headers= []


    def setHeader(self,key,value):
        self.headers.append((key,value))

    def send(self,text = ""):
        self.text = text
        return "end"
    def next(self):
        return "next"
    
    def addHandlers(self,newHandler):
        self.AllHandlers.append(newHandler)