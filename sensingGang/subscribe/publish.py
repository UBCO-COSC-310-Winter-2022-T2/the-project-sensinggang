import paho.mqtt.client as mqtt
from random import randrange, uniform
import time


def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
mqttBroker = "mqtt.eclipseprojects.io"
client1 = mqtt.Client("control1")
client1.on_publish = on_publish                          #assign function to callback
client1.connect(mqttBroker)
ret= client1.publish("house/bulb1","on")    