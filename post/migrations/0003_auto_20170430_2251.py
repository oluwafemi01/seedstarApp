# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_post_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated']},
        ),
    ]