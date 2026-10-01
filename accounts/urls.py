from django.urls import path
from .views import ApiLoginView, ApiLogoutView, login, logout, dashboard

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('login-api/', ApiLoginView.as_view(), name="login-api"),
    path('logout-api/', ApiLogoutView.as_view(), name="logout-api"),
]