# from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse
from .models import SensorData
from datetime import datetime, timedelta

class SensorData(TestCase):
    def setUp(self):
        # Create some test data
        now = datetime.now()
        self.sensor1_data = SensorData.objects.create(
            timestamp=now - timedelta(hours=1),
            temperature = 20.0,
            humidity=25.0
        )
        self.sensor2_data = SensorData.objects.create(
            timestamp=now,
            temperature = 25.0,
            humidity=30.0
        )

    def test_sensor_data_graph_view(self):
        # Send a GET request to the sensor data graph view
        response = self.client.get(reverse('sensor_data'))
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the expected chart data
        expected_data = [
            {'x': self.sensor1_data.timestamp.isoformat(), 'y': self.sensor1_data.value},
            {'x': self.sensor2_data.timestamp.isoformat(), 'y': self.sensor2_data.value},
        ]
        self.assertJSONEqual(response.content.decode(), {'data': expected_data})
