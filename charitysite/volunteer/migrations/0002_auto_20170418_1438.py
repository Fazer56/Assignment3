# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
