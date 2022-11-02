from flask import Flask, request, render_template, redirect, session, url_for
import mysql.connector
import json, os
from mysql_data import MySQLPassword

app=Flask(__name__,)
app.config["SECRET_KEY"] = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = MySQLPassword(),
    database = "website",
    )
    name = request.form["name"]
    user = request.form["username"]
    password = request.form["password"]

    try:
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
    except:   
        print("signup錯誤")
    finally:
        cursor.close()
        connection.close()

@app.route("/signin",methods=["POST"])
def signin():
    connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = MySQLPassword(),
    database = "website",
    )
    user = request.form["username"]
    password = request.form["password"]

    try:
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
    except:   
        print("signin錯誤")
    finally:
        cursor.close()
        connection.close()  

@app.route("/member")
def member():
    connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = MySQLPassword(),
    database = "website",
    )
    if "username" in session:
        username = session["username"]
        
        try:
            cursor = connection.cursor()
            cursor.execute('''select member.username, message.content, message.time,
                                    member.id, message.member_id from member inner join message 
                                    on member.id=message.member_id order by message.time desc;''')
            message = cursor.fetchall()
            return render_template("member.html",username = username,message = message)
        except:   
            print("顯示留言失敗")
        finally:
            cursor.close()
            connection.close()

    else:
        return redirect("/")

@app.route("/api/member", methods=["GET"])
def api_member():
    connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = MySQLPassword(),
    database = "website",
    )
    if "username" in session:
        username = request.args.get("username","")
        
        try:
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
        except:   
            print("查詢失敗")
        finally:
            cursor.close()
            connection.close()

    else:
        return json.dumps({"data":None})

@app.route("/api/member", methods=["PATCH"])
def patch_member():
    connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = MySQLPassword(),
    database = "website",
    )
    if "username" in session:
        data = request.get_json("name")
        name = session["name"]
        
        try:
            cursor = connection.cursor()
            update = ("update member set username=%s where name =%s")
            value = [data["name"], name]
            cursor.execute(update, value)
            connection.commit()

            select = ("select * from member where username=%s and name=%s")
            result  =[data["name"], name]
            cursor.execute(select, result)
            newName = cursor.fetchone()
            if newName:
                return json.dumps({"ok":True})
            else:
                return json.dumps({"error":True})
        except:   
            print("更新失敗")
        finally:
            cursor.close()
            connection.close()

    else:
        return json.dumps({"error":True})

@app.route("/message",methods=["POST"])
def message():
    connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = MySQLPassword(),
    database = "website",
    )
    memberId = session["userid"]
    content = request.form["mesgcontent"]

    try:
        cursor = connection.cursor()
        insert = ("insert into message(memberId, content) values(%s, %s)")
        value=[memberId, content]
        cursor.execute(insert, value)
        connection.commit()
    except:   
        print("新增留言失敗")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("member"))
    
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