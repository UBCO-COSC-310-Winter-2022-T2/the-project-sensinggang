import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    dataArray = [data]
    print("message received " ,data)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


# script to test methods
broker_address = "mqtt.eclipseprojects.io"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","test")
client.publish("house/bulbs/bulb1","off")
client.publish("house/bulbs/bulb1","on")
time.sleep(4) # wait
client.loop_stop() #stop the loop
