import unittest
from django.test import TestCase
import paho.mqtt.client as mqtt
from unittest import TestCase, mock
from subscribe.mqtt_client import MyMQTTClient

client = mqtt.Client("test_client")
mqttBroker = "mqtt.eclipseprojects.io"
mqtt_client = MyMQTTClient("test_client")

# Create your tests here.
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1 + 1, 5)
        
    def test_connection(self):
        client.connect(mqttBroker)
        # Call is_conected() built in function that returns t/f
        self.assertEqual(client.is_connected(), True)
        
    def test_disconnect(self):
        client.disconnect()
        self.assertEqual(client.is_connected(), False)
 
    def test_subscribe(self):
        # Define the expected arguments
        topic = 'test_topic'
        mqtt_client.subscribe(topic)
        self.assertEqual(mqtt_client.is_subscribed, True)
        
    def test_publish(self):
        self.assertEqual(1,2)
        
    def test_unsubscribe(self):
        topic = "test_topic"
        mqtt_client.subscribe(topic)
        mqtt_client.unsubscribe(topic)
        self.assertEqual(mqtt_client.is_subscribed, False)