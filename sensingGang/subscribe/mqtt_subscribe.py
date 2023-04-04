import paho.mqtt.client as mqtt
import time
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

client.loop_start()
client.subscribe("topic")
client.on_message = on_message
time.sleep(3)
client.loop_stop()
