# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_message_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]