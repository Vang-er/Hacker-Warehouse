from rest_framework import serializers
from .models import Stock, StockMovement

class StockSerializer(serializers.ModelSerializer):
    sku = serializers.CharField(source="variant.sku", read_only=True)

    class Meta:
        model = Stock
        fields = ["id", "variant", "sku", "quantity", "reorder_level", "location"]
        read_only_fields = ["quantity", "variant"]

class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ["id", "variant", "movement_type", "reason", "quantity",
                "balance_after", "referemce", "note",
                "created_by", "created_at"]
        read_only_fields = fields

class ReceiveStockSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
    note = serializers.CharField(required=False,allow_blank=True,default="")