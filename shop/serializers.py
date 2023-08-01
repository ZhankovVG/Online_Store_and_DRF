from rest_framework import serializers
from .models import *


class ProductListSerializer(serializers.ModelSerializer):
    # List products
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category')
        
        
class ReviewCreateSerializer(serializers.ModelSerializer):
    # adding a review
    class Meta:
        model = Review
        fields = '__all__'
        
        
class ReviewSeridlizer(serializers.ModelSerializer):
    # Output coments
    class Meta:
        model = Review
        fields = ('name', 'text', 'perent')
    
        
class ProductDetailSerializer(serializers.ModelSerializer):
    # Full product
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewCreateSerializer(many=True)
    
    class Meta:
        model = Product
        exclude = ('available', )