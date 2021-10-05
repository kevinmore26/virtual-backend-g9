from rest_framework.generics import ListCreateAPIView

from facturacion.serializers import comprobanteSerializer
from rest_framework.response import Response
from .generarComprobante import crearComprobante

class ComprobanteController(ListCreateAPIView):
    serializer_class=comprobanteSerializer
    def post(self,request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            print(data.validated_data)
            tipoComprobante =  data.validated_data.get('tipoComprobante')
            pedidoId =  data.validated_data.get('pedidoId')
            numeroDocumento = data.validated_data.get('numeroDocumento')
            tipoComprobante=2 if tipoComprobante =='BOLETA' else 1
            crearComprobante(tipoComprobante,pedidoId,numeroDocumento)
            return Response(data={
                "message":""
            },status=201)
        else:
            return Response(data={
                "message":"error al crear el comprobante",
                "content":data.errors
            },status=400)
    def get(self,request):
        pass