import json
import pymongo
import logging
from datetime import datetime
from samples import sample_inventory_item, sample_order_item, url, sample_cart
from bson.json_util import dumps

client=pymongo.MongoClient(url)

def verify(event, context):
    data = json.loads(event['body'])
    response = {
        "statusCode": 200,
        "body": event['body']
    }
    return response
