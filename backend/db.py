from products import productos
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
    return jsonify({"productos":productos})
@app.route("/productos/agregar",methods = ["POST"])
def agregar():
    print(request.json)
    new_product = {
        "name":  request.json["name"],
        "price": request.json["price"],
        "stock": request.json["stock"]
    }
    productos.append(new_product)
    return jsonify({
        "message": "product add succefully",
        "producto": new_product
    })
@app.route("/productos/leer/<string:name_product>",methods = ["GET"])
def leer(name_product):
    producto_encntrado = [producto for producto in productos if producto["name"] == name_product]
    if(len(producto_encntrado)>0):
        print(producto_encntrado)
        return jsonify({"producto": producto_encntrado})
    else:
        return jsonify({"message": "product do not found"})
@app.route("/productos/actualizar/<string:edit_product>",methods = ["PUT"])
def actualizar(edit_product):
    productos_encontrados = [producto for producto in productos if producto["name"] == edit_product]
    if (len(productos_encontrados) > 0):
        productos_encontrados[0]["name"]  = request.json["name"]
        productos_encontrados[0]["price"] = request.json["price"]
        productos_encontrados[0]["stock"] = request.json["stock"]
        print(productos_encontrados[0])
        return jsonify({
            "message": "Product Updated succefully",
            "productos": productos_encontrados[0]
        })
    return jsonify({'message': 'Product Not found'})
@app.route("/productos/eliminar/<string:delete_product>",methods = ["DELETE"])
def eliminar(delete_product):
    producto_encontrado = [producto for producto in productos if producto["name"] == delete_product]
    if(len(producto_encontrado) > 0):
        productos.remove(producto_encontrado[0])
        print("Producto delete")
        return jsonify({
            "message": "product delete succefully",
            "productos": productos
        })
    else:
        return jsonify({"message": "product not found"})
if __name__ == "__main__":
    app.run("0.0.0.0",5050,debug = True)