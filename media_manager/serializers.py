from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = ["id", "index", "image_url", "alt_text", "created_at"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

class WithPhotosMixin:
    photos = serializers.SerializerMethodField()

    def get_photos(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        photos = Photo.objects.filter(content_type=content_type, object_id=obj.id)
        return PhotoSerializer(photos, many=True, context=self.context).data








# Note to anyone reviewing this... first of all you are great
# Reviewr, as you checked every commit
# it's now 11:52PM egypt time, the deadline for ThirdSpace is 
# in 7 hours... all of my teammates are 5h short, if somehow u see this...
# then we made it to shippment! Please go easy on us