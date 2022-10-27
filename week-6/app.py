from flask import Flask, request, render_template, redirect, session, url_for
import mysql.connector
import os

app=Flask(__name__,)

connection = mysql.connector.connect(
    host= "localhost",
    port= "3306",
    user="root",
    password="隱藏ing",
    database="website"
)
cursor = connection.cursor()

app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    name=request.form["name"]
    user=request.form["username"]
    psd=request.form["password"]
    select=("select * from member where username= %(username)s")
    cursor.execute(select, {"username": user})
    account=cursor.fetchall()
    if account:
        return redirect(url_for("error",message="帳號已被註冊"))
    elif not name or not user or not psd:
        return redirect(url_for("error",message="姓名、帳號、密碼不能空白"))
    else:
        insert=("insert into member(name, username, password) values(%s, %s, %s)")
        value=[name, user, psd]
        cursor.execute(insert, value)
        connection.commit()
        return redirect("/")
    cursor.close()
    connection.close()

@app.route("/signin",methods=["POST"])
def signin():
    user=request.form["username"]
    psd=request.form["password"]
    select=("select * from member where username= %s")
    data=[user]
    cursor.execute(select, data)
    user=cursor.fetchone()
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
    member_id=session["userid"]
    content=request.form["mesgcontent"]
    insert=("insert into message(member_id, content) values(%s, %s)")
    value=[member_id, content]
    cursor.execute(insert, value)
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
    session["loggedin"]=None
    session["userid"]=None
    session["name"]=None
    session["username"]=None
    session["password"]=None
    return redirect("/")


if __name__ =='__main__':
    app.debug = True
    app.run(port=3000)
