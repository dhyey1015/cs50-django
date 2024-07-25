from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.index,name ="index"),
    path("dhyey", views.dhyey, name="dhyey"),
    
]
