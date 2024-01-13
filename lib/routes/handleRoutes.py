from lib.routes.pages import Pages
from lib.routes.RequestRoute import ReqRoute
import traceback 

# add new pages 
pages = Pages()
class HandleRoutes:
    def handle_next_handler(self,index,request,routes,method):
        RequestData = ReqRoute(method,request)
        requestPath = RequestData.url
        
        for routeIndex in range(0,len(routes.all_routes[method])):
                currentRoute = routes.all_routes[method][routeIndex]
                route = currentRoute[0]

                if (requestPath != (route.path).replace("%20"," ")):continue
                try:
                    ResponseState = route.AllHandlers[index](RequestData,route,route.next)
                    if(ResponseState == "end"):
                        pages.Send(request,route)
                        return True
                    elif(ResponseState == "next"):
                        if(index<currentRoute[1]):
                            self.handle_next_handler(index+1,request,routes,method)
                        else:
                            pages.error(request,f"<------- Thare Is Not Any Next() Response -------> ")
                        return True
                    else:
                        pages.error(request,f"<------- Add A Response Handler Here ------->")
                        return True
                except Exception as error:
                    traceback.print_exc()  # Print the full traceback of error
                    # show error page 
                    pages.error(request,f"Internal Server Error:{error} \n <---- Handle This Error")
                    return True
        
        # send False if there is not any route 
        return False
    
    def handle_get_request(self,request,routes):
        try:
            if not self.handle_next_handler(0,request,routes,"GET"):
                # if route not available send 404 page
                pages.show404(request)
        except:
            pages.default("Internal Server Error",request,500)
            return None 