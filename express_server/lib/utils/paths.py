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