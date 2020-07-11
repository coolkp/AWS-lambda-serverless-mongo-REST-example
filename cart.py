import json
import pymongo
import logging
from datetime import datetime
from samples import sample_inventory_item, sample_order_item, url
from bson.json_util import dumps
client=pymongo.MongoClient(url)

def cart(event, context):
    # get request body
    print(event)
    data = json.loads(event['body'])
    store_db = client[event['pathParameters']['db_name']]
    store_db_carts = store_db["carts"]
    store_db_carts.replace_one({"user_email":data["user_email"]}, data, upsert=True)
    response = {
        "statusCode": 200,
        "body": dumps(data)
    }
    return response
