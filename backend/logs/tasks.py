from celery import shared_task
from django.utils import timezone

from datetime import timedelta

from .models import FELog


@shared_task
def clear_debug_logs(days=14):
    cutoff = timezone.now() - timedelta(days=days)

    debug_deleted, _ = FELog.objects.filter(
        level__in=['debug'],
        timestamp__lt=cutoff
    ).delete()

    # Return the number of deleted debug logs
    return debug_deleted


def clear_info_logs(days=30):
    cutoff = timezone.now() - timedelta(days=days)

    info_deleted, _ = FELog.objects.filter(
        level__in=['info'],
        timestamp__lt=cutoff
    ).delete()

    # Return the number of deleted info logs
    return info_deleted


def clear_warn_logs(days=90):
    cutoff = timezone.now() - timedelta(days=days)

    warn_deleted, _ = FELog.objects.filter(
        level__in=['warn'],
        timestamp__lt=cutoff
    ).delete()

    # Return the number of deleted warn logs
    return warn_deleted
