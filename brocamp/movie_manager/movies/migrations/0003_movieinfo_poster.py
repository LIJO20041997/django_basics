# Generated by Django 5.2 on 2025-04-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_director"),
    ]

    operations = [
        migrations.AddField(
            model_name="movieinfo",
            name="poster",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]
