import sqlite3

conn = sqlite3.connect("ferretodo.db")
c= conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS empleados (
    cedula TEXT PRYMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(50),
    usuario VARCHAR(50),
    password VARCHAR(50),
    telefono INTEGER
)""")
c.execute("INSERT INTO empleados VALUES('28103046', 'Louis', 'Arroyo', 'Inferno2208@gmail.com','inferno2208', '28103046Ll.', 04121224435)")
conn.commit()

conn.close()