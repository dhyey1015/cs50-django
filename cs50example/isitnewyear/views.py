from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    context = {
        "newyear": datetime.datetime(2025,1,1) == datetime.datetime.now()
    }
    return render(request, "isitnewyear/index.html",context)
    
