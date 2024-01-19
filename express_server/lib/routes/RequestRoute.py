from urllib.parse import urlparse,parse_qs

# < -- user query like js object -- >
class linked_obj():
    def __init__(self, arr) -> None:
        self.__list__ = arr
        for key in arr:
            # < -- set as self -- >
            setattr(self, key, arr[key])
        
    # if key not not find 
    def __getattr__(self, attr):
        return None

class RequestRoute:
    def __init__(self,method,request):
        self.request = request
        self.path = (request.path.replace("%20"," ")).lower()
        self.protocol = request.protocol_version.split("/")[0]
        self.url = self.originalUrl = self.pathname = self.href = self._raw  = urlparse(self.path).path
        # < -- find host and port of server -- >
        (host, port) = self.request.server.server_address
        # < -- set example.com -- >
        self.hostname = host
        # < -- set example.com:port -- >
        self.host = f"http://{host}:{port}"
        self.server_full_url = f"http://{host}:{port}"+self.path
        self.method = method
        # < -- query like ?query=value -- >
        self.query = None
        self._find_query(self.server_full_url)
        # < -- set client ip and port -- >
        self.ip = request.client_address[0]
        self.client_port = request.client_address[1]
        
        self.headers = None
        self.rawHeaders = []
        self._write_row_header(request)

        # this is for /:kjsd like this url 
        self.params = {}
        # post body
        self.body = {}
        # < -- set cookies -- >
        self._set_init_cookie()
    def getCookie(self,key):
        try:
            for cookieKey, value in self.cookies:
                if(cookieKey == key):
                    return value
        except:
            pass
        return None
    
    def _write_row_header(self,request):
        try:
           headers = {key: value for (key,value) in request.headers.items()}
           self.headers = linked_obj(headers)
          
           for key, value in request.headers.items():
               self.rawHeaders.extend([key,value])
        except:
            pass

    def find_qeury(self,query):
        for sotredQuery in self.query:
            if(sotredQuery == query):
                return self.query[sotredQuery]
        return None
    
    def _set_init_cookie(self):
        row_cookies = self.request.headers.get("Cookie")
        
        # set cookies
        cookies_dist = {}
        try:
            if row_cookies:
                for cookie in  row_cookies.split('; '):
                    cookieArr = cookie.split("=")
                    if(len(cookieArr) == 2):
                        cookies_dist[cookieArr[0]] = cookieArr[1]
                    elif(len(cookieArr) == 1):
                        cookies_dist[""] = cookieArr[0]
        except:
            pass 
        # add a cookies object in cookies
        self.cookies = linked_obj(cookies_dist)
        
    # if attribute not exist
    def __getattr__(self, attr):
        return None


    def _find_query(self,url):
        # < -- splice url -- >
        parsed_url = urlparse(url)

        # < -- find all query from request and add key value in dictionary ex:- {key,value} -- >
        query = {key: value[0] for key, value in parse_qs(parsed_url.query).items()}
        self.query = linked_obj(query)