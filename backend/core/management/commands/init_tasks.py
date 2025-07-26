import json

from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.utils import timezone


class Command(BaseCommand):
    help = 'Initialize all tasks'

    def handle(self, *args, **kwargs):
        # Timer in minutes
        minute_schedule, _ = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES,
        )

        # Timer in days
        day_schedule, _ = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )

        # tasks config
        task_configs = [
            {
                "name": "update youtube cache",
                "task": "pages.tasks.refresh_youtube_cache",
                "schedule": minute_schedule,
                "args": [],
            },
            {
                "name": "clear old frontend debug logs",
                "task": "logs.tasks.clear_debug_logs",
                "schedule": day_schedule,
                "args": [14],
            },
            {
                "name": "clear old frontend info logs",
                "task": "logs.tasks.clear_info_logs",
                "schedule": day_schedule,
                "args": [30],
            },
            {
                "name": "clear old frontend warn logs",
                "task": "logs.tasks.clear_warn_logs",
                "schedule": day_schedule,
                "args": [90],
            },
        ]

        # Delete all tasks that does not exist in task_configs
        existing_tasks = PeriodicTask.objects.all()
        required_tasks = [conf["task"] for conf in task_configs]
        for task in existing_tasks:
            if task.task not in required_tasks:
                self.stdout.write(
                    self.style.WARNING(f"Deleting old task: {task.name} ({task.task})")
                )
                task.delete()

        # Init tasks
        for conf in task_configs:

            # Create all uncreated tasks in task_configs
            task, created = PeriodicTask.objects.get_or_create(
                interval=conf["schedule"],
                name=conf["name"],
                task=conf["task"],
                defaults={
                    'enabled': True,
                    'start_time': timezone.now(),
                    'args': json.dumps(conf["args"]),
                },
            )

            # Update the config of all existing tasks
            if not created:
                task.enabled = True
                task.interval = conf["schedule"]
                task.start_time = timezone.now()
                task.args = json.dumps(conf["args"])
                task.save()

        self.stdout.write(self.style.SUCCESS('Successfully initialized tasks.'))
