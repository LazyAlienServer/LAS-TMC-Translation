from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/pages/", include("pages.urls")),
    path("api/v1/user/", include("profiles.urls")),
    path("api/v1/log/", include("logs.urls")),
    path("api/v1/article/", include("articles.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
