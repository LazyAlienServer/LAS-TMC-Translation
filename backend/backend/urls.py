from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/pages/", include("pages.urls")),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/auth/", include("profiles.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
