import http
from urllib import response
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

