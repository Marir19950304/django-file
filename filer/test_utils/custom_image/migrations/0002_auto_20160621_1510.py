# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='filer.File'),
        ),
        migrations.AlterField(
            model_name='image',
            name='subject_location',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='subject location'),
        ),
    ]
