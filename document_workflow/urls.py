# config/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # JWT Auth
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # App URLs
    path("api/users/", include("accounts.urls")),
    path("api/documents/", include("documents.urls")),
    path("api/workflows/", include("workflows.urls")),
    path("api/audit/", include("audit.urls")),
]
