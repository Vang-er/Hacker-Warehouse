from importlib import import_module

from django import template
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import dashboard , login

urlpatterns = [
    path("",login,name="login") ,
    path("dashboard/",dashboard,name="dashboard")
]