from django import forms 
from django.shortcuts import render


tasks = ['foo', 'bar', 'baz']

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
# Create your views here.

def index(request):
    context = {
        'tasks':tasks
    }
    return render(request, "tasks/index.html",context)

def add(request):
    
    context = {
        "form": NewTaskForm()
    }
    return render(request, "tasks/add.html",context)
    
