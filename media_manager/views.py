from rest_framework import status, views, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from .models import Photo
from .serializers import PhotoSerializer

class PhotoUploadView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        model_name = request.data.get("model_name") # e.g. "product", "category", "productvariant"
        object_id = request.data.get("object_id")
        image = request.FILES.get("image")
        index = request.data.get("index", 0)
        alt_text = request.data.get("alt_text", "")

        if not model_name or not object_id or not image:
            return Response(
                {"detail": "Fields 'model_name', 'object_id', and file 'image' are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            content_type = ContentType.objects.get(
                app_label__in=["catalog", "inventory", "accounts"], 
                model=model_name.lower().strip()
            )
            model_class = content_type.model_class()
            target_obj = model_class.objects.get(pk=object_id)
        except (ContentType.DoesNotExist, model_class.DoesNotExist, ValueError):
            return Response({"detail": "Target object or model not found."}, status=status.HTTP_404_NOT_FOUND)

        photo = Photo.objects.create(
            content_object=target_obj,
            image=image,
            index=index,
            alt_text=alt_text
        )

        return Response(PhotoSerializer(photo, context={"request": request}).data, status=status.HTTP_201_CREATED)