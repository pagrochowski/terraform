# Generated by Django 5.0.6 on 2024-05-25 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_macro_project_screenshot"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Macro_Project",
            new_name="Macroscript_Project",
        ),
    ]