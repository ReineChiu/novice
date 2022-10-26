from flask import Flask, request, render_template, redirect, session, url_for
import mysql.connector
import os

app=Flask(__name__,)

connection = mysql.connector.connect(
    host= "localhost",
    port= "3306",
    user="root",
    password="80808080",
    database="website"
)

app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    regcursor=connection.cursor()
    name=request.form["name"]
    user=request.form["username"]
    psd=request.form["password"]
    regcursor.execute("select * from member where username='"+user+"';")
    account=regcursor.fetchall()
    if account:
        return redirect(url_for("error",message="帳號已被註冊"))
    elif not name or not user or not psd:
        return redirect(url_for("error",message="姓名、帳號、密碼不能空白"))
    else:
        regcursor.execute("insert into member(name, username, password) values('"+name+"','"+user+"','"+psd+"');")
        connection.commit()
        return redirect("/")
    cursor.close()
    connection.close()

@app.route("/signin",methods=["POST"])
def signin():
    mycursor=connection.cursor()
    user=request.form["username"]
    psd=request.form["password"]
    mycursor.execute("select * from member where username='"+user+"' and password='"+psd+"';")
    user=mycursor.fetchone()
    if user:
        session["userid"]=user[0]
        session["name"]=user[1]
        session["username"]=user[2]
        session["password"]=user[3]
        return redirect("/member")
    else:  
        return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))
    cursor.close()
    connection.close()

@app.route("/member")
def member():
    if not session.get("username"):
        return redirect("/")
    username=session["username"]
    mesgcursor=connection.cursor()
    mesgcursor.execute("select member.username, message.content, member.id, message.member_id from member inner join message on member.id=message.member_id order by message.time desc;")
    message = mesgcursor.fetchall()
    return render_template("member.html",username=username,message=message)
    cursor.close()
    connection.close() 

@app.route("/message",methods=["POST"])
def message():
    mesgcursor=connection.cursor()
    member_id=session["userid"]
    username=session["username"]
    content=request.form["mesgcontent"]
    mesgcursor.execute("insert into message(member_id, content) values('"+str(member_id)+"', '"+content+"');")
    mesg = mesgcursor.fetchall()
    connection.commit()
    return redirect(url_for("member"))
    cursor.close()
    connection.close()    

@app.route("/error")
def error():
    message=request.args.get("message","")
    return render_template("error.html",message = message)

@app.route("/signout")
def signout():
    session["userid"]=None
    session["name"]=None
    session["username"]=None
    session["password"]=None
    return redirect("/")


if __name__ =='__main__':
    app.debug = True
    app.run(port=3000)
