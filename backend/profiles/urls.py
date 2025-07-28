from django.urls import path

from .views import (
    ProfileView,
    RegisterView,
    CustomLoginView,
    CustomLoginRefreshView,
    UsernameUpdateView,
    AvatarUpdateView,
)

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('refresh_login_token/', CustomLoginRefreshView.as_view(), name='refresh-login'),
    path('update_profile/', UsernameUpdateView.as_view(), name='update_profile'),
    path('update_avatar/', AvatarUpdateView.as_view(), name='avatar'),
]
