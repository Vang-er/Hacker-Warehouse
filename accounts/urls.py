from django import template
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("",auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login")
]