from django.urls import path

from .views import (
    FELogCreateView
)


urlpatterns = [
    path('collect/', FELogCreateView.as_view(), name='frontend_logs_bulkcreate'),
]
