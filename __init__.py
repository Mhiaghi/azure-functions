#TEST 02
import logging
import requests
import azure.functions as func
import pymysql
from datetime import datetime, timedelta

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        "Se recibio un mensaje",
        status_code=200
        )