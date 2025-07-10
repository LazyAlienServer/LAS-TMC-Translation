from django.urls import path

from .views import (
    ProfileView,
    RegisterView,
    CustomLoginView,
    CustomLoginRefreshView,
)

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('refresh_login_token/', CustomLoginRefreshView.as_view(), name='refresh-login'),
]
