# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 20:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dndpimp', '0003_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]