# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-10 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20170809_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.IntegerField(choices=[(0, 'repo'), (1, 'pm')], default=0, verbose_name='Service Type'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='identifier',
            field=models.IntegerField(choices=[(0, 'access_token'), (1, 'username'), (2, 'password'), (3, 'api_url'), (4, 'key'), (5, 'secret'), (6, 'database_name'), (7, 'pm')], default=0, verbose_name='Identifier'),
        ),
    ]
