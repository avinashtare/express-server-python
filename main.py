from express import express

app = express()

def home(req,res,next):
    password = (req.find_qeury("pass"))
    username = (req.find_qeury("username"))

    return res.send(f"""
                    <h1>Home</h1><a href='/about'>About</a>
                    <h2>UserName: {username}</h2>
                    <h2>Password: {password}</h2>
                    """)

def about(req,res,next):
    path = req.ip
    return res.send(f"{path}<h1>About</h1><a href='/'>Home</a>")

app.get("/",home)
app.get("/about",about)
app.get("/about 2 2 2",about)

app.listen(3000,"0.0.0.0")