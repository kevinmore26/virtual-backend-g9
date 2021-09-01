from sqlalchemy.sql import base
from conexion_bd import base_de_datos
from sqlalchemy import Column,types
from sqlalchemy.sql.schema import ForeignKey
class PreparacionModel(base_de_datos.Model):
    __tablename__="preparaciones"

    preparacionId=Column(type_=types.Integer,name="id",primary_key=True,autoincrement=True,unique=True)

    preparacionOrden=Column(type_=types.Integer,name="orden",default=1)

    preparacionDescripcion=Column(type_=types.Text,name="descripcion",nullable=False)

    receta = Column(ForeignKey(column="recetas.id", ondelete='RESTRICT'),
    name="recetas_id",type_=types.Integer , nullable =False)