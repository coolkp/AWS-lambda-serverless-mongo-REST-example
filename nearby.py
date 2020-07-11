import json
import pymongo
import logging
from datetime import datetime
from samples import url
from bson.json_util import dumps

client=pymongo.MongoClient(url)
from math import radians, cos, sin, asin, sqrt

def distance(lat1, lat2, lon1, lon2):

    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    # Radius of earth in miles.
    r = 3956

    # calculate the result
    return(c * r)

def nearby(event, context):
    data = event['queryStringParameters']
    q = {
        "loc": {
            "$near": {
            "$geometry": {
                "type": "Point" ,
                "coordinates": [float(data["long"]), float(data["lat"])]
            },
            "$maxDistance":7000
            }
         }
        }
    a = client["management"]
    all_stores = a["all_stores"]
    res = list(all_stores.find(q, {"_id":0}))
    for r in res:
        r["distance"] = distance(float(r["loc"]["coordinates"][1]),
                                float(data["lat"]),
                                float(r["loc"]["coordinates"][0]),
                                float(data["long"]))

    return {
        "statusCode": 200,
        "body":dumps(res)
        }
