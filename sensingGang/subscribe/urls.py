from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('index', views.index, name='index'),
    path('sensorList', views.sensorList, name='sensorList'),
    path('sensorRemove', views.sensorRemove, name='sensorRemove'),    
    path('subscribeClient', views.subscribeClient, name='subscribeClient'),
    path('subscribeForm', views.subscribeForm, name='subscribeForm'),
    path('unsubscribeForm', views.unsubscribeForm, name='unsubscribeForm'),
    path('mqtt_data/', views.mqtt_data, name='mqtt_data'),
    path('data_display_test/', views.data_display_test, name='data_display_test'),
]