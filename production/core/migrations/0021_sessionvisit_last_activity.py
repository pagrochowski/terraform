# Generated by Django 5.0.6 on 2024-05-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_sessionvisit"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionvisit",
            name="last_activity",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]