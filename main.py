from express import express

app = express()

def nextHandle(req,res,next):
    return next()

def lasthandler(req,res,next):
    res.setHeader("kdjf","djkf")
    res.setHeader("kdjf","dfjk")
    return res.send("oK")

app.get("/",nextHandle)
app.get("/",lasthandler)

app.get("/a",nextHandle)
app.get("/a",lasthandler)


app.listen(3000,"localhost")