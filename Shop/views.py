from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class ProductView(ListView):
    # Output Produckt
    model = Product
    queryset = Product.objects.filter(available=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context