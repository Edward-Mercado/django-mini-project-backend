from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views are basically just api endpoints

def index(request):
    return HttpResponse("Hellooooo worldddd")