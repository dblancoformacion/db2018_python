CREATE TABLE usuarios(
  id int PRIMARY KEY,
  nombre varchar(255),
  password varchar(20),
  usuarios varchar(20)
  );
CREATE TABLE foros(
  codigo int PRIMARY KEY,
  titulo varchar(255)
  );
CREATE TABLE mensajes(
  codigo int PRIMARY KEY,
  contenido varchar(255),
  fecha date,
  foro int,
  creador int,
  FOREIGN KEY(creador) REFERENCES usuarios(id),
  FOREIGN KEY(foro) REFERENCES foros(codigo)
  );
CREATE TABLE vistas(
  mensaje int,
  usuario int,
  fecha datetime,
  PRIMARY KEY(mensaje,usuario,fecha),
  FOREIGN KEY(mensaje) REFERENCES mensajes(codigo),
  FOREIGN KEY(usuario) REFERENCES usuarios(id)
  );