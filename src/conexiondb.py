from flask import Flask,jsonify,render_template
from flaskext.mysql import MySQL as db
app = Flask(__name__)
mysql = db()
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "iot"
app.config["MYSQL_DATABASE_Host"] = "127.0.0.1"
mysql.init_app(app)
conexion = mysql.connect()
cursor   = conexion.cursor()
query = "INSERT INTO sensores_invernadero(name,sector,valor) VALUES (%s,%s,%s)"
data  = ("humedad","A",50)
cursor.execute(query,data)
conexion.commit()
print(cursor.rowcount, "record inserted.")