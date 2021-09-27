from django.contrib import admin
from .models import ClienteModel, ProductoModel ,ClienteModel

class ProductoAdmin(admin.ModelAdmin):
    # modificar la vista el modelo
    # no funciona lo del ordenamiento
    list_display=['productoId','productoNombre','productoPrecio']
    #para filtrar y hacer busquedas
    search_fields=['productoNombre','productoUnidadMedida']

    list_filter=['productoUnidadMedida']

    # campo solo lectura
    # indico si se desea ver algun campo que el usuario no puede manipular 
    readonly_fields=['productoId']


admin.site.register(ClienteModel)
admin.site.register(ProductoModel,ProductoAdmin)


class ClienteAdmin(admin.ModelAdmin):
    # modificar la vista el modelo
    # no funciona lo del ordenamiento
    list_display=['clienteId','clienteNombre','clienteDocumento','clienteDireccion']
    #para filtrar y hacer busquedas
    search_fields=['clienteNombre','clienteDocumento']

    list_filter=['clienteNombre','clienteDocumento']

    # campo solo lectura
    # indico si se desea ver algun campo que el usuario no puede manipular 
    readonly_fields=['clienteId']