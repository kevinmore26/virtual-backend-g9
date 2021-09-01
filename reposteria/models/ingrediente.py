from conexion_bd import base_de_datos
from sqlalchemy import Column, types

class IngredientesModel(base_de_datos.Model):
    __tablename__ = 'ingredientes'

    # id int primary key not null unique auto_increment
    ingredienteId = Column(name='id',type_=types.Integer,primary_key=True, unique=True, autoincrement=True, nullable=False)

    # ingredienteId = Column.__init__(name='id',type_=types.Integer)

    ingredienteNombre= Column(name='nombre',primary_key=True,type_=types.String(length=45))