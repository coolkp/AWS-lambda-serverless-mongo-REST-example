import json
import pymongo
import logging
from datetime import datetime
from samples import url, proj
from bson.json_util import dumps

client=pymongo.MongoClient(url)

def promotions (event, context):
    store_db = client[event['pathParameters']['db_name']]
    store_db_inventory = store_db['promotions']

    return {
    "statusCode":200,
    "body": dumps(list(store_db_inventory.find({}, proj)))
    }
