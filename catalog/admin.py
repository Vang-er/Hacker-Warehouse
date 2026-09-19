from django.contrib import admin
from .models import Category, Product, ProductVariant

# Register your models here.


class VariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category", "is_active")
    list_filter = ("is_active", "category")
    search_fields = ("name", "brand")
    inlines = [VariantInline]