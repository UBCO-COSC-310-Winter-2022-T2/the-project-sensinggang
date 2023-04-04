from django.shortcuts import render, redirect
from django.http import HttpResponse
import paho.mqtt.client as mqtt
from django.contrib import messages

# def subscribe(request):
#     return HttpResponse("Hello world!")
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("username")
client.connect(mqttBroker)

def subscribe(request):
    return render(request, "subscribe.html")

def sensorList(request):
    return render(request, "sensorList.html")

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    dataArray = [data]
    print("message received " ,data)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def subscribeClient(request):
    data= ""
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
                client.subscribe(sensor1)
                data = data + client.publish(sensor1, "testS1")
                sensors = sensors + sensor1
                print("You have subscribed to " + sensor1)
            if(len(sensor2)!=0):
                client.subscribe(sensor2)
                data = data + client.publish(sensor2, "testS2")
                sensors = sensors + " " + sensor2
                print("You have subscribed to " + sensor2)
            if(len(sensor3)!=0):
                client.subscribe(sensor3)
                data = data + client.publish(sensor3, "testS3")
                sensors = sensors + " " + sensor3
                print("You have subscribed to " + sensor3)

            # message for successful account creation
            messages.success(request, "Your have successfully subscribe to: " + sensors + data)
            return redirect('subscribe')

    return render(request, "subscribe.html")
