# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-03 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopperManage', '0003_product_product_uploadtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sellerid',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
