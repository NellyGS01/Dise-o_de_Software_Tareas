from pymongo.mongo_client import MongoClient
import pymongo
from pymongo import MongoClient


cluster = MongoClient('mongodb+srv://nellyalethia:12345@cluster0.auxtoop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db  = cluster["prueba"]
collection = db["test"]

post = {"_id":0, "name": "Test1",  "age" :32}
collection.insert_one(post)


