from importlib import import_module

from django import template
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import dashboard
urlpatterns = [
    path("",auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login") ,
    path("dashboard/",auth_views.LoginView.as_view(template_name="accounts/main.html"),name="dashboard")
]