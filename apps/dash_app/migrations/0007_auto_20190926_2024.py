# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-26 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_app', '0006_auto_20190926_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='quotes',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='dash_app.User'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
