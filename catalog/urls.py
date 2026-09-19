from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet , ProductViewSet, VariantViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("products", ProductViewSet, basename="product")
router.register("variants", VariantViewSet, basename="variant")

urlpatterns = [path("", include(router.urls))]