# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-12-06 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20221206_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelconfiguration',
            name='startingDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
