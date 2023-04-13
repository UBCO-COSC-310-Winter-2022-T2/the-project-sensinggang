from django.shortcuts import render, redirect
from django.http import HttpResponse

def homePage(request):
    return render(request, "homePage/homePageTemplate.html")
