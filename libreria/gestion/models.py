from django.db import models

#https://docs.djangoproject.com/en/3.2/ref/models/

class ProductoModel(models.Model):

    class OpcionesUm(models.TextChoices):
        UNIDADES='UN','UNIDADES'
        DOCENTA='DOC','DOCENA'
        CIENTO='CI','CIENTO'
        MILLAR='MI','MILLAR'

    productoId = models.AutoField(primary_key=True,null=False, unique=True, db_column='id')

    productoNombre= models.CharField(max_length=45,db_column='nombre',null=False)
    # 
    productoPrecio=models.DecimalField(max_digits=5,decimal_places=2,db_column='precio')
    # 
    productoUnidadMedida= models.TextField(choices=OpcionesUm.choices,default=OpcionesUm.UNIDADES,db_column='unidad_medida')


    class Meta:
        # indica el nombre de la tabla en la bd 
        db_table='productos'
        # ordering=> modifica el ordenamiento por defecto (x el id )al momento de devolver los registros 
        # el "-" es para indicarle de mayor a menors
        ordering=['-productoPrecio']

        # verbose_name y .... => sirven para el panel administrativo de django
        verbose_name='producto'
        verbose_name_plural='productos'



class ClienteModel(models.Model):
    clienteId=models.AutoField(primary_key=True,null=False, unique=True, db_column='id')

    clienteNombre= models.CharField(max_length=45,db_column='nombre',null=False)

    clienteDocumento=models.CharField(max_length=12,db_column='documento',unique=True)

    pclienteDireccion=models.CharField(max_length=100,db_column='direccion')

    class Meta:
        db_table='clientes'
        verbose_name='cliente'
        verbose_name_plural='clientes'

class CabeceraModel(models.Model):
    class OpcionesUm(models.TextChoices):
        VENTA='V','VENTA'
        COMPRA='C','COMPRA'

        
    cabeceraId=models.AutoField(primary_key=True,null=False, unique=True, db_column='id')
    fechaCabecera=models.CharField(max_length=8,db_column='fecha',unique=True)
    tipoCabecera= models.TextField(choices=OpcionesUm.choices,db_column='tipo')


    # 
    clientes=models.ForeignKey(to=ClienteModel, db_column='clientes_id',
                               null=False,related_name='clienteCabecera',on_delete=models.PROTECT)
    # 

    class Meta:
        db_table='cabecera_operaciones'
        verbose_name='cabecera'
        verbose_name_plural='cabeceras'

class DetalleModel(models.Model):
    detalleId=models.AutoField(db_column='id',primary_key=True,unique=True,null=False)

    detalleCantidad=models.IntegerField(db_column='cantidad',null=False)

    detalleImporte=models.DecimalField(max_digits=5,decimal_places=2,db_column='importe',null=False)
    
    productos=models.ForeignKey(to=ProductoModel,db_column='producto_id',on_delete=models.PROTECT,related_name='productoDetalles',null=False)

    cabeceras=models.ForeignKey(to=CabeceraModel,db_column='cabecera_operaciones_id',on_delete=models.
    PROTECT,related_name='cabeceraDetalles',null=False)
    

    class Meta:
        db_table='detalle_operaciones'
        verbose_name='detalle'
        verbose_name_plural='detalles'


