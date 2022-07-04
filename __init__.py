#TEST 02
import logging
import requests
import azure.functions as func
import pymysql
from datetime import datetime
from pytz import timezone

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
    fecha_entrada = req.params.get('fecha_entrada_IoT')
    
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
            fecha_entrada = req_body.get('fecha_entrada_IoT')
            
    if tipo:
        try:
            now = datetime.now()
            the_timezone = timezone("US/Pacific")
            now = now.astimezone(the_timezone)
            fecha_salida = now.strftime("%Y-%m-%d %H:%M%S")
            #fecha_salida = '2020-01-01 10:00:00'
            #cursor.execute("INSERT INTO devices VALUES ('%s','%s','%s', '%s','%s','%s') " % (tipo,codigo,valor,medida,fecha_entrada,fecha_salida))
            #cursor.execute("CALL eliminarultimasfilas('%s') " % (codigo))
            #cnx.commit()
        except pymysql.IntegrityError:
            print("Error")
        return func.HttpResponse(f"Hello, {fecha_salida}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )