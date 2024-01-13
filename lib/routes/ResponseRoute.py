class ResRoute:
    def __init__(self,data):
        self.path = data["path"]
        self.method = data["method"]
        self.handlers = data["handlers"]
        self.text = ''
        self.headers= []


    def setHeader(self,key,value):
        self.headers.append((key,value))

    def send(self,text):
        self.text = text
        return "stop"
    def next(self):
        return "next"