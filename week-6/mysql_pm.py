import mysql.connector

connection = mysql.connector.connect(
        host= "localhost",
        port= "3306",
        user="root",
        password="隱藏ing",
        database="website"
    )

cursor = connection.cursor()

def web_select(**kwargs):
    sql_select = "select * from member where "
    for key in kwargs:
        sql_select+=f"{key}='{kwargs[key]}' and "
    sql=sql_select[:-5]
    cursor.execute(sql)
    user=cursor.fetchone()
    return user

def web_insert(**kwargs):
    insertColumn=''
    insertValue=''
    for key in kwargs:
        insertColumn+=f"{key}, "
        insertValue+=f"'{kwargs[key]}', " 
    insertColumn=insertColumn[:-2]
    insertValue=insertValue[:-2]
    sql_insert = "insert into member ("+insertColumn+") values ("+insertValue+");"
    cursor.execute(sql_insert)
    connection.commit()
