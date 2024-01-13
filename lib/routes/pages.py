import datetime
class Attributes:
    def setHeader(self,request,headers=[]):
        isContentTypeAvailable = False
        for (key,value) in headers:
            request.send_header(key, value)
            if(key.lower() == "content-type"): isContentTypeAvailable = True
        
        if(not isContentTypeAvailable): request.send_header('Content-Type', 'text/html')

        # end headers 
        request.end_headers()

    # add text response to user 
    def addText(self,text,request):
            
            request.wfile.write(text.encode("utf-8"))


attributes = Attributes()

class Pages:
    def Send(self,request,route):
        request.send_response(200)
        attributes.setHeader(request,route.headers)
        attributes.addText(route.text,request)

        
    def default(slef,text,request,port=200):
        request.send_response(port)
        attributes.setHeader(request)
        attributes.addText(text,request)

    def show404(slef,request):
        request.send_response(400)
        attributes.setHeader(request)
        attributes.addText('<h2 align="center">404 Not Found !</h2>',request)

    def error(slef,request,error):
        request.send_response(5000)
        attributes.setHeader(request)
        attributes.addText(f"""<h2 style="color: red;text-align: center;">{error}</h2""",request)