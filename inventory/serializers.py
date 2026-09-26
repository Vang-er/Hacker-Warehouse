from rest_framework import serializers
from .models import Stock, StockMovement

class StockSerializer(serializers.ModelSerializer):
    sku = serializers.CharField(source="variant.sku", read_only=True)
    variant_name = serializers.SerializerMethodField()
    class Meta:
        model = Stock
        fields = ["id", "variant", "sku", "quantity", "reorder_level", "location"]
        read_only_fields = ["quantity", "variant"]
        
    def get_variant_name(self, obj):
        return obj.variant.name or obj.variant.product.name

class StockMovementSerializer(serializers.ModelSerializer):
    variant_name = serializers.SerializerMethodField()
    sku = serializers.CharField(source="variant.sku", read_only=True)

    class Meta:
        model = StockMovement
        fields = ["id", "variant", "sku", "variant_name", "movement_type", "reason", "quantity",
                  "balance_after", "reference", "note", "created_by", "created_at"]
        read_only_fields = fields

    def get_variant_name(self, obj):
        return obj.variant.name or obj.variant.product.name
    
class ReceiveStockSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
    note = serializers.CharField(required=False,allow_blank=True,default="")

class IssueStockSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
    note = serializers.CharField(required=False, allow_blank=True, default="")

class CountStockSerializer(serializers.Serializer):
    counted_quantity = serializers.IntegerField(min_value=0)
    note = serializers.CharField(required=False, allow_blank=True, default="")