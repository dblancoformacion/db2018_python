import untangle
import mysql.connector
conn = mysql.connector.connect(
	host='127.0.0.1',
	user='root',
	password='',
	database='db2018_python'
) 
rs=conn.cursor()
# elimino los registros del mismo día que hago el volcado desde aemet
# para que la clave unique me deje insertar los nuevos
rs.execute("DELETE FROM aemet WHERE date(insercion)=date(NOW());")
# accedo al xml de aemet con los datos de las predicciones
r = untangle.parse('http://www.aemet.es/xml/municipios/localidad_39075.xml')
print("f_elaboracion : ",r.root.elaborado.cdata)
print("lugar : ",r.root.nombre.cdata)
for i in r.root.prediccion.dia:
	fecha=i['fecha']
	for j in i.prob_precipitacion:
		#print(fecha,j['periodo'],j.cdata)
		sql="""
			INSERT INTO aemet (fecha, periodo, lluvia, insercion)
			  VALUES ('{}','{}','{}',NOW());
		""".format(fecha,j['periodo'],j.cdata)
		rs.execute(sql)
	'''
	if len(i.prob_precipitacion):
		lluvia=i.prob_precipitacion[0].cdata
	else:
		lluvia=i.prob_precipitacion.cdata
	sql="""
		INSERT INTO aemet (fecha, lluvia, insercion)
		  VALUES ('{}','{}',NOW());
	""".format(fecha,lluvia)
	'''
	#rs.execute(sql)
rs.execute("DELETE FROM aemet WHERE fecha=date(insercion);")	
rs.execute("UPDATE aemet SET f_prediccion=date(insercion);");
conn.commit()
sql="""
	SELECT fecha,periodo,lluvia
	  FROM aemet WHERE date(insercion)=(
	  SELECT MAX(date(insercion)) FROM aemet
	) AND periodo!='00-06'
	AND lluvia=(
	  SELECT MIN(lluvia) FROM aemet WHERE date(insercion)=(
	    SELECT MAX(date(insercion)) FROM aemet
	  ) AND periodo!='00-06'
	);
"""
rs.execute(sql)
r=rs.fetchall()
for i in r:
	print("Puedes ir el",i[
	0],"a las ",i[1],"con una probabilidad de lluvia del",i[2],"%")
input()
