from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"core/index.html")

def destinations(request):
    return render(request,"core/destinations.html")

def events(request):
    return render(request,"core/events.html")

def us(request):
    return render(request,"core/us.html")

def contact(request):
    return render(request,"core/contact.html")

def eat(request):
    return render(request,"core/eat.html")

def accommodation(request):
    return render(request,"core/accommodation.html")


