from rest_framework import serializers
from cms.models import PedidoModel

class comprobanteSerializer(serializers.Serializer):
    pedidoId=serializers.IntegerField()
    tipoComprobante=serializers.ChoiceField(choices=['BOLETA','FACTURA'])
    numeroDocumento=serializers.CharField(min_length=8,max_length=11)

    def validate(self,data):
        '''Se llamará automáticamente cuando se llame al método is_valid() en el controlador'''
        try:
            data['pedidoId']=PedidoModel.objects.filter(pedidoId=data.get('pedidoId')).first()
        
            if data.get('pedidoId') is None:
                raise Exception()
            return data
        except:
            raise serializers.ValidationError(detail='Error en el pedido')