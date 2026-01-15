# apps/accounts/urls.py
from django.urls import path
from .views import UserCreateAPIView, UserListAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user-list"),
    path("create/", UserCreateAPIView.as_view(), name="user-create"),
]
