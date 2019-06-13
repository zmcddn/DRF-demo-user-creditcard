from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy

from rest_framework.routers import DefaultRouter

from users.views import LoginViewCustom
from accounts.views import CardSerializerViewSet


router = DefaultRouter()
router.register(r'card', CardSerializerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/auth/", include("rest_auth.urls")),
    path("api/auth/registration/", include("rest_auth.registration.urls")),
    path("api/auth/login/", LoginViewCustom.as_view(), name="rest_login"),
]
