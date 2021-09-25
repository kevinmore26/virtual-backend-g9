from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginacionPersonalizada(PageNumberPagination):
    # nombre de la variable para indicar el número de páginas 
    page_query_param='pagina'
    # tamaño de los items por página por defecto
    page_size=2
    #  es el nombre de la variable que usaremos para indicar  los elementos por página
    page_size_query_param='cantidad'
    # sirve para limitar el tamaño de página 
    max_page_size=10

    # la data e sla información que está siendo paginada
    def get_paginated_response(self, data):
        return Response(data={
            "paginacion":{
                "paginaContinua":self.get_next_link(),
                "paginaPrevia":self.get_previous_link(),
                "total":self.page.paginator.count,
                "porPagina":self.page.paginator.per_page
            },
            "data":{
                "content":data,
                "message":None
            }
        })