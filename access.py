# volcado de datos desde Access
import pyodbc
from os import getcwd

DB_PATH = getcwd() + "/" + "db2018"
DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"

conn_local = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))

rs_local = conn_local.cursor()
rs_local.execute("""
		SELECT * FROM datos;
	""")

for r in rs_local.fetchall():
	print(r[1])