from django.db.models import F, Sum
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from catalog.models import Category, Product
from .models import Stock

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def summary(request):
    stock = Stock.objects.all()
    return Response({
        "products": Product.objects.filter(is_active=True).count(),
        "categories": Category.objects.count(),
        "low_stock": stock.filter(quantity__lte=F("reorder_level")).count(),
        "units_on_hand": stock.aggregate(total=Sum("quantity"))["total"] or 0
    })