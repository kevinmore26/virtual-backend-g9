from .models import ComprobanteModel
from django.db import connection
from cms.models import DetallePedidoModel, PedidoModel
from datetime import datetime
from requests import post
from os import environ

def crearComprobante(tipo_de_comprobante:int,pedido:PedidoModel,documento_cliente:str):
    operacion='generar_comprobante'
    if tipo_de_comprobante == 1:
        serie='FFF1' 
    elif tipo_de_comprobante ==2:
        serie='BBB1'

    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT numero FROM comprobantes WHERE serie ='%s' ORDER BY numero DESC LIMIT 1;",(serie))
    ultimoComprobante=ComprobanteModel.objects.values_list('comprobanteNumero').filter(comprobanteSerie=serie).order_by('-comprobanteNumero').first()

    if not ultimoComprobante:
        numero=1
    else:
        numero=ultimoComprobante.comprobanteNumero + 1 
    sunat_transaction=1
    cliente_tipo_de_documento= (1 if len(documento_cliente) == 8 else 6) if documento_cliente else 6

    cliente_numero_de_documento=documento_cliente
    # \ para hacer salto de línea
    cliente_denominacion = pedido.cliente.usuarioNombre + ' ' + pedido.cliente.usuarioApellido

    cliente_direccion=''

    cliente_email=pedido.cliente.usuarioCorreo

    fecha_de_emision=datetime.now()

    moneda = 1

    porcentaje_de_igv = 18

    total=float(pedido.pedidoTotal)
    
    formato_de_pdf='TICKET'

    platos:list[DetallePedidoModel]=pedido.pedidoDetalles.all()

    items=[]

    for plato in platos:
        unidad_de_medida='NIU'
        codigo=plato.detalleId
        descripcion=plato.plato.platoNombre
        cantidad=plato.detalleCantidad

        # valor_unitario = precio_con_igv / 1.18
        # calculadora IGV 
        valor_unitario=float(plato.plato.platoPrecio) /1.18
        precio_unitario=float(plato.plato.platoPrecio)
        subtotal=valor_unitario * cantidad
        tipo_de_igv = 1
        total_gravada = total / 1.18
        igv=(valor_unitario * cantidad) * porcentaje_de_igv /100
        
        anticipo_regularizacion=False
        json = {
            'unidad_de_medida': unidad_de_medida,
            'codigo': codigo,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'valor_unitario': valor_unitario,
            'precio_unitario': precio_unitario,
            'subtotal': subtotal,
            'tipo_de_igv': tipo_de_igv,
            'igv': igv,
            'total': precio_unitario*cantidad,
            'anticipo_regularizacion': anticipo_regularizacion,
        }
        items.append(json)
    comprobante = {
        'operacion': operacion,
        'tipo_de_comprobante': tipo_de_comprobante,
        'serie': serie,
        'numero': numero,
        'sunat_transaction': sunat_transaction,
        'cliente_tipo_de_documento': cliente_tipo_de_documento,
        'cliente_numero_de_documento': cliente_numero_de_documento,
        'cliente_denominacion': cliente_denominacion,
        'cliente_direccion': cliente_direccion,
        'cliente_email': cliente_email,
        'fecha_de_emision': fecha_de_emision.strftime('%d-%m-%Y'),
        'moneda': moneda,
        'porcentaje_de_igv': porcentaje_de_igv,
        'total': total,
        'formato_de_pdf': formato_de_pdf,
        'items': items,
        'total_gravada':total_gravada,
        'total_igv':total-total_gravada,
        
        'enviar_automaticamente_a_la_sunat':True,
        'enviar_automaticamente_al_cliente':True
    }

    
    headers_nubefact={
        'Authorization':environ.get('NUBEFACT_TOKEN'),
        'Content-Type':'application/json'
    }

    respuesta=post(environ.get('NUBEFACT_URL'),json=comprobante,headers=headers_nubefact)
    print(comprobante)
    print(respuesta.json())


def visualizarComprobante():
    pass