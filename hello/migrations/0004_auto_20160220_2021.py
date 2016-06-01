# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello', '0003_proyecto_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='url',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='administrador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
