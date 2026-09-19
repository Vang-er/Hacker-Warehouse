from django.db.models.signals import post_save
from django.dispatch import receiver
from catalog.models import ProductVariant

from .models import Stock



@receiver(post_save, sender=ProductVariant)
def create_stock_row(sender, instance, created, **kwrgs):
    if created:
        Stock.objects.get_or_create(variant=instance)