# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-15 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adds', '0005_auto_20161115_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adds',
            name='item',
            field=models.CharField(choices=[('Broilers', 'Broilers'), ('Layers', 'Layers'), ('Eggs', 'Eggs')], max_length=50, null=True),
        ),
    ]
