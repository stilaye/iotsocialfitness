from pymongo import MongoClient

database_port = 27017
database_collection = "social_fitness"

client = MongoClient(port=database_port)

db_host = "mongodb://localhost:27017/"
db_name = "social_fitness"
db_client = MongoClient(port=database_port)
db = db_client[db_name]
db_collection = db["iot"]


def insert(data):
    db_collection.insert_one(data)