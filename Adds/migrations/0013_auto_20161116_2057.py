# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-16 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Adds', '0012_auto_20161116_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adds',
            old_name='item',
            new_name='choose_category',
        ),
        migrations.AddField(
            model_name='adds',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='adds',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='adds',
            name='image',
            field=models.ImageField(default='images/default/no-img.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='adds',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='adds',
            name='title',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='adds',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
