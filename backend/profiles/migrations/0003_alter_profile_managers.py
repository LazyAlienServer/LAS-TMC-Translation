# Generated by Django 5.2.1 on 2025-07-25 01:42

import profiles.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_google_id_alter_profile_email_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
                ('objects', profiles.models.ProfileManager()),
            ],
        ),
    ]
