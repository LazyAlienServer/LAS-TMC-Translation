from django.contrib import admin, messages

from .models import SourceArticle, PublishedArticle, ArticleSnapshot, ArticleModerationEvent


@admin.register(SourceArticle)
class ArticleAdmin(admin.ModelAdmin):
    model = SourceArticle
    list_display = (
        "title",
        "author",
        "status_display",
        "created_at",
        "updated_at",
        "is_deleted",
    )
    list_filter = (
        "status",
        "is_deleted",
        ("author", admin.RelatedOnlyFieldListFilter),
        "created_at",
    )

    search_fields = ("title", "author__username")
    ordering = ("-created_at",)
    list_per_page = 25
    date_hierarchy = "created_at"

    readonly_fields = ("created_at", "updated_at", "last_moderation_at")

    fieldsets = (
        ("Basic", {"fields": ("title", "content_md")}),
        ("Ownership & Status", {"fields": ("author", "status", "is_deleted")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    actions = ["action_soft_delete", "action_restore", "action_hard_delete"]

    def status_display(self, obj):
        return obj.get_status_display()
    status_display.short_description = "Status"

    def action_soft_delete(self, request, queryset):
        updated = queryset.update(is_deleted=True)
        self.message_user(request, f"Soft-deleted {updated} article(s).", level=messages.WARNING)
    action_soft_delete.short_description = "Soft delete selected"

    def action_restore(self, request, queryset):
        updated = queryset.update(is_deleted=False)
        self.message_user(request, f"Restored {updated} article(s).", level=messages.SUCCESS)
    action_restore.short_description = "Restore selected (undo soft delete)"

    def action_hard_delete(self, request, queryset):
        count = 0
        for obj in queryset:
            obj.hard_delete()
            count += 1
        self.message_user(request, f"Hard-deleted {count} article(s).", level=messages.ERROR)
    action_hard_delete.short_description = "Hard delete selected (cannot be undone)"


@admin.register(PublishedArticle)
class ArticleAdmin(admin.ModelAdmin):
    model = PublishedArticle
    list_display = (
        "title",
        "published_at",
    )
    list_filter = (
        "published_at",
    )

    search_fields = ("title",)
    ordering = ("-published_at",)
    list_per_page = 25
    date_hierarchy = "published_at"

    readonly_fields = ("published_at", "article", "title", "content_md")

    fieldsets = (
        ("Basic", {"fields": ("title", "content_md")}),
        ("Key Info", {"fields": ("article",)}),
        ("Timestamps", {"fields": ("published_at",)}),
    )


@admin.register(ArticleSnapshot)
class ArticleSnapshotAdmin(admin.ModelAdmin):
    model = ArticleSnapshot
    list_display = (
        "title",
        "created_at",
    )
    list_filter = (
        "created_at",
    )

    search_fields = ("title", "creator__username")
    ordering = ("-created_at",)
    list_per_page = 25
    date_hierarchy = "created_at"

    readonly_fields = ("created_at", "article", "title", "content_md", "content_hash")

    fieldsets = (
        ("Basic", {"fields": ("title", "content_md", "content_hash")}),
        ("Key Info", {"fields": ("article",)}),
        ("Timestamps", {"fields": ("created_at",)}),
    )


@admin.register(ArticleModerationEvent)
class ArticleModerationEventAdmin(admin.ModelAdmin):
    model = ArticleModerationEvent
    list_display = (
        "moderator",
        "type",
        "created_at",
    )

    list_filter = (
        "moderator",
        "type",
        "created_at",
    )

    search_fields = ("type", "moderator__username")
    ordering = ("-created_at",)
    list_per_page = 25
    date_hierarchy = "created_at"

    readonly_fields = ("article", "snapshot", "type", "moderator", "created_at")

    fieldsets = (
        ("Key Info", {"fields": ("type", "moderator", "article", "snapshot", "annotation")}),
        ("Timestamps", {"fields": ("created_at",)}),
    )

    def type_display(self, obj):
        return obj.get_type_display()
    type_display.short_description = "Type"
