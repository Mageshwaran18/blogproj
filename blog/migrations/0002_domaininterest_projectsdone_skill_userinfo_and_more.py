# Generated by Django 5.0.3 on 2024-03-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DomainInterest",
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
                ("domain_name", models.CharField(default=" ", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ProjectsDone",
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
                ("project_name", models.CharField(default=" ", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
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
                ("skill_name", models.CharField(default=" ", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
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
                ("email", models.EmailField(max_length=254)),
                ("domain", models.CharField(default=" ", max_length=100)),
                ("city", models.CharField(default=" ", max_length=100)),
                ("phone_number", models.CharField(default=" ", max_length=15)),
                (
                    "domain_interest",
                    models.ManyToManyField(blank=True, to="blog.domaininterest"),
                ),
                (
                    "projects_done",
                    models.ManyToManyField(blank=True, to="blog.projectsdone"),
                ),
                ("skills", models.ManyToManyField(blank=True, to="blog.skill")),
            ],
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]
