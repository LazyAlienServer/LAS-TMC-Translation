from django.urls import path

from rest_framework import routers

from .views import (
    SourceArticleViewSet,
    PublishedArticleViewSet,
    ArticleSnapshotViewSet,
    ArticleEventReadViewset,
    ArticleActionViewset,
)


router = routers.SimpleRouter()

router.register(r'source_articles', SourceArticleViewSet, basename='source_articles')
router.register(r'published_articles', PublishedArticleViewSet, basename='published_articles')
router.register(r'article_snapshots', ArticleSnapshotViewSet, basename='article_snapshots')
router.register(r'article_events', ArticleEventReadViewset, basename='article_events')
router.register(r'article_actions', ArticleActionViewset, basename='article_actions')

urlpatterns = []

urlpatterns += router.urls
