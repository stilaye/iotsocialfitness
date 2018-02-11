from flask import Flask, request, jsonify
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


@app.route('/api/v1/sensor/data',methods = ['POST', 'GET'])
def sensor_data():
	if request.method == 'POST':
		return jsonify(request.json)   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2001)