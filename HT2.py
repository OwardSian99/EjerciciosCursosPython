import  mysql.connector
#Conector con la base de datos
conector = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "3030",
    database = "hoja2"
)

elcursor = conector.cursor()

elcursor.execute("CREATE DATABASE hoja2")
elcursor.execute("Create table personas(id varchar(16), usuario varchar(16), nombre varchar(16), sexo varchar(16), dato varchar(16), correo varchar(16), tel varchar(16), marca varchar(16), marca2 varchar(16), dato2 varchar(16), dato3 varchar() )")
insertar = "insert into personas(id, usuario, nombre, sexo, dato, correo, tel, marca, marca2, dato2, dato3) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
f = open("lectura.txt", "r")
while(True):
    linea = f.readline()
    datos = linea
    elcursor.execute(insertar, datos)
    conector.commit()
    if not linea:
        break
f.close()

elcursor.execute("Select * FROM personas")
mostrar = elcursor.fetchall()

for x in mostrar:
    print(x)