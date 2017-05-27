import requests
from pymongo import MongoClient
from random_uagents import random_ua
from random_proxy import random_proxy


client = MongoClient("YOUR_MONGO_CONNECTION_STRING")
db = client.deliveroo

logs_doc = open("/logs.txt", "w")


for i in range(0, 100000):
    try:
        proxy = random_proxy()
        header = {"User-agent": random_ua()}

        req = requests.request("GET", "https://deliveroo.co.uk/orderapp/v1/restaurants/" + str(i), proxies=proxy, verify=False, headers=header)

        reqj = req.json()

        reqj["coordinates"][0] = str(reqj["coordinates"][0])
        reqj["coordinates"][1] = str(reqj["coordinates"][1])

        db.restaurants.insert_one(reqj)

        logs_doc.write("SUCCESS: " + "https://deliveroo.co.uk/orderapp/v1/restaurants/" + str(i) + "\n")

    except ValueError:
        logs_doc.write("FAIL: " + "https://deliveroo.co.uk/orderapp/v1/restaurants/" + str(i) + "\n")

        continue
