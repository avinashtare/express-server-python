from datetime import datetime, timezone
import os
from ..constants import file_types

# < -- make path simple example: 1: c://programming 2: ./index.php output:-c://programming/index.php -- >
def path_normalizer(filepath):
     if (not os.path.splitdrive(filepath)[0]):
            base_path = os.getcwd()
            return os.path.normpath(os.path.join(base_path,filepath))


# < -- it's reutrn content type of paths that available in file types -- >
def get_content_info_by_extension(extension):
    for FileCategory in file_types:
        for ext in file_types[FileCategory]:
                if ext == extension:
                    return ((file_types[FileCategory][ext],FileCategory))
    return (None,None)

# < -- Find Content Type From File Path -- >
def find_content_type(path,path_info):
    extension = path
    if path_info == "filename":
            extension = os.path.splitext(path)[1]
      
    elif path_info == "extention":
         if not str(extension).startswith("."): extension = "."+extension
    try:
        return get_content_info_by_extension(extension)
    except:
        return (None,None)

# handle cookie options
def keyExist(list,key):
    try:
        return list[key]
    except:
        return False



def CalcuateGMT(sec):
    # Get the current time in GMT
    current_time_gmt = datetime.utcfromtimestamp(sec).replace(tzinfo=timezone.utc)

    # Format the datetime object as a string
    formatted_time = current_time_gmt.strftime("%a, %d %b %Y %H:%M:%S GMT")
    return formatted_time

def GetCookieOptions(options):
    optionsStr = ""
    preOptions={
        "path": keyExist(options,"path"),
        "domain": keyExist(options,"domain"),
        "expires": keyExist(options,"expires"),
        "secure": keyExist(options,"secure"),
        "httpOnly": keyExist(options,"httpOnly"),
        "sameSite": keyExist(options,"sameSite")
    }    
    
    # calcuate expires
    if type(preOptions["expires"]) == int or type(preOptions["expires"]) == float:
        gmt_time = CalcuateGMT(preOptions["expires"])
        optionsStr += f'Expires={gmt_time};'
        
    # check domain
    if preOptions["domain"]:
        optionsStr += f'Domain={preOptions["domain"]};'
    
    # check path
    if preOptions["path"]:
        optionsStr += f'Path={preOptions["path"]};'
    
    #check same site
    sameSite = preOptions["sameSite"]
    if type(sameSite) == str and (sameSite in  "Lax" or sameSite in "Strict" or sameSite in "None"):
        optionsStr += f"SameSite={sameSite};"
        
    # check secure bool value
    if preOptions["secure"]:
        optionsStr += f"Secure;"
        
    # check httpOnly bool value
    if preOptions["httpOnly"]:
        optionsStr += f"HttpOnly;"
 
    return optionsStr

# < -- URL Macing Functions -- >
# convert /about/asdfasdfs////////////dasfsd/asdfasdf/dfasdfasdf/// --> /about/asdfasdfs/dasfsd/asdfasdf/dfasdfasdf
def normalize_path(path):
    normalizePath = path
    try:
        while True:
            if normalizePath.find("//") > 0:
                normalizePath = normalizePath.replace("//", "/")
            else:
                if len(normalizePath) > 1 and normalizePath[-1] == "/":
                    normalizePath = normalizePath[:len(normalizePath) - 1]
                break
    except:
        normalizePath = path
        pass
    return normalizePath

# < -- split path into / -- >
def split_url(url):
    url = url.split("/")
    return url

# < -- match paths like /name /name or /name/home or /name/home -- >
def matchBasePath(req,route):
    for i,p in enumerate(route):
        if(len(req)>i and p == req[i]):
            pass
        else:
            if(p[0] ==  ":" or p[0] ==  "*"):
                return {"index": i,"pattern": p[0]}
            break
    return {"index": None,"pattern": None}


# < -- find params -- >
def findParmas(req,route):
    # all params appended here 
    Match_parmas = {}
    
    # match paths like about/name == about/name 
    basePath = matchBasePath(req,route)
    
    # if path not exist return False
    if basePath["index"] == None:
        return False

    # find only slugs 
    routeIndex = basePath["index"]
    nextReq = req[routeIndex:]
    nextRoute = route[routeIndex:]
    # length of slugs 
    nextReq_len = len(nextReq)
    nextRoute_len = len(nextRoute)
    
    # this is for *
    forward = 0
    if nextRoute_len <= nextReq_len:
        for i in range(0,nextRoute_len):          
            req_param = nextReq[i+forward]
            route_pattern = nextRoute[i]

            if route_pattern.startswith(":"):
                params_key = route_pattern[1:]
                Match_parmas[params_key] = req_param
                
                
            elif route_pattern == "*":
                if (len(nextReq[i:])) >= (len(nextRoute[i:])):
                    forward += len(nextReq[i:])-len(nextRoute[i:])                
            else:
                if req_param != route_pattern:
                    Match_parmas = {}
                    return False

                    
            if(i==nextRoute_len-1):
                if (len(nextReq[i+forward:]) != len(nextRoute[i:]) and not route_pattern.startswith("*")):
                        Match_parmas = {}
                        return False                
    else:
        Match_parmas = {}
        return False
    
    return Match_parmas
