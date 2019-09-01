from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['teststore']
collection = db['products']

#collection.insert_one({"_id": 2, "name": "keyboard", "price": 300})

product_one = {"name": "laptop"}
product_two = {"name": "monitor"}

collection.insert_many([product_one, product_two])

results = collection.find({"price": 300})

for r in results:
    print(r)


collection.delete_many({"price": 300})   # Elimina los objetos con precio = 300
collection.delete_one({"name": "mouse"})  # Elimina los objetos con nombre mouse
collection.delete_many({})    # Elimina todos los datos de la coleccion

collection.update_one({"name": "laptop"}, {"$set": {"name", "keyboard", "price": 300}})   # Actualizar

number_of_products = collection.count_documents({})
print(number_of_products)