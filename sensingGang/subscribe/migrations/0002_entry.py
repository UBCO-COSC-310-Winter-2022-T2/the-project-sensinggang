# Generated by Django 4.1.7 on 2023-04-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscribe", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
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
            ],
        ),
    ]
