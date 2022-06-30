import pymysql

cnx = pymysql.connect(
    user = "Mhiaghi",
    password = 'Miguel123',
    host = 'msaturno-database.mysql.database.azure.com',
    port = 3306,
database = 'SEIDORLAB'
)
cursor = cnx.cursor()
tipo = "Temperatura"
codigo = "T01"
valor = 27.02
medida = "C"
fecha_entrada = "20-01-01 10:00:00"
fecha_salida = "20-01-01 12:00:00"
if tipo:
    try:
        cursor.execute("INSERT INTO devices VALUES ('%s','%s','%f', '%s','%s','%s') " % (tipo,codigo,valor,medida,fecha_entrada,fecha_salida))
        cnx.commit()
    except pymysql.IntegrityError:
        pass