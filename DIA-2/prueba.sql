
USE prueba1;

CREATE TABLE personas (
-- ahora definiremos las columnas --
-- nombre_col tipo_dato[primary key | not null]
id int primary key not null auto_increment,
-- el unique indica que si ingreso unn valor, ese valor no se puede
-- repetir con otro ingresado anterior ment,
-- mas no obliga al usuario a ingresarlo
documento varchar(20) unique ,
tipo_documento enum('DNI','C.E','PASAPORTE'),
nombre varchar(12),
apellido varchar(50),
correo varchar(100) unique,
sexo enum('FEMENINO','MASCULINO','OTRO'),
fecha_nacimiento date 
);

-- FORMA DE AGREGAR VALORES A LA BD
INSERT INTO personas (documento,tipo_documento,nombre,apellido, correo, fecha_nacimiento,sexo)
VALUES 				 ('74822014','DNI','KEVIN','MORE','kore_2608@hotmail.com','2001-08-26','MASCULINO');
-- FORMA DE VISUALIZAR LOS DATOS DE UNA TABLA INDICANDO LAS COLUMNAS
SELECT documento, nombre, fecha_nacimiento FROM personas;

-- para seleccionar todo

SELECT * FROM personas;


INSERT INTO personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
VALUES                 (null, 'S/ DOCUMENTO', 'JUAN', 'MARTINEZ', 'jmartinez@gmail.com', '1989-05-15', 'OTRO');

INSERT INTO personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
VALUES                 ('12345678', 'C.E', 'MARIA', 'PEREZ', 'mperez@gmail.com', '1995-12-10', 'FEMENINO');

INSERT INTO personas (documento, tipo_documento, nombre, apellido, correo, fecha_nacimiento, sexo)
VALUES                 ('12345677', 'C.E', 'EDUARDO', 'PEREZ', 'eperez@gmail.com', '1995-12-10', 'FEMENINO');

ALTER TABLE personas MODIFY documento varchar(20) unique;

SELECT * FROM personas WHERE nombre = 'MARIA' AND sexo= 'FEMENINO';


-- ELIMINAR REGISTRO 

DELETE FROM personas WHERE correo="mperez@gmail.com";
SELECT * from personas ;

-- ACTUALIZAR UNO O VARIOS REGISTROS
UPDATE personas SET nombre ='RAMIRO' WHERE id = 1;




CREATE TABLE medicos(
    id int primary key not null auto_increment,
    cmp varchar(5) unique not null, -- colegio medico del peru
    nombre varchar(30),
    apellido varchar(50)
);


CREATE TABLE historial_vacunaciones(
    id int primary key not null auto_increment,
    vacuna enum('PFIZER','SINOPHARM', 'ASTRAZENECA'),
    lote varchar(10),
    fecha date,
    medico_id int,
    paciente_id int,

    -- para crear las relaciones
    foreign key (medico_id) references medicos(id),
    foreign key (paciente_id) references personas(id)
);

INSERT INTO medicos (cmp, nombre, apellido) 
VALUES               ('1234','RAUL','MUÑOZ'),
                    ('1236','ROSA','HIDALGO'),
                    ('5829','SOFIA','ALEMAN');
                    -- EL NOW ES PARA INDICAR LA HORA ACTUAL 	
INSERT INTO historial_vacunaciones (vacuna, lote, medico_id, paciente_id, fecha) 
VALUES                                ('PFIZER','1234',1, 1, '2021-07-24'),
                                   ('SINOPHARM','1598', 2, 3, '2021-08-01'),
                                   ('ASTRAZENECA','1959', 1, 4, '2021-08-24'),
                                   ('PFIZER','1234',1, 1, now()),
                                   ('SINOPHARM', '5948', 3, 3, now());
                                   
SELECT * FROM historial_vacunaciones;
SELECT * FROM historial_vacunaciones WHERE vacuna = 'PFIZER' OR vacuna= 'ASTRAZENECA';