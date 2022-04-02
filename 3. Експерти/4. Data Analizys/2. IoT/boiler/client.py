import paho.mqtt.client as mqtt

broker_address = "192.168.1.8"
    # broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1")  # create new instance
client.connect(broker_address, port=1883)  # connect to broker
    # client.publish("house/main-light", "OFF")  # publish
client.subscribe("temp_panel")
print(client.subscribe("temp_panel"))


msg = client.subscribe("temp_panel")
print(type(msg))

# [t] = struct.unpack('f', b"msg")
print(msg)

client.loop_forever()