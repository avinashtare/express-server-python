from express import express

app = express()

def handleHome(req,res,next):
    print(req,res,next)

app.get("/",handleHome)

app.listen(3000)