# Generated by Django 4.2 on 2023-04-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magcalendar', '0004_alter_calendar_exercises_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercises',
            name='title_polish',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]