# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='longitufe',
            new_name='longitude',
        ),
    ]
