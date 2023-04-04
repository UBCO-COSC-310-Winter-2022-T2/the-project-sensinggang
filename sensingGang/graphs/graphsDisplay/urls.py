from django.urls import path
from . import views

urlpatterns = [
    # path('graphsDisplay/', views.graphsDisplay, name='graphsDisplay'),
    path('sensor_data/', views.sensor_data, name='sensor_data'),
]