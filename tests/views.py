from django.shortcuts import render

# Create your views here.
def handleindex(request):
    return render(request,"index.html")
def handlelogin(request):
    return render(request,"login.html")
