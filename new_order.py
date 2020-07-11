import json
import pymongo
import logging
from datetime import datetime
from samples import url
from bson.json_util import dumps
import pyqrcode
import io, base64
import random, secrets, string

client=pymongo.MongoClient(url)

def order(event, context):

    qr_dat = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                                                  for i in range(6))
    print("EFFING ", qr_dat)
    c = pyqrcode.create(qr_dat)
    s = io.BytesIO()
    c.png(s,scale=1)
    encoded_qr = base64.b64encode(s.getvalue())
    data = json.loads(event['body'])
    print("DATA")
    print(data)
    data["order"]["qrCode"] = encoded_qr.decode('utf-8')
    data["order"]["qrText"] = qr_dat
    print("QR QR")
    print(data["order"]["qrCode"])
    store_db_name = event['pathParameters']['db_name']
    store_db = client[store_db_name]
    store_db_orders = store_db["orders"]
    store_db_orders.insert_one(data["order"])
    response = {
        "statusCode": 200,
        "body": dumps(data)
    }
    return response
