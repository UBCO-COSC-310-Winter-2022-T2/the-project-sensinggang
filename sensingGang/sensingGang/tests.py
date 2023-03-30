import unittest
import paho.mqtt.client as mqtt

client = mqtt.Client("test_client")

# Create your tests here.
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1 + 1, 2)

# Ensure that the client can connect to the broker and establish a stable connection
    def test_connectivity(self):        
        self.assertEqual(client.is_connected(), True)