from rest_framework import serializers
from .models import Category, ProductVariant, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "parent", "created_at", "updated_at"]

class VariantSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()
    reorder_level = serializers.SerializerMethodField()
    class Meta:
        model = ProductVariant
        fields = ["id", "product", "sku", "name", "price", "cost_price", "is_active", "quantity", "reorder_level"]
        read_only_fields = ["sku"]
    def get_quantity(self, obj):
        return obj.stock.quantity if hasattr(obj, "stock") else 0

    def get_reorder_level(self, obj):
        return obj.stock.reorder_level if hasattr(obj, "stock") else 0

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True, default=None)
    variants = VariantSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name", "description", "brand", "category","is_active", "variants"]