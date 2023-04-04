from django.db import models

# Create your models here.

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    
    def __str__(self):
        return f'SensorData at {self.timestamp}: temp={self.temperature}, humidity={self.humidity}'
    
    class Meta:
        app_label = 'graphsDisplay'