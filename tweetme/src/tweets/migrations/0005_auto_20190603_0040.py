# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-06-03 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=100, validators=[tweets.validators.validate_content]),
        ),
    ]
