from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product, ProductVariant
from .serializers import CategorySerializer , VariantSerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=["get"])
    def tree(self, request):
        categories = list(Category.objects.all())
        by_parent = {}
        for c in categories:
            by_parent.setdefault(c.parent_id, []).append(c)

        def build(parent_id):
            return [
                {"id": c.id, "name": c.name, "children": build(c.id)}
                for c in by_parent.get(parent_id, [])
            ]
        return Response(build(None))

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category")
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "brand"]

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.query_params.get("category")
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs

class VariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = VariantSerializer