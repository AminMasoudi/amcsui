# Generated by Django 4.1.7 on 2023-05-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_userprofile_trips_userprofile_trips"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="credit",
            field=models.IntegerField(default=1000),
        ),
    ]
