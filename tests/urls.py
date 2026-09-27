from importlib import import_module
from operator import index
from django import template
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import handleindex, handlelogin

urlpatterns=[
    path("dash",handleindex,name="handleindexb"),
    path("log",handlelogin,name="handlelogin")
    ]