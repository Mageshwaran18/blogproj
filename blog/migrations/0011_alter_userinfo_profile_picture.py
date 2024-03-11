# Generated by Django 5.0.3 on 2024-03-11 04:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_userinfo_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_picture/"
            ),
        ),
    ]