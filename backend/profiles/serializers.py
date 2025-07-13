from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.settings import api_settings
import string
import random

from .models import Profile


User = get_user_model()


def generate_unique_username():
    for _ in range(1000):
        uid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        username = f"user_{uid}"
        if not Profile.objects.filter(username=username).exists():
            return username
    raise Exception("Unable to generate unique username")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'email')
        read_only_fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Profile
        fields = ('username', 'email', 'password')
        read_only_fields = ('username',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=generate_unique_username(),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


#class UpdateProfileSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Profile
#        fields = ('username', 'avatar')

#    def validate_avatar(self, value):
#        valid_mime_formats = ['image/png', 'image/jpeg', 'image/webp']

#        if value.content_type not in valid_mime_formats:
#            raise serializers.ValidationError("Unsupported avatar file type.")

#        if value.size > 2 * 1024 * 1024:
#            raise serializers.ValidationError("Avatar File Size too large (max 2MB).")

#        return value


class CustomLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        access_lifetime = api_settings.ACCESS_TOKEN_LIFETIME
        refresh_lifetime = api_settings.REFRESH_TOKEN_LIFETIME
        data['access_token_lifetime'] = str(access_lifetime.total_seconds())
        data['refresh_token_lifetime'] = str(refresh_lifetime.days)

        return data


class CustomLoginRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        access_lifetime = api_settings.ACCESS_TOKEN_LIFETIME
        data['access_token_lifetime'] = str(access_lifetime.total_seconds())

        return data
