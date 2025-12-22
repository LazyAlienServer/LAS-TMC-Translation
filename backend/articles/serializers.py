from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.request import Request

from core.utils.drf.validators import RequiredValidator, LengthValidator
from core.utils.drf.permissions import is_moderator
from .models import SourceArticle, PublishedArticle, ArticleSnapshot, ArticleEvent


User = get_user_model()


class SourceArticleReadSerializer(serializers.ModelSerializer):
    """
    Serializer for moderators
    """

    author_username = serializers.CharField(source='author.username')
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = SourceArticle
        fields = '__all__'
        read_only_fields = [
            'id',
            'author',
            'title',
            'content',
            'status',
            'last_moderation_at',
            'created_at',
            'updated_at',
            'is_deleted',
            'author_username',
            'status_display'
        ]

    def get_status_display(self, obj):
        return obj.get_status_display()


class SourceArticleWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the author, can be used to create/update
    """

    title = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[RequiredValidator(field_name='title'), LengthValidator(field_name='title', max_length=60)],
    )

    class Meta:
        model = SourceArticle
        fields = ['title', 'content']

    def create(self, validated_data):
        validated_data.setdefault("title", "Untitled")

        return super().create(validated_data)


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
            'content',
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
            'content',
            'content_hash',
            'created_at'
        )


class ArticleEventSerializer(serializers.ModelSerializer):
    """
    Serializer for article moderation events. All fields are ready-only except annotation.
    """
    class Meta:
        model = ArticleEvent
        fields = '__all__'
        read_only_fields = [
            'id',
            'article',
            'snapshot',
            'annotation',
            'event_type',
            'actor',
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
        return ArticleEvent.objects.create(**validated_data)


class ArticleActionInputSerializer(serializers.Serializer):
    """
    The input serializer for all article actions,
    which include submit, approve, reject, unpublish and delete
    """
    article_id = serializers.UUIDField(required=True)
    annotation = serializers.CharField(required=False, allow_blank=True)


class ArticleActionOutputSerializer(serializers.Serializer):
    event_type = serializers.IntegerField()
    actor_id = serializers.UUIDField()
    article_id = serializers.UUIDField()
    status = serializers.IntegerField()
    snapshot_id = serializers.UUIDField()
    event_id = serializers.UUIDField()

    def to_representation(self, instance):
        """
        Add event_type_display and current_status_display to the response,
        by using .label method
        """
        data = super().to_representation(instance)

        data["event_type_display"] = ArticleEvent.EventType(data["event_type"]).label
        data["status_display"] = SourceArticle.ArticleStatus(data["status"]).label

        return data
