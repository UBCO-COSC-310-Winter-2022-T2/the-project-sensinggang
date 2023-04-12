from django.shortcuts import render, redirect
from django.http import HttpResponse
import paho.mqtt.client as mqtt
from django.contrib import messages
#from .mqtt_script import mqtt_data_list # import the mqtt_data list from mqtt.py
import time, datetime
from queue import Queue
from random import randrange, uniform
from .models import Sensors, DataEntries, Entry
from django.template import loader

#variables to transfer data
mqtt_data_list1 = [] # define the list to store the MQTT data sensor 1
mqtt_data_list2 = [] # define the list to store the MQTT data sensor 2
mqtt_data_list3 = [] # define the list to store the MQTT data sensor 3
received_messages = [] # define the list to store the MQTT data
q = Queue()

#flags for "subscriptions" and displaying data
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
#stores data in data structures and database
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
    
    # create a new entry in the Entry model with the received messaged and the current time
    entry = Entry(topic=message.topic, data=message.payload.decode(), pub_date=datetime.datetime.now())
    entry.save()
    
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def init_client(client_name):
    client = mqtt.Client(client_id=client_name) #create new client instance
    # admin = Sensors(name=client)
    # admin.save()
    
    #attach callback functions:
    client.on_message=on_message        #attach on message function to callback
    client.on_connect=on_connect        #attach on_connect function to callback
    client.on_log=on_log                #attack on_log function to callback
    client.on_disconnect=on_disconnect  #attach disconnect callback
    client.on_subscribe=on_subscribe    #attach subscribe callback
    client.on_publish=on_publish        #attach publish callback
    return client
  
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("good connection, rc=", rc)
    else:
        print("Bad connection, returned code:", rc)
        
    #subcribe to topics when connected
    client.subscribe("sensor1")       #subscribe to topic *MUST BE SUBSCRIBED BEFORE PUBLISH TO RECEIVE MESSAGE*
    client.subscribe("sensor2") 
    client.subscribe("sensor3") 
    
def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_publish(client, userdata, mid):
    print("on_publish callback mid= ", str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed")
    
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code ", str(rc))

# generate_data method is used to set up our client and generate the data
def generate_data():
    #instantiate client and broker and sensor model
    print("creating new instance")
    broker_address = "mqtt.eclipseprojects.io"  #online broker
    client = init_client("admin")
   
    #connect, loop, publish, display results
    #note that callback functions are asynchronous on anoter thread so the order may not always appear logical (in logs)
    print("connecting to broker")
    client.connect(broker_address)              #connect to broker
    client.loop_start()                         #start the loop
    time.sleep(4)                               #give client time to establish connection

    #publish data sensor data (mock) - use loop to randomly generate data in lieu of being connected to real data generating sensors
    print("Publishing messages to topics")
    count=0
    while count<10:
        randNumber3 = uniform(20.0, 21.0)
        randNumber2 = uniform(10.0, 15.0)
        randNumber1 = uniform(0.0, 5.0)
        client.publish("sensor1", randNumber1)
        client.publish("sensor2", randNumber2)
        client.publish("sensor3", randNumber3)
        time.sleep(1)
        count = count +1

    #stop the loop and disconnect client
    time.sleep(4) #wait
    client.loop_stop()
    client.disconnect()

# view to display data from data structures in web page based on user selection of sensors - testing purposes only
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

# view to test database output - displays data pulled from database. For testing purposes only - real data displayed in graphs
def data_display_test(request):
    generate_data()
    entries = Entry.objects.all().values()
    template = loader.get_template('data_display_test.html')
    context = {
        'entries': entries,
    }
    return HttpResponse(template.render(context, request))
