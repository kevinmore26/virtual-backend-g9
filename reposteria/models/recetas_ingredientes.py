
from conexion_bd import base_de_datos
from sqlalchemy import Column,types
from sqlalchemy.sql.schema import ForeignKey

class RecetaIngredienteModel(base_de_datos.Model):
    __tablename__="recetas_ingredientes"

    recetasIngredientesId = Column(name='id',type_=types.Integer,primary_key=True, unique=True, autoincrement=True, nullable=False)


    receta = Column(ForeignKey(column="recetas.id", ondelete='RESTRICT'),
    name="recetas_id",type_=types.Integer , nullable =False)

    ingredientes = Column(ForeignKey(column="ingredientes.id", ondelete='RESTRICT'),
    name="ingredientes_id",type_=types.Integer , nullable =False)