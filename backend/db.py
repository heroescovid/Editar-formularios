from pickle import NONE
from turtle import update
from products import productos
import dbcrud
from flask import Flask, app,jsonify,render_template,request
from flaskext.mysql import MySQL as db
from flask_cors import CORS
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
CORS(app)
#run_with_ngrok(app)
@app.route("/",methods = ["GET"])
def index():
    productos = []
    resultado = dbcrud.read_all()
    for x in resultado:
        producto = {
            "id":    x[0],
            "name":  x[1],
            "price": x[2],
            "stock": x[3]
        }
        productos.append(producto)
        print(producto)
    return jsonify({"productos":productos})
@app.route("/productos/agregar",methods = ["POST"])
def agregar():
    print(request.json)
    new_product = {
        "name":  request.json["name"],
        "price": request.json["price"],
        "stock": request.json["stock"]
    }
    dbcrud.agregar(**new_product)
    return jsonify({
        "message": "product add succefully",
        "producto": new_product
    })
@app.route("/productos/leer/<string:name_product>",methods = ["GET"])
def leer(name_product):
    #producto_encntrado = [producto for producto in productos if producto["name"] == name_product]
    #if(len(producto_encntrado)>0):
    #    print(producto_encntrado)
    #    return jsonify({"producto": producto_encntrado})
    #else:
    #    return jsonify({"message": "product do not found"})
    resultado = dbcrud.leer(name_product)
    #valores = len(resultado)
    if(resultado==None):
        return jsonify({"message": "sorry product not found"})
    else:
        return jsonify({"producto": resultado})
@app.route("/productos/actualizar/<string:edit_product>",methods = ["PUT"])
def actualizar(edit_product):
    #productos_encontrados = [producto for producto in productos if producto["name"] == edit_product]
    #if (len(productos_encontrados) > 0):
    #    productos_encontrados[0]["name"]  = request.json["name"]
    #    productos_encontrados[0]["price"] = request.json["price"]
    #    productos_encontrados[0]["stock"] = request.json["stock"]
    #    print(productos_encontrados[0])
    #    return jsonify({
    #        "message": "Product Updated succefully",
    #        "productos": productos_encontrados[0]
    #    })
    print(request.json)
    update_product = {
        "name":  request.json["name"],
        "price": request.json["price"],
        "stock": request.json["stock"]
    }
    print(update_product)
    dbcrud.actualizar(edit_product,**update_product)
    return jsonify({'message': 'Product Not found'})
@app.route("/productos/eliminar/<string:delete_product>",methods = ["DELETE"])
def eliminar(delete_product):
    #producto_encontrado = [producto for producto in productos if producto["name"] == delete_product]
    #if(len(producto_encontrado) > 0):
    #    productos.remove(producto_encontrado[0])
    dbcrud.eliminar(delete_product)
    print("Producto delete succefully")
    return jsonify({
            "message": "product delete succefully",
            "productos": ""
    })
    #else:
    #    return jsonify({"message": "product not found"})
if __name__ == "__main__":
    app.run("0.0.0.0",5050,debug = True)