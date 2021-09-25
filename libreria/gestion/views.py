# from libreria.gestion.serializers import ProductoSerializer
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,CreateAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import ProductoModel, ClienteModel
from .serializers import ProductoSerializer
from rest_framework import status
from .utils import PaginacionPersonalizada
from rest_framework.serializers import Serializer
# from django.db.models.

class PruebaController(APIView):
    def get(self, request,format=None):
        return Response({'message':'Exito'},status=200)
    
    def post(self,request:Request, format=None):
        print(request.data)
        return Response(data={'message':'Hiciste post'})

class ProductosController(ListCreateAPIView):
    # pondremos la consulta de ese modelo en la BD
    queryset=ProductoModel.objects.all()
    # es igual que el SELECT * FROM productos ;

    serializer_class=ProductoSerializer
    pagination_class=PaginacionPersonalizada

    # def get(self,request):
    #     respuesta=self.get_queryset().filter(productoEstado=True).all()
    #     print(respuesta)
    #     respuesta_serializada= self.serializer_class(instance=respuesta,many=True)
        
    #     return Response(data={
    #         "message":None,
    #         "content":respuesta_serializada.data
    #     })

    def post(self, request:Request):
        print(request.data)
        data=self.serializer_class(data=request.data)
        if data.is_valid():
            # PARA HACER EL GUARDADO DE UN NUEVO REGISTRO EN LABD ES OBLIGATORIO HACER PRIMERO EL IS_vALID
            data.save()
            return Response(data={
                "message":"Producto creado exitosamente",
                "content":data.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message":"Error al guardar",
                "content":data.errors
                }, status=status.HTTP_400_BAD_REQUEST)

class ProductoController(APIView):
    def get(self, request,id):

        print(id)
        # select* from productos where id = id
        productoEncontrado=ProductoModel.objects.filter(productoId=id).first()
        
        print(productoEncontrado)
        try:
            productoEncontrado2=ProductoModel.objects.get(productoId=id)
            print(productoEncontrado2)
        except ProductoModel.DoesNotExist:
            print('no se encontró')
        if productoEncontrado is None:
            return Response(data={
                "message":"Producto no existe",
                
                }, status=status.HTTP_404_NOT_FOUND)

        serializador = ProductoSerializer(instance=productoEncontrado2)

        return Response(data={
            "message":None,
            "content":serializador.data
        })
    def put(self,request:Request,id):
        # 1. busco si el producto existe
        productoEncontrado=ProductoModel.objects.filter(productoId=id).first()
        if productoEncontrado is None:
            return Response(data={
                "message":"Producto no existe",
                "content":None
            }, status=status.HTTP_404_NOT_FOUND)
        # 2. modificaré los valores proveidos
        serializador = ProductoSerializer(data=request.data)
        if serializador.is_valid():
        
            serializador.update(instance=productoEncontrado,validated_data=serializador.validated_data)
            # 3. guardaré y devolveré el producto actualizado
            return Response(data={
                "message":"Producto actualizado exitosamente",
                "content":serializador.data
            })
        else:
            return Response(data={
                "message":"Error al actualizar",
                "content":serializador.errors
            }, status=400)

    def delete(self,request,id):
        productoEncontrado=ProductoModel.objects.filter(productoId=id).first()
        if productoEncontrado is None:
            return Response(data={
                "message":"Producto no encontrado",
                "content":None
            },status=status.HTTP_404_NOT_FOUND)
        
        productoEncontrado.productoEstado=False
        productoEncontrado.save()

        serializador=ProductoSerializer(instance=productoEncontrado)

        return Response(data={
            "message":"Producto eliminado exitosamente",
            "content":serializador.data
        })
        

class ClienteController(ListCreateAPIView):
    queryset=ClienteModel.objects.all()
    def get(self,request):
        pass
    
    def post(self,request:Request):
        data:Serializer=self.get_serializer(data=request.data)
        if data.is_valid():
            return Response(data={
                "message":"Cliente agregado exitosamente"
            })
        else:
            return Response(data={
                "message":"Error al ingresar el cliente",
                "content":data.errors
            })




