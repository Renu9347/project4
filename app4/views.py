from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<marquee><h1>virat is the best batsman in the world</marquee></h1>')
