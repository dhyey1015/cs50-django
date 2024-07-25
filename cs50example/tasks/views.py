from django import forms 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label= "Priority", min_value=1, max_value=10)
# Create your views here.

def index(request):
    
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    context = {
        'tasks':request.session["tasks"]
    }
    return render(request, "tasks/index.html",context)

def add(request):
    
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["tasks"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("index"))
            
        else:
            context= {
                "form":form
            }
            return render(request, "task/add.html",context)
    
    context = {
        "form": NewTaskForm()
    }
    return render(request, "tasks/add.html",context)
    
