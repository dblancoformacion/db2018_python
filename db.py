import mysql.connector

conn = mysql.connector.connect(
	host='localhost',
	user='root',
	password='',
	database='db2018'
) 

rs=conn.cursor()

sql="""
	INSERT INTO datos (dato) VALUES (
		'{}'
	);
""".format('Hola')
#rs.execute(sql)
conn.commit()

sql="""
	SELECT * FROM datos;
""";
rs.execute(sql)

r=rs.fetchall()
for i in r:
	print(i[1])


conn.close()