# Generated by Django 5.0.6 on 2024-05-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthUserManager', '0003_alter_customeuser_email'),
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='badges',
            field=models.ManyToManyField(blank=True, to='badges.badge'),
        ),
    ]