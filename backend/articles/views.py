from django.shortcuts import get_object_or_404

from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.utils.drf.pagination import StandardPagination
from core.utils.drf.permissions import is_moderator
from .permissions import (
    SourceArticlePermission,
    PublishedArticlePermission,
    ArticleSnapshotPermission,
    ArticleEventPermission,
)
from .models import SourceArticle, PublishedArticle, ArticleSnapshot, ArticleEvent
from .serializers import (
    SourceArticleAuthorSerializer,
    SourceArticleModeratorSerializer,
    PublishedArticleSerializer,
    ArticleSnapshotSerializer,
    ArticleEventSerializer,
    ArticleActionInputSerializer,
    ArticleActionOutputSerializer,
)
from .services.articles import (
    submit, withdraw, approve, reject, unpublish, delete
)


class SourceArticleCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SourceArticleAuthorSerializer


class SourceArticleView(RetrieveUpdateAPIView):
    permission_classes = (SourceArticlePermission,)

    def get_serializer_class(self):
        if is_moderator(self.request.user):
            return SourceArticleModeratorSerializer
        return SourceArticleAuthorSerializer


class PublishedArticleViewSet(ReadOnlyModelViewSet):
    queryset = PublishedArticle.objects.all()
    serializer_class = PublishedArticleSerializer
    permission_classes = (PublishedArticlePermission,)


class ArticleSnapshotViewSet(ReadOnlyModelViewSet):
    queryset = ArticleSnapshot.objects.all()
    serializer_class = ArticleSnapshotSerializer
    permission_classes = (ArticleSnapshotPermission,)


class ArticleEventReadViewset(ReadOnlyModelViewSet):
    queryset = ArticleEvent.objects.all()
    permission_classes = (ArticleEventPermission,)
    serializer_class = ArticleEventSerializer

    def get_queryset(self):
        user = self.request.user
        if is_moderator(user):
            return ArticleEvent.objects.all()
        return ArticleEvent.objects.filter(article__author=user)


class ArticleActionViewset(GenericViewSet):
    queryset = SourceArticle.objects.all()

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def submit(self, request, pk=None):
        input_serializer = ArticleActionInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        result = submit(
            article_id=pk,
            actor=request.user,
            annotation=input_serializer.validated_data.get("annotation", None)
        )

        output_serializer = ArticleActionOutputSerializer(result)

        return Response(output_serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def withdraw(self, request, pk=None):
        input_serializer = ArticleActionInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        result = withdraw(
            article_id=pk,
            actor=request.user,
            annotation=input_serializer.validated_data.get("annotation", None)
        )

        output_serializer = ArticleActionOutputSerializer(result)

        return Response(output_serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def approve(self, request, pk=None):
        input_serializer = ArticleActionInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        result = approve(
            article_id=pk,
            actor=request.user,
            annotation=input_serializer.validated_data.get("annotation", None)
        )

        output_serializer = ArticleActionOutputSerializer(result)

        return Response(output_serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def reject(self, request, pk=None):
        input_serializer = ArticleActionInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        result = reject(
            article_id=pk,
            actor=request.user,
            annotation=input_serializer.validated_data.get("annotation", None)
        )

        output_serializer = ArticleActionOutputSerializer(result)

        return Response(output_serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unpublish(self, request, pk=None):
        input_serializer = ArticleActionInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        result = unpublish(
            article_id=pk,
            actor=request.user,
            annotation=input_serializer.validated_data.get("annotation", None)
        )

        output_serializer = ArticleActionOutputSerializer(result)

        return Response(output_serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def delete(self, request, pk=None):
        input_serializer = ArticleActionInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        result = delete(
            article_id=pk,
            actor=request.user,
            annotation=input_serializer.validated_data.get("annotation", None)
        )

        output_serializer = ArticleActionOutputSerializer(result)

        return Response(output_serializer.data)
