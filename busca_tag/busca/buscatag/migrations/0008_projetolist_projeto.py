# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscatag', '0007_auto_20170112_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetolist',
            name='projeto',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]