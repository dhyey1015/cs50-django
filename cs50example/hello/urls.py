from django.urls import path
from . import views

urlpatterns = [
    
    #path("",views.index,name ="index"),
    path("dhyey", views.dhyey, name="dhyey"),
    #path("<str:name>", views.greet, name = "greet"),
    
# userinterface lecture----------------------------------------------
    path("singlepage", views.singlepage, name= "singlepage"),
    path("singlepage2", views.singlepage2, name="singlepage2"),
    path("sections/<int:num>", views.section, name= "sections"),
    path("section/<int:num1>", views.section, name='section'),
    path("scroll", views.scroll, name="scroll")
    
]
