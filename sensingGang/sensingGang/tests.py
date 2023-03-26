#from django.test import TestCase
import pytest
import time

# Create your tests here.

#from django.test import TestCase
import paho.mqtt.client as mqtt
import ssl

# Set up MQTT client


# Test cases
@pytest.fixture(scope='module')

def test_connectivity(self):        # Ensure that the client can connect to the broker and establish a stable connection
    self.assertEqual(client.is_connected(), True)