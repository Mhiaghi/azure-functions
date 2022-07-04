#TEST 02
import logging
import requests
import azure.functions as func
import pymysql
from datetime import datetime, timedelta



def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    cnx = pymysql.connect(
        user = "Mhiaghi",
        password = 'Miguel123',
        host = 'msaturno-database.mysql.database.azure.com',
        port = 3306,
        database = 'SEIDORLAB'
        )
    cursor = cnx.cursor()
    req_body = req.get_json()
    #multiple
    if len(req_body) == 5:
        try:
            tipo = req_body.get('tipo_IoT')
            codigo = req_body.get('codigo_IoT')
            valor = req_body.get('valor_IoT')
            medida = req_body.get('medida_IoT')
            fecha_entrada = req_body.get('fecha_entrada')
            fecha_entrada = fecha_entrada = fecha_entrada[0:10] + " " + fecha_entrada[11:19]
            now = datetime.now()
            now = now - timedelta(hours= 5)
            fecha_salida = now.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO devices VALUES ('%s','%s','%s', '%s','%s','%s') " % (tipo,codigo,valor,medida,fecha_entrada,fecha_salida))
            cursor.execute("CALL eliminarultimasfilas('%s') " % (codigo))
            cnx.commit()
            func.HttpResponse("introduccion exitoso 1 solo",status_code=200)
        except:
            func.HttpResponse("introduccion fallida 1 solo",status_code=200)
    for texto in req_body:
        tipo = texto.get('tipo_IoT')
        codigo = texto.get('codigo_IoT')
        valor = texto.get('valor_IoT')
        medida = texto.get('medida_IoT')
        fecha_entrada = texto.get('fecha_entrada')
        now = datetime.now()
        now = now - timedelta(hours= 5)
        fecha_salida = now.strftime("%Y-%m-%d %H:%M:%S")
        fecha_entrada = fecha_entrada = fecha_entrada[0:10] + " " + fecha_entrada[11:19]
        try:
            cursor.execute("INSERT INTO devices VALUES ('%s','%s','%s', '%s','%s','%s') " % (tipo,codigo,valor,medida,fecha_entrada,fecha_salida))
            cursor.execute("CALL eliminarultimasfilas('%s') " % (codigo))
            cnx.commit()
        except pymysql.IntegrityError:
            func.HttpResponse("Error en base de datos de muchas filas",status_code=200)

    func.HttpResponse("Exito muchas filas", status_code=200)
    return "JSON"

