# Generated by Django 5.0.3 on 2024-03-11 04:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_userinfo_about_alter_userinfo_department_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
        ),
    ]
