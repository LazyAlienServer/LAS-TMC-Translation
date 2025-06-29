import json

from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.utils import timezone


class Command(BaseCommand):
    help = 'Initialize all tasks'

    def handle(self, *args, **kwargs):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES,
        )

        tasks = [
            "pages.tasks.refresh_youtube_cache",
        ]

        existing_tasks = PeriodicTask.objects.all()
        for task in existing_tasks:
            if task.task not in tasks:
                self.stdout.write(self.style.WARNING(f"Deleting old task: {task.name} ({task.task})"))
                task.delete()

        refresh_task, created = PeriodicTask.objects.get_or_create(
            interval=schedule,
            name="update youtube cache",
            task=tasks[0],
            defaults={
                'enabled': True,
                'start_time': timezone.now(),
                'args': json.dumps([])
            },
        )

        if not created:
            refresh_task.enabled = True
            refresh_task.interval = schedule
            refresh_task.start_time = timezone.now()
            refresh_task.save()

        self.stdout.write(self.style.SUCCESS('Successfully initialized tasks.'))
