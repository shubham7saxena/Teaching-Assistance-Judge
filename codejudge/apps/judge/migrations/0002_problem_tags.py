# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-07-06 08:26
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
