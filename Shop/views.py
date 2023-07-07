from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *


class Mixin:
    # Class Mixin
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["products"] = Product.objects.all()
        context["category"] = Category.objects.all()
        return context
    

class ProductView(Mixin, ListView):
    # Output Produckt
    model = Product
    queryset = Product.objects.filter(available=False)
      

class CategoryView(Mixin, ListView):
    # Product listing by category
    model = Product
    template_name = 'Shop/product_list.html'
    
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['cat_slug'])
        return Product.objects.filter(category=category)
    
    
class ProductDetailView(Mixin, DetailView):
    # Full product description
    model = Product
    slug_field = 'slug'
    template_name = 'Shop/detail_list.html'