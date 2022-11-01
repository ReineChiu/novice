from flask import Flask, request, render_template, redirect, session, url_for
import mysql.connector
import json, os

connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "",
    database = "website",
)

app=Flask(__name__,)
app.config["SECRET_KEY"] = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    name = request.form["name"]
    user = request.form["username"]
    password = request.form["password"]
    cursor = connection.cursor()
    select=("select * from member where username= %(username)s")
    cursor.execute(select, {"username": user})
    account = cursor.fetchone()
    if account:
        return redirect(url_for("error",message = "帳號已被註冊"))
    elif not name or not user or not password:
        return redirect(url_for("error",message = "姓名、帳號、密碼不能空白"))
    else:
        insert = ("insert into member(name, username, password) values(%s, %s, %s)")
        value = [name, user, password]
        cursor.execute(insert, value)
        connection.commit()
        return redirect("/")
    cursor.close()
    connection.close()

@app.route("/signin",methods=["POST"])
def signin():
    user = request.form["username"]
    password = request.form["password"]
    cursor = connection.cursor()
    select = ("select * from member where username= %s and password= %s")
    data = [user, password]
    cursor.execute(select, data)
    result = cursor.fetchone()
    if result:
        session["userid"] = result[0]
        session["name"] = result[1]
        session["username"] = result[2]
        session["password"] = result[3]
        return redirect(url_for("member"))
    else:  
        return redirect(url_for("error",message = "帳號、或密碼輸入錯誤"))
    cursor.close()
    connection.close() 

@app.route("/member")
def member():
    if "username" in session:
        username = session["username"]
        messagecursor = connection.cursor()
        messagecursor.execute('''select member.username, message.content, message.time,
                                member.id, message.member_id from member inner join message 
                                on member.id=message.member_id order by message.time desc;''')
        message = messagecursor.fetchall()
        return render_template("member.html",username = username,message = message)
    else:
        return redirect("/")
    
    cursor.close()
    connection.close()

@app.route("/api/member", methods=["GET"])
def api_member():
    if "username" in session:
        username = request.args.get("username","")
        cursor = connection.cursor()
        select = ("select id, name, username from member where username=%s")
        value = [username]
        cursor.execute(select, value)
        name = cursor.fetchone()
        if name:
            columns = [col[0] for col in cursor.description]
            data = dict(zip(columns, name))
            return json.dumps({"data":data}, ensure_ascii=False)
        else:
            return json.dumps({"data":None})
    else:
        return json.dumps({"data":None})
    
    cursor.close()
    connection.close()

@app.route("/api/member", methods=["PATCH"])
def patch_member():
    if "username" in session:
        data = request.get_json("name")
        name = session["name"]
        cursor = connection.cursor()
        update = ("update member set username=%s where name =%s")
        value = [data["name"], name]
        cursor.execute(update, value)
        connection.commit()

        newcursor = connection.cursor()
        select = ("select * from member where username=%s and name=%s")
        result  =[data["name"], name]
        newcursor.execute(select, result)
        newName = newcursor.fetchone()
        if newName:
            return json.dumps({"ok":True})
        else:
            return json.dumps({"error":True})
    else:
        return json.dumps({"error":True})
    cursor.close()
    connection.close()

@app.route("/message",methods=["POST"])
def message():
    memberId = session["userid"]
    content = request.form["mesgcontent"]
    cursor = connection.cursor()
    insert = ("insert into message(memberId, content) values(%s, %s)")
    value=[memberId, content]
    cursor.execute(insert, value)
    connection.commit()
    return redirect(url_for("member"))
    cursor.close()
    connection.close()
    
@app.route("/error")
def error():
    message = request.args.get("message","")
    return render_template("error.html",message = message)

@app.route("/signout", methods=["GET"])
def signout():
    session["userid"] = None
    session["name"] = None
    session["username"] = None
    session["password"] = None
    return redirect("/")

if __name__ =='__main__':
    app.debug = True
    app.run(port=3000)