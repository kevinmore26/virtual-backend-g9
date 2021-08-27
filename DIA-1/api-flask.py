from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
productos=[
    {
        "nombre":"palta fuerte",
        "precio":5.20
    },
    {
        "nombre":"albahaca",
        "precio":0.80
    }
]
@app.route("/")
def inicio():
    return{
        "message":"Bienvenido ",
        "content":"hola",
    }

@app.route("/productos", methods=['POST','GET'])
def gestion_productos():
    print(request.method)
    if request.method == 'GET':
        return{
            "message":'los productos son:',
            "content":productos     
        }

    elif request.method =='POST':
        producto = request.get_json()
        productos.append(producto)
        return{
        "message":"producto creado exitosamente",
        "content":producto
    }
@app.route("/producto/<int:id>", methods=["GET","PUT","DELETE"])
def gestion_producto(id):
    total_productos=len(productos)
    if id<total_productos:
        if request.method =="GET":
            return{
            "content":productos[id],
            "message": None
        },200
        elif request.method =="PUT":
            data = request.get_json()
            productos[id]=data
            return{
                "content":productos[id],
                "message":"Producto actualizado exitosamente"
            }, 201

        elif request.method =="DELETE":
                del productos[id]
                return{
                    "content":None,
                    "message":"Producto eliminado exitosamente"
                }

            


            

    else:
            return{
                "message":"producto no existe",
                "content":None
        },404
    


    # print(request.method)
    # if id<=10 =="GET":
    #     return{
    #     "message":"producto no existe"
    # }

    


    

if __name__=="__main__":
    app.run(debug=True)