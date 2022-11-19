import base64
from sqlite3 import connect
import pymysql
import pymysql.cursors
import time
import jwt


JWT_SECRET = "secret"
JWT_ALGO = "HS256"


def select(select_array , table_name , where_list , where_value):
    return 0

def update(update_list , update_value , table_name , where_list , where_value):
    return 0

def delete(table_name , where_list , where_value):
    return 0

def insert(table_name , insert_list , insert_value):
    return 0

def push_user(name: str, username: str, password: str, mail: str):
    password = password.encode("utf-8")
    password = base64.b64encode(password)
    connection = pymysql.connect(host='db',
                             port=3306,
                             user='root',
                             passwd='root',
                             db='gpeDb',)
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO user (name ,username ,password ,mail , role ) VALUES (%s, %s , %s , %s , 1)"
            cursor.execute(sql, (name , username , password , mail))
        try:
            connection.commit()
            return 1
        except pymysql.Error as e:
            return 0

def get_user(username: str, password: str):
    password = password.encode("utf-8")
    password = base64.b64encode(password)
    connection = pymysql.connect(host='db',
                             port=3306,
                             user='root',
                             passwd='root',
                             db='gpeDb',)
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE password=%s AND username=%s"
            cursor.execute(sql, (password , username))
            return cursor.fetchall()

def get_list_user():
    connection = pymysql.connect(host='db',
                        port=3306,
                        user='root',
                        passwd='root',
                        db='gpeDb',)
    with connection:
        with connection.cursor() as cursor:
            sql =  "SELECT * FROM user"
            cursor.execute(sql)
            return cursor.fetchall()

def update_user(token , name , username , mail , password):
    connection = pymysql.connect(host='db',
                        port=3306,
                        user='root',
                        passwd='root',
                        db='gpeDb',)
    decoded_jwt = jwt.decode(token , JWT_SECRET , algorithms=[JWT_ALGO])
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user WHERE userID=%s"
            cursor.execute(sql , (decoded_jwt["id"]))
            result = cursor.fetchall()
    if name == None :
        name = result[0][1]
    if username == None :
        username = result[0][2]
    if mail == None :
        mail = result[0][4]
    if password == None :
        password = result[0][3]
    else :
        password = password.encode("utf-8")
        password = base64.b64encode(password)
    connection = pymysql.connect(host='db',
                        port=3306,
                        user='root',
                        passwd='root',
                        db='gpeDb',)
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE user SET name=%s , username=%s , password=%s , mail=%s WHERE userID=%s"
            cursor.execute(sql ,(name , username , password , mail , decoded_jwt["id"]))
        connection.commit()
    return {"token" : token , "name" : name , "username" : username , "mail": mail , "password" : password}

def delete_user(token , id):
    connection = pymysql.connect(host='db',
                        port=3306,
                        user='root',
                        passwd='root',
                        db='gpeDb',)
    decoded_jwt = jwt.decode(token , JWT_SECRET , algorithms=[JWT_ALGO])
    if decoded_jwt["role"] == 1 and int(decoded_jwt["id"]) != id:
        return {"error" : "permission denied"}
    else:
        with connection:
            with connection.cursor() as cursor:
                sql = "DELETE FROM user WHERE userID=%s"
                cursor.execute(sql ,(id))
            connection.commit()    
        return {"msg" : "le delete de l'utilisateur est reussi"}
        
