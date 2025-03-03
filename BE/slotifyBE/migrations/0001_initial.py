# Generated by Django 5.1.4 on 2025-01-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OwnerProfile",
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
                ("firstName", models.CharField(max_length=50)),
                ("lastName", models.CharField(max_length=50)),
                ("emailId", models.EmailField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("contactNumber", models.CharField(max_length=10, unique=True)),
                ("idProof", models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
