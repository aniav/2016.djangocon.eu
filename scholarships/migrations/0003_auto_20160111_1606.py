# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2016-01-11 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0002_auto_20160111_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='location',
            field=models.CharField(max_length=150),
        ),
    ]
