from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer


def index(request):
   #return render(request, "products/index.html")
   products = Product.objects.all()
   return render(request, "index.html", {"pro": products})
   #return HttpResponse(index.html)
    