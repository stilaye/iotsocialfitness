from pymongo import MongoClient

database_port = 27017
database_collection = "social_fitness"

client = MongoClient(port=database_port)

db_host = "mongodb://localhost:27017/"
db_name = "social_fitness"
db_client = MongoClient(port=database_port)
db = db_client[db_name]
db_collection = db["iot"]


def update_sensor_data(data):
    db_collection.update(
        {
            "user": str(data['user'])
        },
        {
            "$set": {
                "device_status": data.get('device_status'),
                "device_id": data.get("device_id"),
                "type": data.get("type")
            }
        }, upsert=True)


def update_user_data(data):
    db_collection.update(
        {
            "user": str(data['user'])
        },
        {
            "$set": {
                "phone": data.get('phone'),
                "email": data.get("email"),
                "mac_address": data.get("mac_address"),
                "user_location": data.get("location")
            }
        }, upsert=True)