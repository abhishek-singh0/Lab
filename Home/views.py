from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')


def login(request):
    return render(request, 'home/login.html')

def register(request):
    return render(request, 'home/register.html')


def about(request):
    return render(request, 'home/about.html')


