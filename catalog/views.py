from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product, ProductVariant
from .serializers import CategorySerializer, VariantSerializer, ProductSerializer
from accounts.models import User

from inventory.models import StockMovement


class IsNotViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsNotViewer]

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
    permission_classes = [IsNotViewer]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "brand"]

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.request.query_params.get("category")
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs

    def perform_create(self, serializer):
        product = serializer.save()

    def perform_destroy(self, instance):
        StockMovement.objects.filter(variant__product=instance).delete()
        instance.delete()


class VariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = VariantSerializer
    permission_classes = [IsNotViewer]
    def perform_destroy(slef, instance):
        StockMovement.objects.filter(variant=instance).delete()
        instance.delete()


"""
Hi, we have somehow made it to week 3... it's now 12:51 AM , The deadline is
in 6h... one of my teammates has 5.7h logged only, so he has to work like 4h straigt
IT IS HARD, but it's possiable (HOPEFULLY)
If u can see this, GO EASY ON US PLEASEEEEEE, we've spent 90h in that project
It may look simple but working in a team made it harder than expected.
whether it's acepted or not, I'm greatful that I met those great guys
also I love being a hackclubber even without any prizes!!!
"""

# Uh also, Being in a huddl for 9h straight is not that healthy