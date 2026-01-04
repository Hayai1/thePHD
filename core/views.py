from django.shortcuts import render
from .models import Tour


def home(request):
    tours = Tour.objects.all()
    return render(request, 'home.html', {'tours': tours})

def gigs(request):
    return render(request, "gigs.html")

def music(request):
    return render(request, "music.html")

def contact(request):
    return render(request, "contact.html")