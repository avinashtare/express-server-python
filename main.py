from express import express

app = express()

myglobaldata = 0
def nextHandle1(req,res,next):
    global myglobaldata
    print(myglobaldata)
    myglobaldata += 1
    return next()
    
def nextHandle2(req,res,next):
    res.data = "This is response from \n"
    return next()

def lasthandler(req,res,next):
    return res.send(res.data)

app.get("/",nextHandle1)
app.get("/",nextHandle2)
app.get("/",lasthandler)
# app.get("/",nextHandle)

app.get("/a",nextHandle1)
app.get("/a",lasthandler)


app.listen(3000,"localhost")