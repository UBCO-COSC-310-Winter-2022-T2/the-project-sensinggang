import unittest
from django.test import TestCase
import paho.mqtt.client as mqtt

client = mqtt.Client("test_client")
# Create your tests here.
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1 + 1, 5)
        
    def test_connection(self):
        
        # Call is_conected() built in function that returns t/f
        self.assertEqual(client.is_connected(), True)
        
    def test_subscribe(self, mock_subscribe):
        # Define the expected arguments
        topic = 'mytopic'
        qos = 0

        # Call the subscribe function with the expected arguments
        client.subscribe(topic, qos)

        # Assert that the MQTT client's subscribe method was called with the expected arguments
        mock_subscribe.assert_called_once_with(topic, qos)
