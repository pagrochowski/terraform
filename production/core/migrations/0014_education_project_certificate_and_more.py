# Generated by Django 5.0.6 on 2024-05-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_education_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="education_project",
            name="certificate",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="education_project",
            name="link",
            field=models.TextField(blank=True, null=True),
        ),
    ]