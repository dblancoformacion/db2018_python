import untangle

# predicción
r = untangle.parse('http://www.aemet.es/xml/municipios/localidad_39075.xml')

print('Fecha elaboración de la predicción: ',r.root.elaborado.cdata)
#print(r.root.elaborado.prediccion.dia[0]['fecha'])

for i in r.root.prediccion.dia:
	print('--- ',i['fecha'],' ---')
	for j in i.prob_precipitacion:
		if len(j.cdata):
			#if int(j.cdata)>0:
				print(str(j['periodo'])+'h',j.cdata)