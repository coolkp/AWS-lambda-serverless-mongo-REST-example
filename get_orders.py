import json
import pymongo
import logging
from datetime import datetime
from samples import url
from bson.json_util import dumps

client=pymongo.MongoClient(url)

def order(event, context):
    data = json.loads(event['body'])
    store_db_name = data["db_name"]
    store_db = client[store_db_name]
    store_db_orders = store_db["orders"]
    response = {
        "status":200,
        "body":dumps(list(store_db_orders.find({})))
    }
    return response