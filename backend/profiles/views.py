from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .serializers import ProfileSerializer, RegisterSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
