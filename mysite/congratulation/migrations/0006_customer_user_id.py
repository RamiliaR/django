# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congratulation', '0005_auto_20150731_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user_id',
            field=models.CharField(null=True, max_length=5),
        ),
    ]
