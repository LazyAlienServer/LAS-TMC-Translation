from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from backend.settings.base import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("pages.urls")),
]
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
