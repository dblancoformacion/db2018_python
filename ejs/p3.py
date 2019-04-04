import untangle
import mysql.connector
conn = mysql.connector.connect(
	host='127.0.0.1',
	user='root',
	password='',
	database='db2018_python'
) 
rs=conn.cursor()
rs.execute("DELETE FROM aemet WHERE date(insercion)=date(NOW());")
r = untangle.parse('http://www.aemet.es/xml/municipios/localidad_39075.xml')
print("f_elaboracion : ",r.root.elaborado.cdata)
print("lugar : ",r.root.nombre.cdata)
for i in r.root.prediccion.dia:
	fecha=i['fecha']
	if len(i.prob_precipitacion):
		lluvia=i.prob_precipitacion[0].cdata
	else:
		lluvia=i.prob_precipitacion.cdata
	sql="""
		INSERT INTO aemet (fecha, lluvia, insercion)
		  VALUES ('{}','{}',NOW());
	""".format(fecha,lluvia)
	rs.execute(sql)
rs.execute("DELETE FROM aemet WHERE fecha=date(insercion);")	
rs.execute("UPDATE aemet SET f_prediccion=date(insercion);");
conn.commit()