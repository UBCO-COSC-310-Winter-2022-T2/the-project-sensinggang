# Generated by Django 4.1.7 on 2023-04-12 23:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("subscribe", "0002_entry"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("category", models.CharField(max_length=100)),
                ("num_of_products", models.IntegerField()),
            ],
        ),
    ]