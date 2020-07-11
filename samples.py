import os
url = os.environ['MONGO_DB_URL']
sample_inventory_item = {
        "updatedOn": "Sat May 30 19:18:27 EDT 2020",
        "itemName":"Sample",
        "barcode":"72527273070",
        "price":0.99,
        "category":"cleaning",
        "brand":"sample"
    }

sample_order_item = {
        "processedOn": "Sat May 30 19:18:27 EDT 2020",
        "ordertotal":0.99,
        "userId":"001"
    }

sample_cart = {
            "user_email":"test@test.com",
            "items":[
                    {
                    "barcode":"7768680260",
                    "name":"Test Product",
                    "price":"0.99",
                    "quantity":"2"
                    }
            ],
            "total":24.86
        }

proj = {'_id':0}
