# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directionsfulltextindex',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='directionsindex',
            old_name='recipe_id',
            new_name='recipe',
        ),
    ]
