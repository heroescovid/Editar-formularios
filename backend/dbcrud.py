from products import productos
from flask import Flask
from flaskext.mysql import MySQL as db
app = Flask(__name__)
mysql = db()
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "iot"
app.config["MYSQL_DATABASE_Host"] = "127.0.0.1"
mysql.init_app(app)
query_db = """
    """
valores = ()
def agregar(**valores):
    conexion = mysql.connect()
    cursores = conexion.cursor()
    query_db = """ INSERT INTO store(
        name,price,stock)VALUES(%s,%s,%s);"""
    data = (valores["name"],valores["price"],valores["stock"])
    cursores.execute(query_db,data)
    conexion.commit()
    conexion.close()
def leer(identify):
    conexion = mysql.connect()
    cursores   = conexion.cursor()
    querydbs = """
        SELECT * FROM store WHERE name = %s;
    """
    cursores.execute(querydbs,identify)
    conexion.commit()
    resultad = cursores.fetchone()
    conexion.close()
    return resultad
def actualizar(identify,**valores):
    conexion = mysql.connect()
    cursores = conexion.cursor()
    query_db = """UPDATE store SET name = %s,price = %s, stock = %s WHERE id = %s;"""
    data = (valores["name"],valores["price"],valores["stock"],identify)
    cursores.execute(query_db,data)
    conexion.commit()
    conexion.close()
def eliminar(identify):
    conexion = mysql.connect()
    cursores = conexion.cursor()
    query_db = """DELETE FROM store WHERE id = %s;"""
    cursores.execute(query_db,identify)
    conexion.commit()
    conexion.close()
def read_all():
    conexion = mysql.connect()
    cursores = conexion.cursor()
    query_db = """SELECT * FROM store;"""
    cursores.execute(query_db)
    resultado = cursores.fetchall()
    cursores.close()
    return resultado