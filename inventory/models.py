from django.db import models

# Create your models here.

from django.conf import settings
from catalog.models import ProductVariant

class Stock(models.Model):
    variant = models.OneToOneField(ProductVariant, on_delete=models.CASCADE, related_name="stock")
    quantity = models.IntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=80, blank=True, help_text="Shelf code.")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.variant.sku}: {self.quantity}"


class StockMovement(models.Model):
    class Type(models.TextChoices):
        IN = "IN", "Stock in"
        OUT = "OUT", "Stock out"
        ADJUST = "ADJUST", "Adjustment"

    class Reason(models.TextChoices):
        RECEIPT = "RECEIPT", "Goods received"
        SALE = "SALE", "Sale"
        RETURN = "RETURN", "Customer return"
        COUNT = "COUNT", "Stock count"
        DAMAGE = "DAMAGE", "Damage or loss"
        MANUAL = "MANUAL", "Manual correction"

    variant = models.ForeignKey(ProductVariant, on_delete=models.PROTECT, related_name="movements")
    movement_type = models.CharField(max_length=10, choices=Type.choices)
    reason = models.CharField(max_length=20, choices=Reason.choices, default=Reason.MANUAL)
    quantity = models.IntegerField(help_text="Positive to add, Negative to remove.")
    balance_after = models.IntegerField()
    reference = models.CharField(max_length=64, blank=True, help_text="Invoice or receipt number.")
    note = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movement_type} {self.quantity:+d} on {self.variant.sku}"