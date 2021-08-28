-- CREAR UNA BASE DE DATOS LLAMADA EMPRESA
-- GESTION DE LOS EMPLEADOS DE UNA EMPRESEA, EN LA CUAL ESTÀ DISTRIBUIDA
-- POR DEPARTAMENTO ( INFORMATICA, PUBLICADO , MARKETING, FINANZAS)
-- ADEMÀS SE REQUIERE CONTROLAR AL PERSONAL( NOMBRE, APELLIDO, ID ) CADA 
-- PERSONAL PUEDE PERTENECER A UN DEPARTAMENTO 
-- NO TODOS LOS EMPLEADOS TIENEN DEPARTAMENTOS

-- UN PERSONAL A LA VEZ PUEDE SER SUPERIOR DE OTRO PERSONAL

CREATE DATABASE EMPRESA;
USE EMPRESA;

CREATE TABLE DEPARTAMENTOS (
	ID INT NOT NULL auto_increment PRIMARY KEY,
    NOMBRE VARCHAR(30)
    
);

CREATE TABLE PERSONALES(
ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
NOMBRE VARCHAR(40),
APELLIDO VARCHAR(40),
IDENTIFICADOR TEXT,
DEPARTAMENTO_ID INT,
SUPERVISOR_ID INT,
FOREIGN KEY (DEPARTAMENTO_ID) REFERENCES DEPARTAMENTOS(ID),
FOREIGN KEY (SUPERVISOR_ID) REFERENCES PERSONALES(ID)

);
