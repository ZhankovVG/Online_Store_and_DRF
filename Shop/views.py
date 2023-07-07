from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class Mixin:
    # Class Mixin
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['products'] = Product.objects.all()
        context["category"] = Category.objects.all()
        return context
    

class ProductView(Mixin, ListView):
    # Output Produckt
    model = Product
    queryset = Product.objects.filter(available=False)
      

class CategoryView(Mixin, ListView):
    # Product listing by category
    model = Product
    template_name = 'product_list.html'