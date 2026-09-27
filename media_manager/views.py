from django.shortcuts import render

# Create your views here.

from rest_framework import status, views, permissions
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from .models import Photo
from .serializers import PhotoSerializer

class PhotoUploadView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        model_name = request.data.get("model_name")
        object_id = request.data.get("object_id")
        image = request.FILES.get("image")
        index = request.data.get("index", 0)
        alt_text = request.data.get("alt_text", "")

        if not model_name or not object_id or not image:
            return Response({"detail": "model_name, object_id, and image are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            content_type = ContentType.objects.get(app_label_in=["catalog", "inventory","accounts"], model=model_name.lower())
            model_name = content_type.model_class()
            target_obj = model_name.object.get(pk=object_id)
        except (ContentType.DoesNotExist, model_name.DoesNotExist):
            target_obj = None

        if not target_obj:
            return Response({"detail":"Target Object not found."}, status=status.HTTP_404_NOT_FOUND)

        photo = Photo.objects.create(
            content_object=target_obj,
            image=image,
            index=index,
            alt_text=alt_text,
        )
        return Response(PhotoSerializer(photo, context={"request": request}).data, status=status.HTTP_201_CREATED)


        