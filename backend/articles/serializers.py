from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.request import Request

from core.utils.drf.validators import RequiredValidator, LengthValidator
from core.utils.drf.permissions import is_moderator
from .models import SourceArticle, PublishedArticle, ArticleSnapshot, ArticleModerationEvent


User = get_user_model()


class SourceArticleAuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the author
    """

    author_username = serializers.CharField(source='author.username')
    title = serializers.CharField(validators=[RequiredValidator(field_name='title'), LengthValidator(field_name='title', max_length=60)])

    class Meta:
        model = SourceArticle
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'author',
            'author_username',
            'last_moderation_at'
        )

    def create(self, validated_data):
        request = self.context.get("request")
        user = getattr(request, "user", None)

        if user is None or user.is_anonymous:
            raise serializers.ValidationError("Invalid user")

        validated_data["author"] = user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.title = validated_data.get('title', instance.title)
        instance.content_md = validated_data.get('content_md', instance.content_md)
        instance.save()

        return instance


class SourceArticleModeratorSerializer(serializers.ModelSerializer):
    """
    Serializer for moderators
    """

    author_username = serializers.CharField(source='author.username')

    class Meta:
        model = SourceArticle
        fields = '__all__'
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'is_deleted',
            'author',
            'author_username',
            'title',
            'content_md',
            'last_moderation_at',
        )

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance


class PublishedArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for published articles. All fields are ready-only.
    """

    class Meta:
        model = PublishedArticle
        fields = '__all__'
        read_only_fields = (
            'id',
            'article',
            'title',
            'content_md',
            'published_at'
        )


class ArticleSnapshotSerializer(serializers.ModelSerializer):
    """
    Serializer for article snapshots. All fields are ready-only.
    """

    class Meta:
        model = ArticleSnapshot
        fields = '__all__'
        read_only_fields = (
            'id',
            'article',
            'title',
            'content_md',
            'content_hash',
            'created_at'
        )


class ArticleModerationEventSerializer(serializers.ModelSerializer):
    """
    Serializer for article moderation events. All fields are ready-only except annotation.
    """
    class Meta:
        model = ArticleModerationEvent
        fields = '__all__'
        read_only_fields = [
            'id',
            'article',
            'snapshot',
            'annotation',
            'type',
            'moderator',
            'created_at'
        ]

    def _get_request(self):
        req = self.context.get("request")
        return req if isinstance(req, Request) else None

    def _get_user(self):
        req = self._get_request()
        return getattr(req, "user", None)

    def get_fields(self):
        fields = super().get_fields()
        user = self._get_user()

        if is_moderator(user):
            fields['annotation'].read_only = False

        return fields

    def create(self, validated_data):
        return ArticleModerationEvent.objects.create(**validated_data)
