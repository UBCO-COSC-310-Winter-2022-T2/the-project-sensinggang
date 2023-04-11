# import paho.mqtt.client as mqtt
# from random import randrange, uniform
# import time

# mqttBroker = "mqtt.eclipseprojects.io"
# client2 = mqtt.Client("TestClient")
# client2.connect(mqttBroker)
# count = 0
# topic = "topic"

# while count<10:
#     randNumber = uniform(20.0, 21.0)
#     client2.publish(topic, randNumber)
#     print("Just published " + str(randNumber) + " to Topic: " + topic)
#     time.sleep(1)
#     count = count +1
