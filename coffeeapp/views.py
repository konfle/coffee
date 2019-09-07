from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'coffeeapp/index.html', {})

def brewing(request):
    return render(request, 'coffeeapp/brewing.html', {})