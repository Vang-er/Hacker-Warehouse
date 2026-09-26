from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import StockMovementViewSet,StockViewSet
from .dashboard import summary

router = DefaultRouter()
router.register("stock", StockViewSet, basename="stock")
router.register("stock-movements", StockMovementViewSet,basename="stock-movement")

urlpatterns= [path("", include(router.urls))]
urlpatterns += [path("dashboard/summary/", summary, name="dashboard-summary")]