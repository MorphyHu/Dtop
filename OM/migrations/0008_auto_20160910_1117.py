# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-10 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OM', '0007_servergroup_server_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverlist',
            name='service_owner',
        ),
        migrations.AddField(
            model_name='servergroup',
            name='servergroup_memo',
            field=models.CharField(default='null', max_length=64, verbose_name='\u5907\u6ce8\u4fe1\u606f'),
        ),
        migrations.AddField(
            model_name='serverlist',
            name='server_memo',
            field=models.CharField(default='null', max_length=64, verbose_name='\u5907\u6ce8\u4fe1\u606f'),
        ),
    ]