import csv
import time
import paho.mqtt.client as mqtt


class SensorMock:
    MQTT_CLIENT_NAME = 'sensor'
    DATA_FILE_NAME = 'data.csv'
    MQTT_BROKER_HOST = 'localhost'
    MQTT_BROKER_PORT = 1883
    MQTT_TOPIC = 'ecg_data'
    
    def __init__(self):
        self.client = self.__create_MQTT_client()
    
    def __create_MQTT_client(self):
        client = mqtt.Client(self.MQTT_CLIENT_NAME)
        client.on_connect = self.__on_connect
        return client

    def __on_connect(self, client, userdata, flags, rc):
        print("Connected to broker.")
 
    def run(self):
        self.client.connect(self.MQTT_BROKER_HOST, self.MQTT_BROKER_PORT, 60)
        self.client.loop_start()
        
        while(True):
            with open(self.DATA_FILE_NAME, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    time.sleep(0.05)
                    self.client.publish(self.MQTT_TOPIC, row[0]) 
                
                