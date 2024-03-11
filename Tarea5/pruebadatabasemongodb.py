from pymongo.mongo_client import MongoClient
import pymongo
from pymongo import MongoClient


cluster = MongoClient('mongodb+srv://nellyalethia:12345@cluster0.auxtoop.mongodb.net/?retryWrites=true&w=majority&Prueba/test=Cluster0')
db  = cluster["Prueba"]
collection = db["test"]

post = {"_id":0, "name": "Test1",  "age" :32}
collection.insert_one(post)

#result = collection.delete_one({"_id":0})

#results = collection.update_one({"_id":0, "name": "Test2",})



#Da error la conexion