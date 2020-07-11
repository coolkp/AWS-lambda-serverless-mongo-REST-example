import json
import pymongo
import logging
from datetime import datetime
from samples import sample_inventory_item, sample_order_item, url, sample_cart
from bson.json_util import dumps

client=pymongo.MongoClient(url)

def create(event, context):
    # get request body
    print(event)
    print("FUCK FUCK")
    data = json.loads(event['body'])
    admin = client["management"]
    #MAKE ALL STORES GEOSPATIAL AND INDEXED BY LATITUDE LONGITUDE.
    all_stores = admin["all_stores"]
    try:
        all_stores.create_index([("loc", pymongo.GEOSPHERE)],unique=True)
    except Exception as e:
        pass
    s = "_".join(data["name"].split())
    store_db_name = s + "_" + "0"
    while store_db_name in client.list_database_names():
        store_db_name = store_db_name[:-1] + str(int(store_db_name[-1]) + 1)
    data["db_name"] = store_db_name
    try:
        all_stores.insert_one(data)
    except Exception as e:
        response = {
            "statusCode": 400,
            "body": json.dumps({"msg":"Already present store"})
        }
        return response


    store_db = client[store_db_name]
    store_db_orders = store_db["orders"]

    store_db_orders.insert_one(sample_order_item)

    store_db_inventory = store_db["inventory"]
    store_db_inventory.create_index("barcode", unique=True)
    store_db_inventory.insert_one(sample_inventory_item)

    store_db_carts = store_db["carts"]
    store_db_carts.create_index("user_email", unique=True)
    store_db_carts.insert_one(sample_cart)
    # write item to database
    response = {
        "statusCode": 200,
        "body": dumps(data)
    }
    logging.info(data)

    return response
