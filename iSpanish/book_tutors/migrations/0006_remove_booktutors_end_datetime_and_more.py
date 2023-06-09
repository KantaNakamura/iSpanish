# Generated by Django 4.1 on 2023-05-23 13:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book_tutors', '0005_rename_date_booktutors_end_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booktutors',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='booktutors',
            name='start_datetime',
        ),
        migrations.AddField(
            model_name='booktutors',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booktutors',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booktutors',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booktutors',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
