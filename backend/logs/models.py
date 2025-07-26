from django.db import models


class FELog(models.Model):
    LEVEL_CHOICES = [
        ('debug', 'DEBUG'),
        ('info', 'INFO'),
        ('warn', 'WARN'),
        ('error', 'ERROR'),
    ]

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    message = models.TextField()
    extra = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Frontend Log'
        verbose_name_plural = 'Frontend Logs'

    def __str__(self):
        return f"[{self.level.upper()}]: {self.page} - {self.message[:50]}"
