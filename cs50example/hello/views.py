from django.shortcuts import render
from django.http import HttpResponse,Http404
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

#singel-page all infromation

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
    
def scroll(request):
    return render(request,"hello/scroll.html")

    

    