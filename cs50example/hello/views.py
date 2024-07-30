from django.shortcuts import render
from django.http import HttpResponse,Http404, JsonResponse
import time
# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def dhyey(request):
   return HttpResponse("hello! dhyey")

def greet(request, name): 
    context = {
        "name": name
    }
    return render(request, "hello/greet.html",context)
#userinterface lectures----------------------------------------------------

#single-page-web-application
texts = ["page1beuwinjokl;A", "page2BFUNIEWOMKL,Q", "page3eubinjkwclm"]

def singlepage(request):
    return render(request, "hello/singlepage.html")

def singlepage2(request):
    return render(request, "hello/singlepage2.html")

def section(request,num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num -1])
    else:
        raise Http404("No Such Section!!")
    
#scroll color change-----------------------------
    
def scroll(request):
    return render(request,"hello/scroll.html")

#infinite scroll-----------------------------------

def hscroll(request):
    return render(request, "hello/hscroll.html")

def posts(request):
    
    #get start and end point
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or start + 9)
    
    #generate post according to given start and end points
    data = []
    for i in range(start, end + 1):
        data.append(f"Post#{i}")
        
    #delay speed of response manually    
    time.sleep(1)
    
    return JsonResponse({
        'posts': data
    })
    
    
    
def hide(request):
    return render(request, "hello/hide.html")

    
    

    