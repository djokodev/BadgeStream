# Generated by Django 5.0.6 on 2024-05-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_alter_animatedvideo_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='animatedvideo',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
