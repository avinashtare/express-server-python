from lib.routes.pages import Pages

# add new pages 
pages = Pages()

class HandleRoutes:
    def handle_next_handler(self,index,request,routes,method):
        for routeIndex in range(0,len(routes.all_routes[method])):
                currentRoute = routes.all_routes[method][routeIndex]
                route = currentRoute[0]

                if (request.path != route.path):continue
                try:
                    ResponseState = route.AllHandlers[index]("kdjf",route,route.next)
                    if(ResponseState == "end"):
                        pages.Send(request,route)
                        return True
                    elif(ResponseState == "next"):
                        if(index<=currentRoute[1]):
                            self.handle_next_handler(index+1,request,routes,method)
                            return True
                    else:
                        pages.default("Please add next request",request)
                        return True
                except:
                    pages.default("Please add response",request)
                    return True
        return False
    
    def handle_get_request(self,request,routes):
        try:
            if not self.handle_next_handler(0,request,routes,"GET"):
                # if route not available send 404 page
                pages.show404(request)
        except:
            pages.default("Internal Server Error",request,500)
            return None 