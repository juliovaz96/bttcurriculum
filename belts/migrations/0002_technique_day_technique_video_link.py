# Generated by Django 5.1.5 on 2025-01-15 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='technique',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='technique',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
