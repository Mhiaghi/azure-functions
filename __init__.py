import logging
import requests
import azure.functions as func
import mysql.connector

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    cnx = mysql.connector.connect(
        user = "Mhiaghi",
        password = 'Miguel123',
        host = 'msaturno-database.mysql.database.azure.com',
        port = 3306
    )
    logging.info(cnx)
    cursor = cnx.cursor()
    tipo = req.params.get('tipo_IoT')	
    codigo = req.params.get('codigo_IoT')
    valor = req.params.get('valor_IoT')
    medida = req.params.get('medida_IoT')
    fecha_entrada = req.params.get('fecha_entrada_IoT')
    fecha_salida = req.params.get('fecha_salida_IoT')
    cursor.execute("USE SEIDORLAB")
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
            fecha_salida = req_body.get('fecha_salida_IoT')
            
    if tipo:
        cursor.execute("INSERT INTO devices VALUES ('%s','%f', '%s','%s','%s')"% (tipo,codigo,valor,medida,fecha_entrada,fecha_salida))
        return func.HttpResponse(f"Hello, {codigo}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )