from rest_framework import permissions

from core.utils.drf.permissions import is_moderator, is_the_author


class SourceArticlePermission(permissions.BasePermission):
    """
    Only the author and moderators can view an article.
    Only the author can change title, summary and content_md field of the article
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return is_the_author(request.user, obj) or is_moderator(request.user)


class PublishedArticlePermission(permissions.BasePermission):
    """
    Everyone can view a published article.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class ArticleSnapshotPermission(permissions.BasePermission):
    """
    Only moderators can view snapshots.
    """

    def has_permission(self, request, view):
        return is_moderator(request.user)

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class ArticleModerationEventReadPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS and (is_moderator(request.user) or is_the_author(request.user, obj.article))


class ArticleModerationEventWritePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return is_moderator(request.user)
