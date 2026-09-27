# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

LoginView = TokenObtainPairView

class MeView(APIView):
     permission_classes = [IsAuthenticated]

     def get(self,request):
        role_data = [request.user.role] if hasattr(request.user,'role') else []
        return Response({
             "username": request.user.username,
             "role": role_data,
        })

def login(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    return auth_views.LoginView.as_view(
        template_name="accounts/login.html"
    )(request)
@login_required
def dashboard(request):
        return (render(request,"accounts/main.html"))
