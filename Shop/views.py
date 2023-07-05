from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class ProductView(ListView):
    # Output Produckt
    model = Product
    queryset = Product.objects.filter(available=False)
