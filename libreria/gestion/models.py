from django.db import models

#https://docs.djangoproject.com/en/3.2/ref/models/

class ProductoModel(models.Model):
    productoId = models.AutoField(primary_key=True,null=False, unique=True, db_column='id')

    productoNombre= models.CharField(max_length=45,db_column='nombre',null=False)

