# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-25 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20161031_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedsearch',
            name='name',
            field=models.CharField(default='Unsaved Search 2017-01-25 17:03:55.593390+00:00', max_length=100),
        ),
    ]