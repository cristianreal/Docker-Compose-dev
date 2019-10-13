create database tareacontainers_sa;
USE tareacontainers_sa;

create table prueba (
id int(6) unsigned auto_increment primary key,
nombre varchar(30) not null,
usuario varchar(50),
reg_date timestamp default current_timestamp on update current_timestamp
);

show tables;

Insert into prueba (nombre, usuario) values ('Juan Carlos Plata', 'usuario1@mail.com');
Insert into prueba (nombre, usuario) values ('Carlos Ruiz', 'usuario2@mail.com');
Insert into prueba (nombre, usuario) values ('Guillermo Ramirez', 'usuario3@mail.com');
Insert into prueba (nombre, usuario) values ('Lionel Messi', 'usuario4@mail.com');
Insert into prueba (nombre, usuario) values ('Cristiano Ronaldo', 'usuario5@mail.com');
Insert into prueba (nombre, usuario) values ('Zlatan Ibrahimovic', 'usuario6@mail.com');

select * from prueba;