# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-23 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_auto_20170423_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='birth_date',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]