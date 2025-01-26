# user_manager/urls.py
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import (LoginView_, LogoutView_, OrganizationViewSet,
                    RegisterView_, TeamViewSet, UserViewSet)

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path("register/", RegisterView_.as_view(), name="register"),
    path("login/", LoginView_.as_view(), name="login"),
    path("logout/", LogoutView_.as_view(), name="logout"),
    path('', include(router.urls)),
]
