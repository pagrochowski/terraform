# Generated by Django 5.0.6 on 2024-05-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_macro_project_options_macro_project_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="macro_project",
            name="screenshot",
            field=models.FileField(
                blank=True, null=True, upload_to="project_screenshots/"
            ),
        ),
    ]