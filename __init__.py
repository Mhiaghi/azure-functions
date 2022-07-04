#TEST 02
import logging
import requests
import azure.functions as func
import pymysql
from datetime import datetime, timedelta

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_json()
        return func.HttpResponse(
                "Se recibio un json",
                status_code=200
                )
    except:
        return func.HttpResponse(
                "Mensaje Nulo",
                status_code=200
                )