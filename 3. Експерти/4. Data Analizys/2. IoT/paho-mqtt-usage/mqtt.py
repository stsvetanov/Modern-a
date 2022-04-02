import paho.mqtt.client as mqtt
from flask_app.utils import fill_db, send_data_to_web_app


def on_connect(client, userdata, rc, tp):
    client.subscribe('controller/#')


def on_message(client, userdata, message):
    payload = message.payload
    topic = message.topic

    # Each message is stored in the database
    fill_db(topic, payload)
    # Each message is processed and some detail might be sent to the web app
    send_data_to_web_app(topic, payload)


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect('mqtt.hpc.bg', 1883)
