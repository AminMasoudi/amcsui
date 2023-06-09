# Generated by Django 4.1.7 on 2023-04-12 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("flights", "0002_delete_userprofile"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="userProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                (
                    "trips",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="flights.flight"
                    ),
                ),
            ],
        ),
    ]
