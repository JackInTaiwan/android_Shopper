# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-02 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopperManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=60)),
                ('product_name', models.CharField(max_length=60)),
                ('product_attr', models.CharField(max_length=30)),
                ('product_price', models.IntegerField()),
                ('product_img', models.TextField()),
                ('product_buyer', models.CharField(default='', max_length=60)),
            ],
        ),
    ]