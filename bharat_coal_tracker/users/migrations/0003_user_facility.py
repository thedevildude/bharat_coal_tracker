# Generated by Django 4.2.5 on 2023-09-24 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0001_initial"),
        ("users", "0002_role_user_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="facility",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="facility.facility"
            ),
        ),
    ]
