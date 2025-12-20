from django.db import transaction
from django.contrib.auth import get_user_model
from django.utils import timezone

from articles.models import (
    SourceArticle, PublishedArticle, ArticleSnapshot, ArticleEvent
)
from .exceptions import (
    StateTransitionError,
    CoolingDownError,
    NoChangeError,
    NoSnapshotError,
)
from .utils import (
    hash_and_normalize, get_last_snapshot, get_published_version, within_submit_cooldown
)


User = get_user_model()


def select_article_for_update(article_id):
    article = (
        SourceArticle.objects
        .select_for_update()
        .select_related('author')
        .get(pk=article_id)
    )

    return article


def create_article_event(article, snapshot, annotation, event_type, actor):

    article_event = ArticleEvent.objects.create(
        article=article,
        snapshot=snapshot,
        annotation=annotation,
        event_type=event_type,
        actor=actor,
    )

    return article_event


def build_article_action_result(*, article, actor, event, snapshot):

    return {
        "event_type": event.event_type,
        "actor_id": actor.id,
        "article_id": article.id,
        "current_article_status": article.status,
        "snapshot_id": snapshot.id,
        "event_id": event.id,
    }


@transaction.atomic
def submit(*, article_id, actor, annotation=None):
    article = select_article_for_update(article_id)

    # If submitted within 12 hours since last submission, raise CoolingDownError
    last_moderation_at = article.last_moderation_at
    if last_moderation_at and within_submit_cooldown(last_moderation_at, hours=6):
        raise CoolingDownError("Submission has a cooldown of 6 hours.")

    current_hash = hash_and_normalize(
        article.title,
        article.content_md
    )

    # If unchanged, raise NoChangeError
    last_snapshot = get_last_snapshot(article)
    if last_snapshot and last_snapshot.content_hash == current_hash:
        raise NoChangeError("Please modify before submission.")

    # Business Logic

    # Create Snapshot
    snapshot = ArticleSnapshot.objects.create(
        article=article,
        title=article.title,
        content_md=article.content_md,
        content_hash=current_hash,
    )

    # Create Article Event
    article_event = create_article_event(
        article, snapshot, annotation, event_type=ArticleEvent.EventType.SUBMIT, actor=actor
    )

    # Update Source Article
    article.status = SourceArticle.ArticleStatus.PENDING
    article.save(update_fields=['status'])

    return build_article_action_result(article=article, actor=actor, event=article_event, snapshot=snapshot)


@transaction.atomic
def withdraw(*, article_id, actor, annotation=None):
    article = select_article_for_update(article_id)

    # Delete Last Snapshot
    snapshot = get_last_snapshot(article)

    # Create Article Event
    article_event = create_article_event(
        article, snapshot, annotation, event_type=ArticleEvent.EventType.WITHDRAW, actor=actor
    )

    # Update Source Article
    article.status = SourceArticle.ArticleStatus.DRAFT
    article.save(update_fields=['status'])

    return build_article_action_result(article=article, actor=actor, event=article_event, snapshot=snapshot)


@transaction.atomic
def approve(*, article_id, actor, annotation=None):
    article = select_article_for_update(article_id)

    # Can only approve when the Source Article is PENDING
    if article.status != SourceArticle.ArticleStatus.PENDING:
        raise StateTransitionError("Only a pending article can be approved!")

    snapshot = get_last_snapshot(article)
    if not snapshot:
        raise NoSnapshotError("There are no snapshots for this article!")

    # Create Published Article
    published_article = PublishedArticle.objects.create(
        article=article,
        title=snapshot.title,
        content_md=snapshot.content_md,
    )

    # Create Article Event
    article_event = create_article_event(
        article, snapshot, annotation, event_type=ArticleEvent.EventType.APPROVE, actor=actor
    )

    # Update Source Article
    article.status = SourceArticle.ArticleStatus.PUBLISHED
    article.last_moderation_at = timezone.now()
    article.save(update_fields=['status', 'last_moderation_at'])

    return build_article_action_result(article=article, actor=actor, event=article_event, snapshot=snapshot)


@transaction.atomic
def reject(*, article_id, actor, annotation=None):
    article = select_article_for_update(article_id)

    # Can only reject when the Source Article is PENDING
    if article.status != SourceArticle.ArticleStatus.PENDING:
        raise StateTransitionError("Only a pending article can be rejected!")

    snapshot = get_last_snapshot(article)
    if not snapshot:
        raise NoSnapshotError("There are no snapshots for this article!")

    # Create Article Event
    article_event = create_article_event(
        article, snapshot, annotation, event_type=ArticleEvent.EventType.REJECT, actor=actor
    )

    # Update Source Article
    article.status = SourceArticle.ArticleStatus.REJECTED
    article.last_moderation_at = timezone.now()
    article.save(update_fields=['status', 'last_moderation_at'])

    return build_article_action_result(article=article, actor=actor, event=article_event, snapshot=snapshot)


@transaction.atomic
def unpublish(*, article_id, actor, annotation=None):
    article = select_article_for_update(article_id)

    # Can only unpublish when the Source Article is PUBLISHED
    if article.status != SourceArticle.ArticleStatus.PUBLISHED:
        raise StateTransitionError("Only a published article can be unpublished!")

    snapshot = get_last_snapshot(article)
    if not snapshot:
        raise NoSnapshotError("There are no snapshots for this article!")

    # Create Article Event
    article_event = create_article_event(
        article, snapshot, annotation, event_type=ArticleEvent.EventType.UNPUBLISH, actor=actor
    )

    # Update Source Article
    article.status = SourceArticle.ArticleStatus.UNPUBLISHED
    article.last_moderation_at = timezone.now()
    article.save(update_fields=['status', 'last_moderation_at'])

    return build_article_action_result(article=article, actor=actor, event=article_event, snapshot=snapshot)


@transaction.atomic
def delete(*, article_id, actor, annotation=None):
    article = select_article_for_update(article_id)

    # Can only delete when the Source Article is not PENDING
    if article.status == SourceArticle.ArticleStatus.PENDING:
        raise StateTransitionError("A pending article cannot be deleted! Please withdraw it from moderation first.")

    snapshot = get_last_snapshot(article)
    if not snapshot:
        raise NoSnapshotError("There are no snapshots for this article!")
    published_article = get_published_version(article)

    # Soft Delete Source Article
    article.delete()

    # Delete Associated Published Article
    if published_article:
        published_article.delete()

    # Create Article Event
    article_event = create_article_event(
        article, snapshot, annotation, event_type=ArticleEvent.EventType.DELETE, actor=actor
    )

    # Update Source Article
    article.status = SourceArticle.ArticleStatus.DELETED
    article.save(update_fields=['status'])

    return build_article_action_result(article=article, actor=actor, event=article_event, snapshot=snapshot)
