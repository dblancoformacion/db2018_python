SELECT * FROM mysql.user;
SELECT * FROM information_schema.SCHEMA_PRIVILEGES;
SELECT * FROM information_schema.USER_PRIVILEGES WHERE GRANTEE LIKE '%profe%';
CREATE USER 'profe'@'localhost' IDENTIFIED BY 'hola';

DROP USER 'profe'@'%';
GRANT ALL ON  *.* TO 'profe'@'%' IDENTIFIED BY 'hola';
GRANT ALL ON db2018.* TO 'alumno'@'%';
GRANT ALL ON db2018.* TO 'profe'@'%' IDENTIFIED BY 'hola';
GRANT ALL ON ciclistas.* TO profe;


SHOW TABLES;

SHOW GRANTS FOR 'profe'@'%';

REVOKE ALL ON ciclistas.* FROM profe;
SHOW GRANTS FOR profe;

