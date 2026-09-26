from django.shortcuts import render

# Create your views here.

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Stock,StockMovement
from .serializers import (
    CountStockSerializer, IssueStockSerializer, ReceiveStockSerializer,
    StockMovementSerializer, StockSerializer,
)
from .services import InsufficientStockError, apply_movement, set_quantity

class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.select_related("variant")
    serializer_class = StockSerializer

    def get_serializer_class(self):
        if self.action == "receive":
            return ReceiveStockSerializer
        if self.action == "issue":
            return IssueStockSerializer
        if self.action == "count":
            return CountStockSerializer
        return StockSerializer

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


    @action(detail=True, methods=["post"])
    def count(self, request, pk=None):
        stock = self.get_object()
        body = CountStockSerializer(data=request.data)
        body.is_valid(raise_exception=True)
        movement = set_quantity(
            variant=stock.variant, counted_quantity=body.validated_data["counted_quantity"],
            user=request.user, note=body.validated_data["note"],
        )
        if movement is None:
            return Response({"detail": "Counted quantity matches the system. Nothing changed."})
        return Response(StockMovementSerializer(movement).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"])
    def issue(self, request, pk=None):
        stock = self.get_object()
        body = IssueStockSerializer(data=request.data)
        body.is_valid(raise_exception=True)
        try:
            movement = apply_movement(
                variant=stock.variant,
                delta= -body.validated_data["quantity"],
                movement_type=StockMovement.Type.OUT,
                reason=StockMovement.Reason.DAMAGE,
                user=request.user,
                note=body.validated_data["note"],
            )
            return Response(StockMovementSerializer(movement).data, status=status.HTTP_201_CREATED)
        except InsufficientStockError as exc:
            return Response({"detail": str(exc)},status=status.HTTP_400_BAD_REQUEST)

class StockMovementViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StockMovementSerializer
    def get_queryset(self):
        queryset = StockMovement.objects.select_related("variant")
        variant_id = self.request.query_params.get("variant")

        if variant_id:
            queryset = queryset.filter(variant_id=variant_id)
        movement_type = self.request.query_params.get("movement_type")
        if movement_type:
            queryset = queryset.filter(movement_type=movement_type)

        reason = self.request.query_params.get("reason")
        if reason:
            queryset = queryset.filter(reason=reason)

        return queryset