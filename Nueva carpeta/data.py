import sqlite3

conn = sqlite3.connect("ferretodo.db")
c= conn.cursor()

# Ejecutar la consulta para agregar la columna

c.execute("ALTER TABLE productos ADD COLUMN cant INT(11) ")

conn.commit()

conn.close()