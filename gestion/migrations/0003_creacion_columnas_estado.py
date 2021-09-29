# Generated by Django 3.2.7 on 2021-09-24 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_creacion_tablas_operaciones_clientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientemodel',
            name='pclienteDireccion',
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='clienteDireccion',
            field=models.CharField(db_column='direccion', default='los palitos 414', max_length=100, verbose_name='direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='clienteEstado',
            field=models.BooleanField(db_column='estado', default=True),
        ),
        migrations.AddField(
            model_name='productomodel',
            name='productoEstado',
            field=models.BooleanField(db_column='estado', default=True),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='clienteDocumento',
            field=models.CharField(db_column='documento', max_length=12, unique=True, verbose_name='ingrese su documento'),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='clienteNombre',
            field=models.CharField(db_column='nombre', help_text='ingresa tu nombre xd', max_length=45, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='productomodel',
            name='productoUnidadMedida',
            field=models.TextField(choices=[('UN', 'UNIDAD'), ('DOC', 'DOCENA'), ('CI', 'CIENTO'), ('MI', 'MILLAR')], db_column='unidad_medida', default='UN'),
        ),
    ]