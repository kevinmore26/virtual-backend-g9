from rest_framework import serializers
from .models import ProductoModel

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        # esto vinculará el serializador con el modelo respectivo para alar sus atributos y hacer la validaicones corresponientes
        model = ProductoModel
        # indica qué campos tengo que mostrar para la deserialización 
        # ---
        # indicará qué haremos uso de todaos los atributos del modelo
        fields='__all__'
        # fields=['productoNombre','productoPrecio']
        # ---
        # atributos para excluir
        # exclude=['productoId']
