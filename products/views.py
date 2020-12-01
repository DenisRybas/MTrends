from django.shortcuts import render
from .models import Product


def home(request):
    context = {
        'posts': Product.objects.all()
    }
    return render(request, 'products/home.html', context)


def about(request):
    return render(request, 'products/about.html', {'title': 'About'})
