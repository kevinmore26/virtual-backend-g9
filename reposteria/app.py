from flask import Flask 
from conexion_bd import base_de_datos
from models.ingrediente import IngredientesModel
from models.receta import RecetaModel
from models.preparacion import PreparacionModel
from models.recetas_ingredientes import RecetaIngredienteModel
from os import environ 
from dotenv import load_dotenv
load_dotenv()

print(environ.get('DATABASE_URI'))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= environ.get('DATABASE_URI')

# FOR MYSQL   mysql:// username:password@host/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/reposteria_flask'

# si se establece True sqlAchemy rastreará las modificaciones de los objetos (modelos) y lanzará señales de cambio, su valor prederteminado es None, igual habilita el tracking pero emite una advertencia que en futuras versiones se removerá el valor x default None y si o si tendremos que indicar un valor inicial
app.config['SQALCHEMY_TRACK_MODIFICATIONS']=False

base_de_datos.init_app(app)

base_de_datos.create_all(app=app)

@app.route("/")
def initial_controller():
    return{
        "message":'hola'
    }

if __name__=='__main__':
    app.run(debug=True)