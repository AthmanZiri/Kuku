# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-16 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adds', '0011_remove_adds_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addsimage',
            name='item',
        ),
        migrations.DeleteModel(
            name='AddsImage',
        ),
    ]
