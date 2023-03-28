import paho.mqtt.client as mqtt

class MyMQTTClient:

    is_subscribed = False
    
    def __init__(self, client_id):
        self._mqtt_client = mqtt.Client(client_id)
        
    def subscribe(self, topic):
        self._mqtt_client.subscribe(topic)
        self.is_subscribed = True
        
    def unsubscribe(self, topic):
        self._mqtt_client.unsubscribe(topic)
        self.is_subscribed = False

    def _on_message(self, client, userdata, message):
        # Do something with the received message
        print(f"Received message on topic {message.topic}: {message.payload}")
