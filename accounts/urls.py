from importlib import import_module

from django import template
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import dashboard , login , LoginView , MeView

urlpatterns = [
    path("web-login/", login, name="web-login"),
    path("dashboard/", dashboard, name="dashboard"),
    
    path("login/", LoginView.as_view(), name="api-login"),
    path("me/", MeView.as_view(), name="api-me"),
]