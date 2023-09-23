# Generated by Django 4.2.4 on 2023-09-23 05:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("farm_one", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="farmone",
            old_name="turbidity",
            new_name="humidity",
        ),
        migrations.RemoveField(
            model_name="farmone",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="farmonesubject",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="subject",
            name="is_active",
        ),
    ]
