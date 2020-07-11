import json
import pymongo
import logging
from datetime import datetime
from samples import url
from bson.json_util import dumps

client=pymongo.MongoClient(url)

def all(event, context):
    # get request body
    resp = {"stores":list(client["management"]["all_stores"].find({}))}
    response = {
        "statusCode": 200,
        "body": dumps(list(client["management"]["all_stores"].find({})))
    }
    return response