from django.urls import path

from rest_framework import routers

from .views import (
    SourceArticleCreateView,
    SourceArticleView,
    PublishedArticleViewSet,
    ArticleSnapshotViewSet,
    ArticleEventReadViewset,
    ArticleActionViewset,
)


router = routers.SimpleRouter()
router.register(r'published_articles', PublishedArticleViewSet)
router.register(r'article_snapshots', ArticleSnapshotViewSet)
router.register(r'article_events', ArticleEventReadViewset)
router.register(r'article_actions', ArticleActionViewset)

urlpatterns = [
    path('source_articles/', SourceArticleView.as_view()),
    path('source_articles/create/', SourceArticleCreateView.as_view()),
]

urlpatterns += router.urls
