# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-16 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adds', '0008_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adds',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
