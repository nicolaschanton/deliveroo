from pymongo import MongoClient

client = MongoClient("YOUR_MONGO_CONNECTION_STRING")
db = client.deliveroo


db.restaurants.remove({})