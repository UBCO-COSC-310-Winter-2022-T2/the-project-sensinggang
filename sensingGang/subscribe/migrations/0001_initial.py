# Generated by Django 4.1.7 on 2023-04-11 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensors",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="DataEntries",
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
                ("topic", models.CharField(max_length=255)),
                ("data", models.TextField()),
                ("pub_date", models.DateField()),
                (
                    "sensor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="subscribe.sensors",
                    ),
                ),
            ],
        ),
    ]
