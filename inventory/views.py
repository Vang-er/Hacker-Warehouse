from django.shortcuts import render

# Create your views here.

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Stock,StockMovement
from .serializers import ReceiveStockSerializer, StockMovementSerializer, StockSerializer
from .services import InsufficientStockError, apply_movement

class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.select_related("variant")
    serializer_class = StockSerializer

    @action(detail=True, methods=["post"])
    def receive(self,request, pk=None):
        stock = self.get_object()
        body = ReceiveStockSerializer(data=request.data)
        body.is_valid(raise_exception=True)

        movement = apply_movement(
            variant=stock.variant,
            delta=body.validated_data["quantity"],
            movement_type=StockMovement.Type.IN,
            reason=StockMovement.Reason.MANUAL,
            user=request.user,
            note=body.validated_data["note"],
        )
        return Response(StockMovementSerializer(movement).data, status=status.HTTP_201_CREATED)

class StockMovementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StockMovement.objects.select_related("variant")
    serializer_class = StockMovementSerializer