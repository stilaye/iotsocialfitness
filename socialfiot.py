from flask import Flask
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


@app.route('/api/v1/sensor/data')
def sensor_data():
    return "Hello World!"    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2001)