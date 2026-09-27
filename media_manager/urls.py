from django.urls import path
from .views import PhotoUploadView

urlpatterns = [
    path("photos/upload", PhotoUploadView.as_view(), name="photo-upload")
]