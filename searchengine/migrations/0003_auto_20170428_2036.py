# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0002_auto_20170426_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
