from flask import Flask, request, jsonify
import database

app = Flask(__name__)
HEADERS = {'Cache-Control': 'private, max-age=0, no-cache', 'Content-type': 'application/json'}


@app.route('/status')
def status():
    return "Social Fitness IoT"


@app.route('/api/v1/social')
def social():
    # get data from mongo here and return like the json below
    # empty_coffee_machine = database.get_empty_coffee_machines()
    d = {
            "coffee_pot": [{
                "name": "atrium",
                "location": "atrium",
                "device_status": "empty"
            }],
            "peoples": [{
                "user": "sheshank kodam",
                "phone": "617-750-4465",
                "device_status": "empty",
                "email": "sheshank.kodam@gmail.com",
                "location": "room_name"
            }, {
                "user": "swapnil tilaye",
                "phone": "617-750-7777",
                "device_status": "empty",
                "email": "swapnil.tilaye@gmail.com",
                "location": "room_name"
            }]
        }
    return jsonify(d),


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2001)
