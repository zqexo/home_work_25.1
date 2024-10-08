# Generated by Django 5.1.1 on 2024-09-18 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите курс",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.course",
                verbose_name="Курс",
            ),
        ),
    ]
