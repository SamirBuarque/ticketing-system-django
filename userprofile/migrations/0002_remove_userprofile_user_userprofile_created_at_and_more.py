# Generated by Django 5.0.4 on 2024-04-20 00:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='Unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='Unknown', max_length=128),
            preserve_default=False,
        ),
    ]
