# 
edad = input("Edad : \n")
nacimiento = 2019-int(edad)
print(nacimiento)
#######
import mysql.connector
conn = mysql.connector.connect(
	host='127.0.0.1',
	user='root',
	password='',
	database='db2018_python'
) 
sql="""
	INSERT INTO python (instante,edad,nacimiento)
	  VALUES (NOW(),'{}','{}');
""".format(edad,nacimiento)
rs=conn.cursor()
rs.execute(sql)
conn.commit()
######
input("Pulsa enter para cerrar")