from django.shortcuts import get_object_or_404

from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.utils.drf.pagination import StandardPagination
from .permissions import (
    SourceArticlePermission,
    PublishedArticlePermission,
    ArticleSnapshotPermission,
    ArticleModerationEventReadPermission,
    ArticleModerationEventWritePermission
)
from .models import PublishedArticle, ArticleSnapshot, ArticleModerationEvent
from .serializers import (
    SourceArticleAuthorSerializer,
    SourceArticleModeratorSerializer,
    PublishedArticleSerializer,
    ArticleSnapshotSerializer,
    ArticleModerationEventSerializer
)


class SourceArticleCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SourceArticleAuthorSerializer


class SourceArticleModeratorView(RetrieveUpdateAPIView):
    permission_classes = (SourceArticlePermission,)
    serializer_class = SourceArticleModeratorSerializer


class SourceArticleAuthorView(RetrieveUpdateAPIView):
    permission_classes = (SourceArticlePermission,)
    serializer_class = SourceArticleAuthorSerializer


class PublishedArticleViewSet(ReadOnlyModelViewSet):
    queryset = PublishedArticle.objects.all()
    serializer_class = PublishedArticleSerializer
    permission_classes = (PublishedArticlePermission,)


class ArticleSnapshotViewSet(ReadOnlyModelViewSet):
    queryset = ArticleSnapshot.objects.all()
    serializer_class = ArticleSnapshotSerializer
    permission_classes = (ArticleSnapshotPermission,)


class ArticleModerationEventCreateView(CreateAPIView):
    permission_classes = (ArticleModerationEventWritePermission,)
    serializer_class = ArticleModerationEventSerializer


class ArticleModerationEventReadViewset(ReadOnlyModelViewSet):
    queryset = ArticleModerationEvent.objects.all()
    permission_classes = (ArticleModerationEventReadPermission,)
    serializer_class = ArticleModerationEventSerializer
