from rest_framework import serializers
from .models import Category, ProductVariant, Product
from media_manager.serializers import WithPhotosMixin

class VariantSerializer(WithPhotosMixin, serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()
    reorder_level = serializers.SerializerMethodField()
    product_name = serializers.CharField(source="product.name", read_only=True)
    stock_id = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariant
        fields = [
            "id", "product", "product_name", "sku", "name", 
            "price", "cost_price", "is_active", "quantity",
            "reorder_level", "stock_id"
        ]
        read_only_fields = ["sku"]

    def get_quantity(self, obj):
        return obj.stock.quantity if hasattr(obj, "stock") else 0

    def get_reorder_level(self, obj):
        return obj.stock.reorder_level if hasattr(obj, "stock") else 0

    def get_stock_id(self,obj):
        return obj.stock.id if hasattr(obj, "stock") else None

class ProductSerializer(WithPhotosMixin, serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True, default=None)
    variants = VariantSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name", "description", "brand", "category", "is_active", "variants", "category_name",]

class CategorySerializer(WithPhotosMixin, serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "description", "parent", "created_at", "updated_at", "products"]
