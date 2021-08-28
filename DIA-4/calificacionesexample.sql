CREATE DATABASE CALIFICACIONES;
USE CALIFICACIONES;

CREATE TABLE alumnos(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(30),
    APELLIDO VARCHAR(30),
    CORREO VARCHAR(50)
);

CREATE TABLE cursos(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(30),
    DURACION TINYINT,
    CREDITOS TINYINT,
    ESTADO BOOLEAN
);

CREATE TABLE alumnos_cursos(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_alumno int,
    id_curso int,
     FOREIGN KEY (id_alumno) REFERENCES alumnos(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);
