from django.http import response
from django.shortcuts import render

# Create your views here.

def home(response):
    return render(response, "main/index.html")
