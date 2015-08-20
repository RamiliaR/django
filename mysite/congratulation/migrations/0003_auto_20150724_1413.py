# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congratulation', '0002_auto_20150714_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(null=True, max_length=75),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(null=True, max_length=30),
        ),
    ]
