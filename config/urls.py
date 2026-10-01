from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/dashboard/')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view(), name="login"),
    path('api/auth/refresh', TokenRefreshView.as_view(), name="token-refresh"),
    path('api/', include("catalog.urls")),
    path('api/', include("inventory.urls")),
    path("",include("accounts.urls")),
    path("test/",include("tests.urls")),
    path('api/', include("media_manager.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)