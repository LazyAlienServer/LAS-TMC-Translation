from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response

from .serializers import (
    ProfileSerializer,
    RegisterSerializer,
    CustomLoginSerializer,
    CustomLoginRefreshSerializer,
    UsernameUpdateSerializer,
    AvatarUpdateSerializer,
)

from .models import Profile


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """获取当前用户信息"""
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class BaseUserUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Don't really need this
        return Profile.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        return self.request.user


class UsernameUpdateView(BaseUserUpdateView):
    serializer_class = UsernameUpdateSerializer


class AvatarUpdateView(BaseUserUpdateView):
    serializer_class = AvatarUpdateSerializer


class CustomLoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomLoginSerializer


class CustomLoginRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)
    serializer_class = CustomLoginRefreshSerializer
