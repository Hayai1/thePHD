from django.shortcuts import render
from .models import Tour


def home(request):
    tours = Tour.objects.all()
    tours = [tour for tour in tours]
    for tour in tours:
        tour.venue = tour.venue.upper()
        tour.date = tour.date.strftime("%d %b %Y").upper()
        print("TOUR DATE:", tour.date)
        tour.city = tour.city.upper()
        tour.country = tour.country.upper()
    return render(request, 'home.html', {'tours': tours})

def gigs(request):
    return render(request, "gigs.html")

def music(request):
    return render(request, "music.html")

def contact(request):
    return render(request, "contact.html")