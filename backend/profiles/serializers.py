from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from .models import Profile

import string
import random


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
