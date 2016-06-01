# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_design_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='image',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
