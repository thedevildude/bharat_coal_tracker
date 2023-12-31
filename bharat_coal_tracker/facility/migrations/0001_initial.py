# Generated by Django 4.2.5 on 2023-09-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Facility",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, verbose_name="Name of Facility")),
                ("address", models.CharField(max_length=200)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("MINE", "Mine"),
                            ("WASHERY", "Washery"),
                            ("RAILWAY", "Railway"),
                            ("PORT", "Port"),
                            ("POWER_PLANT", "Power Plant"),
                            ("OTHER", "Other"),
                        ],
                        default="OTHER",
                        max_length=100,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name_plural": "Facilities",
                "ordering": ["name"],
            },
        ),
    ]
