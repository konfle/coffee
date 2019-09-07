from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'coffeeapp/index.html', {})

def brewing(request):
    return render(request, 'coffeeapp/brewing.html', {})

def roasting(request):
    return render(request, 'coffeeapp/roasting.html', {})

def grinding(request):
    return render(request, 'coffeeapp/grinding.html', {})

def drinks(request):
    return render(request, 'coffeeapp/drinks.html', {})

def survey(request):
    return render(request, 'coffeeapp/survey.html', {})