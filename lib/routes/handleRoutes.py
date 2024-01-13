from lib.routes.pages import Pages

pages = Pages()

def isNextRouteExist(path,method,routes,index):
    routesList = []
    index = index+1
    while(index<len(routes.routes[method])):
        if routes.routes[method][index].path == path:
            routesList.append(routes)
            break
        index +=1
        
    if (len(routesList) == 0):
        return False
    else:
        return True


class HandleRoutes:
    def HandleGETRequest(self,request,routes):
        for index,route in enumerate(routes.routes["GET"]):
            if request.path == route.path:
                # call to response handler 
                handlerReturn = route.handlers(index,route,route.next)

                # if user send response
                if(handlerReturn == 'stop'):
                    # send a default text page 
                    pages.Send(request,route)
                    return None

                # if user call next response 
                elif(handlerReturn == 'next'):
                    # check next request exist or not 
                    if (not isNextRouteExist(request.path,route.method,routes,index)):
                        pages.default("Next Request Not Exist",request)
                        return None
                # if user forgot to call next response or last respone  
                else:
                    # check next request exist or not 
                    if (not isNextRouteExist(request.path,route.method,routes,index)):
                        pages.default("Add A Response this is last route",request)
                    else:
                        pages.default("Add a respone route",request)
                    return None
        
        # if route not available send 404 
        pages.show404(request)