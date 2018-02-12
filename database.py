from pymongo import MongoClient

database_port = 27017
database_collection = "social_fitness"

client = MongoClient(port=database_port)

db_host = "mongodb://localhost:27017/"
db_name = "social_fitness"
db_client = MongoClient(port=database_port)
db = db_client[db_name]
machine_coll = db["machine"]
users_coll = db["users"]

_COFFEE_POT = ["coffee_pot", "coffee pot", "coffee machine", "coffee_machine"]


def update_sensor_data(data):
    device_type = data.get("type")
    if device_type in _COFFEE_POT:
        machine_coll.update(
            {
                "user": str(data['user'])
            },
            {
                "$set": {
                    "device_status": data.get('device_status'),
                    "device_id": data.get("device_id"),
                    "type": data.get("type"),
                    "location": data.get("location")
                }
            }, upsert=True)
    else:
        users_coll.update(
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
    users_coll.update(
        {
            "user": str(data['user'])
        },
        {
            "$set": {
                "phone": data.get('phone'),
                "email": data.get("email"),
                "mac_address": data.get("mac_address"),
                "user_location": data.get("location"),
                "name": str(data.get('name')),
                "interests": data.get("interests")            }
        }, upsert=True)


def get_empty_coffee_machines():
    cursor = machine_coll.find({"device_status": "empty"},
                               {"_id": 0, "user": 1, "device_status": 1, "device_id": 1, "location": 1})
    empty_machines = []
    for res in cursor:
        empty_machines.append(res)
    return empty_machines


def get_users_empty_devices():
    cursor = users_coll.find({"device_status": "empty"},
                             {"_id": 0, "user": 1, "device_status": 1, "phone": 1, "email": 1, "interests":1, "name": 1,
                              "user_location": 1})
    users = []
    for res in cursor:
        users.append(res)
    return users
