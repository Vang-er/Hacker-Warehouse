from django.contrib import admin
from .models import Stock, StockMovement

# Register your models here.

from .models import Stock,StockMovement

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("variant", "quantity", "reorder_level", "location")
    readonly_fields = ("variant", "quantity")

    def has_add_permission(self, request):
        return False

@admin.register(StockMovement)
class StockMovmentAdmin(admin.ModelAdmin):
    list_display = ("created_at", "variant", "movement_type", "quantity", "balance_after", "reference")
    list_filter = ("movement_type", "reason")

    #def has_add_permission(self, request):
        #return False

    #def has_change_permission(self, request, obj = None):
        #return False

        #### THE ABOVE TO funcs... they are here for later to detirmine who has
        #Acess to the LOG!