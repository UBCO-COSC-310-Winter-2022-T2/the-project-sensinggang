from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sensorList', views.sensorList, name='sensorList'),
    path('subscribeForm', views.subscribeForm, name='subscribeForm'),
]