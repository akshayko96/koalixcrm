# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-05 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20180104_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salescontract',
            name='template_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoUserExtension.DocumentTemplate', verbose_name='Referred Template'),
        ),
    ]