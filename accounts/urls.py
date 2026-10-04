from django.urls import path
from .views import ApiLoginView, ApiLogoutView, login, logout, dashboard,handleroot, ChangeCredentialsView

urlpatterns = [
    path('',handleroot,name="handleroot"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('login-api/', ApiLoginView.as_view(), name="login-api"),
    path('logout-api/', ApiLogoutView.as_view(), name="logout-api"),
    path('change-credentials/', ChangeCredentialsView.as_view(), name="change-credentials")
]