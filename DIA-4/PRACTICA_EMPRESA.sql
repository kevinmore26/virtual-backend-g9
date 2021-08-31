use empresa;

select count(departamento_id) as cantidad , departamento_id, nombre 
from personales group by departamento_id, nombre ;

select  departamento_id, nombre , count(departamento_id) as cantidad 
from personales group by  nombre ,departamento_id 
order by departamento_id ;

select   'departamento 2' departamento , count(id) from personales where departamento_id= 2;

-- NUMERO DE PERSONALES QUE NO TIENEN SUPERVISOR 
select count(*) from personales, departamento_id where supervisor_id IS null group by 
departamento_id order by 1 desc;


-- MOSTRAR EL NOMBRE DEL DEPARTAMENTO Y SU CANTIDAD DE EMPLEADOS 
-- DEPARTAMENTO | CANTIDAD DE EMPLEADOS
-- VENTAS			|  15
-- ADMINISTRACION		25
-- FNANZAS			30

SELECT DEPARTAMENTOS.NOMBRE, count(personales.id) as 'Cantidad de empleados' FROM DEPARTAMENTOS 
	INNER JOIN PERSONALES 
	ON DEPARTAMENTOS.ID = PERSONALES.DEPARTAMENTO_ID group by departamentos.nombre;
    
    

