from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. Here soon will be cards with animal's info")