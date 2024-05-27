# Generated by Django 5.0.6 on 2024-05-26 20:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0021_sessionvisit_last_activity"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionvisit",
            name="visit_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
