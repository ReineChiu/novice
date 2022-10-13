from flask import Flask
from flask import request
from flask import render_template 
from flask import redirect 
from flask import session
from flask import url_for
app=Flask(__name__)

app.secret_key="any string but secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin",methods=["POST"])
def signin():
    userid=request.form["userid"]
    password=request.form["password"]
    
    if userid=="test" and password=="test": 
        session["userid"]=userid
        return redirect("/member")
    elif userid=="" or password=="":
        return redirect(url_for("error",message="請輸入帳號、密碼"))
    else:
        return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))
   
@app.route("/member")
def member():
    if not session.get("userid"):
        return redirect("/")
    return render_template("member.html")

@app.route("/sign_out")
def sign_out():
    session["userid"] = None
    return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("error.html",message = message)
     
@app.route("/account")
def account():
    num=request.args.get("num")
    num=int(num)
    return redirect(url_for("square",num=num))

@app.route("/square/<int:num>")
def square(num):
    return render_template("square.html",result =str(num**2))
    

if __name__ =='__main__':
    app.debug = True
    app.run(port=3000)