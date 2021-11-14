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
conexion = mysql.connect()
cursor   = conexion.cursor()
