# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate , update_session_auth_hash
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class ChangeCredentialsView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        new_username = request.data.gat("username", "").strip()
        new_password = request.data.get("password", "").strip()

        if not new_username and not new_password:
            return Response(
                {"detail": "Please provide a new username or a new password."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if new_username:
            user.username = new_username
        if new_password:
            user.set_password(new_password)
            update_session_auth_hash(request, user)
        user.save()
        return Response({
            "detail": "Credentials update successfully.",
            "username": user.username
        }, status=status.HTTP_200_OK)

class ApiLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username= request.data.get("username","").strip()
        password= request.data.get("password","").strip()

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                {"detail": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        django_login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "username": user.username,
        }, status=status.HTTP_200_OK)

class ApiLogoutView(APIView):
    permission_classes= [AllowAny]

    def post(self,request):
        django_logout(request)
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)

def login(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    return render(request, "login.html")
def logout(request):
    django_logout(request)
    return redirect("/login/")


def handleroot(request):
    if not (request.user.is_authenticated):
        return redirect("/login/")
    return redirect("/dashboard/")

    
@login_required(login_url="/login/")
def dashboard(request):
    return render(request, "index.html")
