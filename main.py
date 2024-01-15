from express import express
app = express()

# response handler
def home(req,res,next):
    return res.sendfile("index.html")

def about(req,res,next):
    return res.send("This is about page")

# routes 
app.get("/",home)
app.get("/about",about)

app.listen(3000,"0.0.0.0")