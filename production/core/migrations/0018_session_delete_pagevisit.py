# Generated by Django 5.0.6 on 2024-05-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_pagevisit_duration_pagevisit_end_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.DateTimeField(auto_now_add=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                ("duration", models.DurationField(blank=True, null=True)),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                ("user_agent", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="PageVisit",
        ),
    ]