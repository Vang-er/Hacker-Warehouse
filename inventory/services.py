from django.db import transaction
from .models import Stock, StockMovement

class InsufficientStockError(Exception):
    "Raised when a movment would push stock below zero"

@transaction.atomic
def apply_movement(*, variant, delta, movement_type, reason, note="", user=None, reference=""):
    stock = Stock.objects.select_for_update().get(variant=variant)
    new_quantity = stock.quantity + delta

    if new_quantity < 0:
        raise InsufficientStockError(
            f"Not Enough stock for {variant.sku}: {stock.quantity} on hand, {abs(delta)} requested..."
        )
    stock.quantity = new_quantity
    stock.save()

    return StockMovement.objects.create(
        variant=variant,
        movement_type=movement_type,
        reason=reason,
        quantity=delta,
        balance_after=new_quantity,
        reference=reference,
        note=note,
        created_by=user,
    )

def set_quantity(*, variant,counted_quantity, user=None, note=""):
    current = variant.stock.quantity
    delta = counted_quantity - current
    if delta ==0:
        return None
    return apply_movement(
        variant=variant,
        delta=delta,
        movement_type=StockMovement.Type.ADJUST,
        reason=StockMovement.Reason.COUNT,
        user=user,
        note=note,
    )