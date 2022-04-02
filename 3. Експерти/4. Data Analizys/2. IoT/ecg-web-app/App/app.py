import eventlet
from eventlet import wsgi
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

from src.SensorDataSubscriber import SensorDataSubscriber
from src.ECGAnalyzer import ECGAnalyzer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode='eventlet')

mqttEventsCustomData = {
    'analyzer': ECGAnalyzer(),
    'socketio': socketio
}

@app.route('/')
def index():   
    return render_template("index.html")

subsciber = SensorDataSubscriber(mqttEventsCustomData)
subsciber.run()

socketio.run(app)
wsgi.server(eventlet.listen(('', 8000)), app)