from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse('<center><h1>Jingo</h1><center>')

def dssu(response):
    return HttpResponse('<center><h1>DSSU</h1><center>')

def test(response):
    return HttpResponse('<center><h1>DSSU TEST</h1><center>')