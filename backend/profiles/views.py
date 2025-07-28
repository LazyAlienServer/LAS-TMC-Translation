from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import (
    ProfileSerializer,
    RegisterSerializer,
    CustomLoginSerializer,
    CustomLoginRefreshSerializer,
    UsernameUpdateSerializer,
)


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UsernameUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UsernameUpdateSerializer


class AvatarUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer


class CustomLoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomLoginSerializer


class CustomLoginRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)
    serializer_class = CustomLoginRefreshSerializer
