from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('sensorList', views.sensorList, name='sensorList'),
    path('subscribeClient', views.subscribeClient, name='subscribeClient'),
    
]