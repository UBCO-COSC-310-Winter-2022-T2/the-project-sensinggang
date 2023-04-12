from django.db import models
from datetime import date

# Create your models here.
class Sensors(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class DataEntries(models.Model):
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    data = models.TextField()
    pub_date = models.DateField()
    
class Entry(models.Model):
    topic = models.CharField(max_length=255)
    data = models.TextField()
    pub_date = models.DateField()
