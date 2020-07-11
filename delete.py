import json
import pymongo
import logging
from datetime import datetime
from samples import url
from bson.json_util import dumps

client=pymongo.MongoClient(url)

def delete(event, context):
    # get request body
    data = json.loads(event['body'])
    management = client["management"]
    resp = {"deleted":[]}
    all_stores = management["all_stores"]
    for store_db_name in client.list_database_names():
        if data["name"] in store_db_name:
            print(store_db_name)
            print("HELLO")
            q = {"db_name":store_db_name}
            store = all_stores.find_one(q)
            delete_result = all_stores.delete_one(q)
            print(delete_result)
            resp["deleted"].append(store)
            client.drop_database(store_db_name)
    response = {
        "statusCode": 200,
        "body": dumps(resp)
    }
    return response
