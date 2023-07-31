from rest_framework import serializers
from .models import *


class ProductListSerializer(serializers.ModelSerializer):
    # list products
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category')
        
        
class ProductDetailSerializer(serializers.ModelSerializer):
    # full product
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    
    class Meta:
        model = Product
        exclude = ('available', )