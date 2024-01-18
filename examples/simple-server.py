from express_server import express

app = express()
PORT = 3000

# home page 
def home(req,res,next):
    return res.sendfile("./pages/index.html")

# about page
def about(req,res,next):
    return res.sendfile("./pages/about.html")

# route 
app.get("/",home)
app.get("/about",about)

# listner
def listner(err):
    if(not err):
        print(f"Server Running At: {PORT}")

app.listen(PORT,"0.0.0.0",listner)