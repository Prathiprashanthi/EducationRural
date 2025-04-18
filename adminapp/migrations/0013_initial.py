# Generated by Django 5.0.2 on 2024-06-22 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("adminapp", "0012_delete_addcourse_delete_instructorregmodel_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Addcourse",
            fields=[
                ("course_id", models.AutoField(primary_key=True, serialize=False)),
                ("course_name", models.CharField(max_length=255)),
                ("course_image", models.ImageField(upload_to="course_images/")),
                ("course_category", models.CharField(max_length=100)),
                ("course_language", models.CharField(max_length=100)),
                ("video_url", models.URLField()),
                ("duration_weeks", models.IntegerField()),
                ("added_date", models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                "db_table": "Courses_details",
            },
        ),
        migrations.CreateModel(
            name="InstructorRegModel",
            fields=[
                ("instructor_id", models.AutoField(primary_key=True, serialize=False)),
                ("full_name", models.CharField(max_length=55)),
                ("email", models.EmailField(help_text="Enter Email", max_length=100)),
                ("phone_number", models.BigIntegerField(null=True)),
                ("gender", models.CharField(default=False, max_length=50)),
                (
                    "password",
                    models.CharField(help_text="Enter Password", max_length=100),
                ),
                ("photo", models.ImageField(default=False, upload_to="")),
                (
                    "status",
                    models.CharField(default="Pending", max_length=100, null=True),
                ),
                ("reg_date", models.DateField(auto_now_add=True, null=True)),
                ("address", models.CharField(max_length=255)),
                ("otp", models.CharField(default=0, max_length=6)),
                ("otp_status", models.CharField(default="Not Verified", max_length=15)),
            ],
            options={
                "db_table": "Instructor_Details",
            },
        ),
        migrations.CreateModel(
            name="LoanApplication",
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
                ("title", models.CharField(max_length=100)),
                ("eligibility", models.CharField(max_length=10)),
                ("deadline", models.DateField()),
                ("link", models.URLField()),
                ("description", models.TextField()),
            ],
            options={
                "db_table": "loan",
            },
        ),
        migrations.CreateModel(
            name="ScholarshipApplication",
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
                ("title", models.CharField(max_length=100)),
                ("eligibility", models.CharField(max_length=10)),
                ("deadline", models.DateField()),
                ("link", models.URLField()),
                ("description", models.TextField()),
            ],
            options={
                "db_table": "scholarshi",
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                (
                    "subject",
                    models.CharField(
                        choices=[
                            ("Mathematics", "Mathematics"),
                            ("Science", "Science"),
                            ("English", "English"),
                            ("History", "History"),
                            ("Geography", "Geography"),
                            ("Physical Education", "Physical Education"),
                            ("Art", "Art"),
                            ("Music", "Music"),
                            ("Computer Science", "Computer Science"),
                            ("Biology", "Biology"),
                            ("Chemistry", "Chemistry"),
                            ("Physics", "Physics"),
                            ("Economics", "Economics"),
                            ("Sociology", "Sociology"),
                            ("Psychology", "Psychology"),
                            ("Foreign Languages", "Foreign Languages"),
                        ],
                        max_length=50,
                    ),
                ),
                ("question_text", models.TextField()),
                ("class_name", models.CharField(max_length=255)),
                ("option_a", models.CharField(max_length=255)),
                ("option_b", models.CharField(max_length=255)),
                ("option_c", models.CharField(max_length=255)),
                ("option_d", models.CharField(max_length=255)),
                ("correct_answer", models.CharField(max_length=255)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminapp.addcourse",
                    ),
                ),
            ],
            options={
                "db_table": "questions",
            },
        ),
    ]
