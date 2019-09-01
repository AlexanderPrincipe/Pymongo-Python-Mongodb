from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['teststore']
collection = db['products']

#collection.insert_one({"_id": 2, "name": "keyboard", "price": 300})

#product_one = {"name": "mouse"}
#product_two = {"name": "monitor"}

#collection.insert_many([product_one, product_two])

results = collection.find({"price": 300})

for r in results:
    print(r)