from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def gigs(request):
    return render(request, "gigs.html")

def music(request):
    return render(request, "music.html")

def contact(request):
    return render(request, "contact.html")