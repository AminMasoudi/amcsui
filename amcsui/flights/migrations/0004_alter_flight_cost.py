# Generated by Django 4.1.7 on 2023-05-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0003_flight_cost_alter_flight_destination_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="cost",
            field=models.IntegerField(),
        ),
    ]
