# Generated by Django 4.2 on 2023-04-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magcalendar', '0003_alter_calendar_exercises_id_exercises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar_exercises',
            name='created_at',
            field=models.DateField(),
        ),
    ]
