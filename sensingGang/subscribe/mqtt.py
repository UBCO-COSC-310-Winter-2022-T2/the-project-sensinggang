import paho.mqtt.client as mqtt
import time
from queue import Queue

mqtt_data_list = [] # define the list to store the MQTT data
q = Queue()

def on_message(client, userdata, message):
    q.put(message)
    mqtt_data_list.append(message.payload.decode("utf-8"))
    # print("message received " ,str(message.payload.decode("utf-8")))
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)
    
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("good connection, rc=", rc)
    else:
        print("Bad connection, returned code:", rc)
    
def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_publish(client, userdata, mid):
    print("on_publish callback mid= ", str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed")
    
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code ", str(rc))

# script to test methods
#instantiate client and broker
print("creating new instance")
broker_address = "mqtt.eclipseprojects.io"  #online broker
client = mqtt.Client("P1") #create new instance

#attach callback functions:
client.on_message=on_message        #attach function to callback
client.on_connect=on_connect        #attach function to callback
client.on_log=on_log                #attack function to callback
client.on_disconnect=on_disconnect  #attach disconnect callback
client.on_subscribe=on_subscribe    #attach subscribe callback
client.on_publish=on_publish        #attach publish callback

#connect, loop, subscribe, publish, display results
#note that callback functions are asynchronous on anoter thread so the order may not always appear logical (in logs)
print("connecting to broker")
client.connect(broker_address)              #connect to broker
client.loop_start()                         #start the loop
time.sleep(4)                               #give client time to establish connection
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")       #subscribe to topic *MUST BE SUBSCRIBED BEFORE PUBLISH TO RECEIVE MESSAGE*
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","test")  #publish to topic
client.publish("house/bulbs/bulb1","off")
client.publish("house/bulbs/bulb1","on")
while not q.empty():                        #while loop to print received messages using queue, global scope
   message = q.get()
   if message is None:
       continue
   print("received from queue",str(message.payload.decode("utf-8")))
time.sleep(4) # wait
client.loop_stop() #stop the loop
client.disconnect()
