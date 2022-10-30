create database aplicacion;
use aplicacion;
create table registro(
id int primary key auto_increment,
nombre varchar(255),
apellido varchar(255),
correo varchar(255),
contraseña varchar(8)
);

create table nota(
id int primary key auto_increment,
nombrenota varchar(255),
nota varchar(255)
);
create table galeria(
id int primary key auto_increment,
imagen LONGBLOB,
video  BLOB
);
create table nota_de_voz(
id int primary key auto_increment,
audio BLOB
);

#alter table nota add constraint fk_notagaleria foreign key (id) references galeria(id) on delete cascade on update cascade;
#alter table registro add constraint fk_registronota foreign key (id) references nota(id) on delete cascade on update cascade;
#alter table galeria add constraint fk_galerianota foreign key (id) references nota(id) on delete cascade on update cascade;
#alter table nota_de_voz add constraint fk_galerian foreign key (id) references galeria(id) on delete cascade on update cascade;
#drop database aplicacion;
select * from registro;