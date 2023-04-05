from django.shortcuts import render, redirect
from django.http import HttpResponse
import paho.mqtt.client as mqtt
from django.contrib import messages
from .mqtt_script import mqtt_data_list # import the mqtt_data list from mqtt.py
import time
from queue import Queue
from random import randrange, uniform

#variables to transfer data
mqtt_data_list1 = [] # define the list to store the MQTT data sensor 1
mqtt_data_list2 = [] # define the list to store the MQTT data sensor 2
mqtt_data_list3 = [] # define the list to store the MQTT data sensor 3
received_messages = [] # define the list to store the MQTT data
q = Queue()

#flags for "subsctions" and displaying data
is_sub_s1 = False
is_sub_s2 = False
is_sub_s3 = False

def mqtt_data(request):
    # Render the data in a template
    return render(request, 'mqtt_data.html', {'mqtt_data_list1': mqtt_data_list1,'mqtt_data_list2': mqtt_data_list2,'mqtt_data_list3': mqtt_data_list3, 'is_sub_s1':is_sub_s1,'is_sub_s2':is_sub_s2,'is_sub_s3':is_sub_s3})

def subscribe(request):
    return render(request, "subscribe.html")

def sensorList(request):
    return render(request, "sensorList.html")

#on_message is callback function for receiving data as a subscriber
#could implement database inserts in this function
def on_message(client, userdata, message):
    q.put(message)
    if(message.topic=="sensor1"):
        mqtt_data_list1.append(message.payload.decode("utf-8"))
    else:
        if(message.topic=="sensor2"):
            mqtt_data_list2.append(message.payload.decode("utf-8"))
        else:
            if(message.topic=="sensor3"):
                 mqtt_data_list3.append(message.payload.decode("utf-8"))
    
    mqtt_data_list.append(message.payload.decode("utf-8"))
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    
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
#make client subscriptions
client.subscribe("sensor1")       #subscribe to topic *MUST BE SUBSCRIBED BEFORE PUBLISH TO RECEIVE MESSAGE*
client.subscribe("sensor2") 
client.subscribe("sensor3") 
#publish data sensor data (mock)
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("sensor1","s1-1")  #publish to topic sensor1
client.publish("sensor1","s1-2")  #publish to topic
client.publish("sensor1","s1-3")  #publish to topic

client.publish("sensor2","s2-1")  #publish to topic sensor2
client.publish("sensor2","s2-2")  #publish to topic
client.publish("sensor2","s2-3")  #publish to topic

count=0
#test with loop
while count<10:
    randNumber = uniform(20.0, 21.0)
    client.publish("sensor3", randNumber)
    time.sleep(1)
    count = count +1
    
# client.publish("sensor3","s3-2")  #publish to topic sensor3
# client.publish("sensor3","s3-2")  #publish to topic
# client.publish("sensor3","s3-3")  #publish to topic

time.sleep(4) #wait
client.loop_stop() #stop the loop
client.disconnect()

def subscribeClient(request):
    mqttBroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("admin")
    client.connect(mqttBroker)
    #verifying post request method
    if request.method == "POST":
        sensor1 = request.POST['sensor1']
        sensor2 = request.POST['sensor2']
        sensor3 = request.POST['sensor3']
        
        # Error checking for account creation
        errors = []
        if len(sensor1) == 0 and len(sensor2) == 0 and len(sensor3) == 0:
            errors.append("No Sensors")
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('subscribe')
        else:
            # subscribe to sensors object and saving it
            sensors = ""
            if(len(sensor1)!=0):
                global is_sub_s1
                is_sub_s1= True
                sensors = sensors + " " + sensor1
            else:
                is_sub_s1=False
            if(len(sensor2)!=0):
                global is_sub_s2 
                is_sub_s2 = True
                sensors = sensors + " " + sensor2
            else:
                is_sub_s2=False
            if(len(sensor3)!=0):
                global is_sub_s3 
                is_sub_s3= True
                sensors = sensors + " " + sensor3
            else:
                is_sub_s3=False
                

            # message for successful account creation
            messages.success(request, "Your have successfully subscribe to: " + sensors)
            return redirect('subscribe')

    return render(request, "mqtt_data.html")
