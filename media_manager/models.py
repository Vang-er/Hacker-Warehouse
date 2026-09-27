from django.db import models

# Create your models here.

import os 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

def product_photo_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"uploads/{instance.content_type.model}/{instance.object_id}/{instance.index}_{filename}"

class Photo(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    image = models.ImageField(upload_to=product_photo_path)
    index = models.PositiveBigIntegerField(default=0, help_text="order index for the photo")
    alt_text = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['index', 'id']

    def __str__(self):
        return f"Photo {self.index} for {self.content_type.model} #{self.object_id}"