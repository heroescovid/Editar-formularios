from flask import Flask, app,jsonify,render_template,request
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
data = cursor.execute("SHOW TABLES")
@app.route("/",methods = ["GET"])
def index():
    return jsonify({"message": "Welcome to my API"})
@app.route("/crear",methods = ["POST"])
def crear():
    return("")
@app.route("/leer",methods = ["GET"])
def leer():
    return("")
@app.route("/actualizar",methods = ["UPDATE"])
def actualizar():
    return("")
@app.route("/eliminar",methods = ["DELETE"])
def eliminar():
    return("")
if __name__ == "__main__":
    app.run("0.0.0.0",5050,debug = True)