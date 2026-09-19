from rest_framework import serializers
from .models import Category, ProductVariant, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "parent", "created_at", "updated_at"]

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ["id", "product", "sku", "name", "price", "cost_price", "is_active"]
        read_only_fields = ["sku"] 

class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name", "description", "brand", "category","is_active", "variants"]