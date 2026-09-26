# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
def login(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    return auth_views.LoginView.as_view(
        template_name="accounts/login.html"
    )(request)
@login_required
def dashboard(request):
        return (render(request,"accounts/main.html"))
