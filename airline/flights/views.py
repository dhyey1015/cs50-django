from django.shortcuts import render
from .models import Flight, Passengers
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,"flights/index.html", {
        "flights" : Flight.objects.all(),
    })
    
def flight(request,flight_id):
    flight = Flight.objects.get(pk= flight_id)
    return render (request,"flights/flight.html",{
        "flight": flight,
        #"passengers": flight.passengers.get(),
        "non_passengers": Passengers.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk =flight_id)
        passenger = Passengers.object.get(pk=int(request.POST["passenger"]))
        passenger.flights.addI(flight)
        
        return HttpResponseRedirect(reverse("flight", args=(flight_id)))
    