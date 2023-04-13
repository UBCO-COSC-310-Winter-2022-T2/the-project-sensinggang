from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('index', views.index, name='index'),
    path('sensorList', views.sensorList, name='sensorList'),
    path('subscribeClient', views.subscribeClient, name='subscribeClient'),
    path('mqtt_data/', views.mqtt_data, name='mqtt_data'),
    path('data_display_test/', views.data_display_test, name='data_display_test'),
]