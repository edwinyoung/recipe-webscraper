# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0004_auto_20170428_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='source_url',
            field=models.TextField(unique=True),
        ),
    ]
