# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-09 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopperManage', '0006_auto_20170608_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sellerid',
            field=models.IntegerField(default=0),
        ),
    ]
