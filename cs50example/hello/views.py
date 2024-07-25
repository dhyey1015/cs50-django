from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def dhyey(request):
    return HttpResponse("hello! dhyey")

def greet(request, name):
    
    context = {
        "name": name
    }
    return render(request, "hello/greet.html")