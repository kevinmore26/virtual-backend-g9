from flask import Flask, request

app = Flask(__name__)
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
            "message":'',
            "content":"los productos son:"
        }

    elif request.method =='POST':
        producto = request.get_json()
        productos.append(producto)
        return{
        "message":"producto creado exitosamente",
        "content":producto
    }
@app.route("/producto/<int:id>", methods=["GET"])
def gestion_producto(id):
    total_productos=len(productos)
    if id<=total_productos:
        return{
            "content":productos[id],
            "message": None
        }
    else:
        return{
                "message":"producto no existe",
                "content":None
        }
    # print(request.method)
    # if id<=10 =="GET":
    #     return{
    #     "message":"producto no existe"
    # }

    


    

if __name__=="__main__":
    app.run(debug=True)