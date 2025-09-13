from django.db import transaction
from django.shortcuts import get_object_or_404

from articles.models import (
    SourceArticle, PublishedArticle, ArticleSnapshot, ArticleModerationEvent
)
from .exceptions import (
    StateTransitionError,
    CoolingDownError,
    NoChangeError,
)
from .utils import (
    hash_and_normalize, get_last_snapshot, within_submit_cooldown
)


@transaction.atomic
def submit(*, article_id, actor_id):
    article = SourceArticle.objects.select_for_update().select_related('author').get(pk=article_id)

    if within_submit_cooldown(article.last_moderation_at, hours=24):
        raise CoolingDownError("Submission has a cooldown of 24 hours.")

    current_hash = hash_and_normalize(article.title, article.summary, article.content_md)

    last_snapshot = get_last_snapshot(article)
    if last_snapshot and last_snapshot.hash == current_hash:
        raise NoChangeError("Please modify before submission.")
