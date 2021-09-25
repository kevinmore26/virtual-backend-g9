from rest_framework.test import APITestCase
from .models import ProductoModel

class ProductosTestCase(APITestCase):

    def setUp(self):
        ProductoModel(productoNombre='Producto 21', productoUnidadMedida='UN', productoPrecio=20.50).save()
        ProductoModel(productoNombre='Producto 23', productoUnidadMedida='UN',productoPrecio=20.50).save()
        ProductoModel(productoNombre='Producto 41',productoUnidadMedida='UN',productoPrecio=20.50).save()
        ProductoModel(productoNombre='Producto 21', productoUnidadMedida='UN',productoPrecio=20.50).save()



    def test_post_fail(self):
        # print(self.shortDescription())
        '''Debería fallar el test cuando no le pasamos la información'''
        request=self.client.post('/gestion/productos/')
        message=request.data.get('message')

        self.assertEqual(request.status_code,400)
        self.assertEqual(message,'Error al guardar')

    def test_post_success(self):
        '''Debería retornar el producto creado'''
        # print(self.shortDescription())

        request = self.client.post('/gestion/productos/',data={
        "productoNombre":"Cartulinda blanca",
        "productoPrecio":7.50,
        "productoUnidadMedida":"UN"
        },format='json')

        message=request.data.get('message')
        id=request.data.get('content').get('productoId')
        
        productoEncontrado=ProductoModel.objects.filter(productoId=id).first()
        
        self.assertEqual(request.status_code,201)
        self.assertEqual(message,'Producto creado exitosamente')
        self.assertIsNotNone(productoEncontrado)

def test_get_success(self):
    '''Debería retornar los productos ya creados'''

    # request=self.client.get('/gestion/productos?pagina=1&cantidad=2')
    # paginaPrevia=request.data.get('paginaPrevia')
    # paginaContinua =request.data.get('paginaContinua')
    # porPagina=request.data.get('porPagina')

   
    # self.assertEqual(paginaPrevia,None)
    # self.assertIsNotNone(paginaContinua)
    # self.assertEqual(porPagina,porPagina)

    request=self.client.get('/gestion/productos?pagina=1&cantidad=2')
    paginacion=request.data.get('paginacion')
    content=request.data.get('data').get('content')

    self.assertIsNone(paginacion.get('paginaPrevia'))
    self.assertIsNone(paginacion.get('paginaContinua'))
    self.assertEqual(paginacion.get('porPagina'),2)
    self.assertEqual(len(content),2)



