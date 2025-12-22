from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

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
    SourceArticleReadSerializer,
    SourceArticleWriteSerializer,
    PublishedArticleSerializer,
    ArticleSnapshotSerializer,
    ArticleEventSerializer,
    ArticleActionInputSerializer,
    ArticleActionOutputSerializer,
)
from .services.articles import (
    submit, withdraw, approve, reject, unpublish, delete
)


class SourceArticleViewSet(ModelViewSet):
    permission_classes = (SourceArticlePermission,)

    # Only moderators can see all source articles.
    def get_queryset(self):
        queryset = SourceArticle.objects.select_related("author")

        if is_moderator(self.request.user):
            return queryset
        return queryset.filter(author=self.request.user)

    def get_serializer_class(self):
        # Author - Write Serializer | Moderators - Read Serializer
        if self.action in ('create', 'update', 'partial_update'):
            return SourceArticleWriteSerializer
        return SourceArticleReadSerializer

    def create(self, request, *args, **kwargs):
        input_serializer = SourceArticleWriteSerializer(
            data=request.data,
            context=self.get_serializer_context(),
        )
        input_serializer.is_valid(raise_exception=True)

        instance = input_serializer.save(author=self.request.user)

        output_serializer = SourceArticleReadSerializer(
            instance=instance,
            context=self.get_serializer_context(),
        )
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def mine(self, request):
        """
        Only return the current user's articles
        """
        queryset = SourceArticle.objects.select_related("author").filter(author=self.request.user)

        # page = self.paginate_queryset(queryset)
        #
        # # return data depends on whether a pagination is required in the request
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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

    @action(detail=True, methods=['post'], permission_classes=[SourceArticlePermission,])
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

    @action(detail=True, methods=['post'], permission_classes=[SourceArticlePermission,])
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

    @action(detail=True, methods=['post'], permission_classes=[SourceArticlePermission,])
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

    @action(detail=True, methods=['post'], permission_classes=[SourceArticlePermission,])
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

    @action(detail=True, methods=['post'], permission_classes=[SourceArticlePermission,])
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

    @action(detail=True, methods=['post'], permission_classes=[SourceArticlePermission,])
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
