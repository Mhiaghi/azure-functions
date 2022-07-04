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
    logging.info(cnx)
    cursor = cnx.cursor()
    tipo = req.params.get('tipo_IoT')	
    codigo = req.params.get('codigo_IoT')
    valor = req.params.get('valor_IoT')
    medida = req.params.get('medida_IoT')
    fecha_entrada = req.params.get('fecha_entrada')
    
    if not tipo:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            tipo = req_body.get('tipo_IoT')
            codigo = req_body.get('codigo_IoT')
            valor = req_body.get('valor_IoT')
            medida = req_body.get('medida_IoT')
            fecha_entrada = req_body.get('fecha_entrada')
            
    if tipo:
        try:
            now = datetime.now()
            now = now - timedelta(hours= 5)
            fecha_salida = now.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO devices VALUES ('%s','%s','%s', '%s','%s','%s') " % (tipo,codigo,valor,medida,fecha_entrada,fecha_salida))
            cursor.execute("CALL eliminarultimasfilas('%s') " % (codigo))
            fecha_entrada = fecha_entrada = fecha_entrada[0:10] + " " + fecha_entrada[11:19]
            cnx.commit()
        except pymysql.IntegrityError:
            print("Error")
        return func.HttpResponse(f"Hello, {codigo}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )