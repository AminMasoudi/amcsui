# Generated by Django 4.1.7 on 2023-05-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0004_alter_flight_cost"),
    ]

    operations = [
        migrations.AddField(
            model_name="flight",
            name="capacity",
            field=models.IntegerField(default=20),
        ),
    ]
