# Generated by Django 4.2 on 2023-04-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magcalendar', '0005_exercises_title_polish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='title_polish',
            field=models.CharField(default='', max_length=255),
        ),
    ]
