from flask import Flask, request, jsonify
import database
from urllib.parse import urlparse

app = Flask(__name__)
HEADERS = {'Cache-Control': 'private, max-age=0, no-cache', 'Content-type': 'application/json'}


@app.route('/status')
def status():
    return "Social Fitness IoT"


@app.route('/api/v1/social')
def social():
    # get data from mongo here and return like the json below
    res = {
        "coffee_pots": database.get_coffee_machines(),
        "users": database.get_users_empty_devices()
    }
    return jsonify(res)


@app.route('/api/v1/user/data', methods=['POST', 'GET'])
def user_data():
    if request.method == 'POST':
        data = request.json
        database.update_user_data(data)
        return jsonify(data)


@app.route('/api/v1/sensor/data', methods=['POST', 'GET'])
def sensor_data():
    if request.method == 'POST':
        data = request.json
        database.update_sensor_data(data)
        return jsonify(data)


@app.route('/api/v1/location', methods=['GET'])
def user_location():
    user = request.args.get('user')
    return jsonify(database.location(user))


@app.route('/api/v1/users/nearby', methods=['GET'])
def user_nearby_location():
    loc = request.args.get('location')
    return jsonify(database.users_nearby(loc))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2001)
