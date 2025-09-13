from django.urls import path

from rest_framework import routers

from .views import (
    SourceArticleCreateView,
    SourceArticleAuthorView,
    SourceArticleModeratorView,
    PublishedArticleViewSet,
    ArticleSnapshotViewSet,
    ArticleModerationEventCreateView,
    ArticleModerationEventReadViewset
)


router = routers.SimpleRouter()
router.register(r'published_articles', PublishedArticleViewSet)
router.register(r'article_snapshots', ArticleSnapshotViewSet)
router.register(r'article_moderation_events', ArticleModerationEventReadViewset)

urlpatterns = [
    path('source_articles/create/', SourceArticleCreateView.as_view()),
    path('source_articles/author_view/', SourceArticleAuthorView.as_view()),
    path('source_articles/moderator_view/', SourceArticleModeratorView.as_view()),
    path('article_moderation_events/create/', ArticleModerationEventCreateView.as_view()),
]

urlpatterns += router.urls
