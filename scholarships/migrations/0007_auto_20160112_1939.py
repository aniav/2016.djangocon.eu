# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2016-01-12 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0006_application_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='financial_assistance',
            field=models.TextField(),
        ),
    ]
