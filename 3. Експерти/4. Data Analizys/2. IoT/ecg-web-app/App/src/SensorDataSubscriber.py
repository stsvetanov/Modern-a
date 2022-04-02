import paho.mqtt.client as mqtt

class SensorDataSubscriber:
    MQTT_CLIENT_NAME = 'web_app'
    MQTT_BROKER_HOST = 'localhost'
    MQTT_BROKER_PORT = 1883
    MQTT_TOPIC = 'ecg_data'

    def __init__(self, userdata):
        self.client =  self.__create_MQTT_client(userdata)

    def __create_MQTT_client(self, userdata):
        client = mqtt.Client(self.MQTT_CLIENT_NAME, userdata=userdata)
        client.on_message = self.__on_message
        client.on_connect = self.__on_connect
        return client

    def __on_connect(self, client, userdata, flags, rc):
        print("Connected to broker.")
        client.subscribe(self.MQTT_TOPIC)

    def __on_message(self, client, userdata, msg):
        analyzer = userdata['analyzer']
        socketio = userdata['socketio']

        payload = float(msg.payload)
        analyzer.appendData(payload)
        socketio.emit('ecg_sample', payload)

        if analyzer.getSamples() % 50 == 0:
            try:
                print(analyzer.getSamples())
                analyzedResult = analyzer.analyzeData()
                print(analyzedResult)
                socketio.emit('ecg_analysis', analyzedResult, broadcast=True)
            except:
                print("Couldn't analyze data...")
        
    def run(self):
        self.client.connect(self.MQTT_BROKER_HOST, self.MQTT_BROKER_PORT, 60)
        self.client.loop_start()
