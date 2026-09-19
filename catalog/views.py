from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Category, Product, ProductVariant
from .serializers import CategorySerializer , VariantSerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = VariantSerializer