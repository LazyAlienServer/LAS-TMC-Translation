from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/pages/", include("pages.urls")),
    path("api/v1/user/", include("profiles.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
