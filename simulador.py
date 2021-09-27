from faker import Faker
fake=Faker()

def fake_products(cantidad):
    UNIDADES_MEDIDAS=['UN',
                    'DOC',
                    'CI',
                    'MI']
    for id in range(1, cantidad+1):
        nombre= "Producto 0" +str(id)
        precio= float(fake.pydecimal(left_digits=3, right_digits=1, positive=True, min_value=1, max_value=150))
        unidad_medida=UNIDADES_MEDIDAS[ fake.random_int(min=0,max=3)]
        print("INSERT INTO productos(nombre,precio,unidad_medida,estado) VALUES('%s',%s,'%s',true);" %(nombre,precio,unidad_medida))

fake_products(100)

# def fake_clients(cantidad):
    
#     RANDOM_PLACES=['palitos123',
#                     'cedros156',
#                     'sanmiguel123',
#                     'pueblolibre434',
#                     'tangamandapio']
#     for id in range(1, cantidad+1):
#         nombre= "cliente 0" +str(id)
#         documento= float(fake.pyint(min_value=11111111, max_value=99999999,))
#         direccion=RANDOM_PLACES[ fake.random_int(min=0,max=4)]
#         # direccion=fake.place_name()

       
#         print("INSERT INTO productos(nombre,documento,direccion,estado) VALUES('%s',%s,'%s',true);" %(nombre,documento,direccion))

# fake_clients(100)