# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganji', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
