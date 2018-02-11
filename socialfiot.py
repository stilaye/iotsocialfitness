from flask import Flask, request, jsonify
import database

app = Flask(__name__)


@app.route('/status')
def status():
    return "Social Fitness IoT"


@app.route('/api/v1/social')
def social():
    return "Hello World!"


@app.route('/api/v1/user/data')
def user_data():
    return "Hello World!"


@app.route('/api/v1/sensor/data', methods=['POST', 'GET'])
def sensor_data():
    if request.method == 'POST':
        data = request.json

        data_dict = {'user': data['user'],
                     'device_status': data["device_status"],
                     'device_id': data["device_id"],
                     'type': data["type"]}
        database.insert(data_dict)
        return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2001)
