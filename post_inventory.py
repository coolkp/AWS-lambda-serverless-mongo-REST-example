import json
import pymongo
import logging
from datetime import datetime
from samples import url

client=pymongo.MongoClient(url)


def inventory(event, context):
    # get request body
    data = json.loads(event['body'])

    # Get store db name by coordinates from all stores
    store_db_name = data["db_name"]
    inventory_items = data["inventory_items"]
    store_db = client[store_db_name]
    store_db_inventory = store_db["inventory"]
    for inventory_item in inventory_items:
        filter = {"barcode":inventory_item["barcode"]}
        store_db_inventory.replace_one({"barcode":inventory_item["barcode"]}, inventory_item, upsert=True)

    response = {
        "statusCode": 200,
        "body": event['body']
    }
    return response
