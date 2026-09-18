from django.contrib import admin

# Register your models here.

from .models import Stock,StockMovement

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("variant", "quantity", "reorder_level", "location")

@admin.register(StockMovement)
class StockMovmentAdmin(admin.ModelAdmin):
    list_display = ("created_at", "variant", "movement_type", "quantity", "balance_after", "reference")
    list_filter = ("movement_type", "reason")