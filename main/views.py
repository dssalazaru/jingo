from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(response):
    return render(response, "main/base.html", {'name':'DSSU'})

def home(response):
    return render(response, "main/home.html", {'name':'DScode'})