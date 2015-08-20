# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congratulation', '0007_auto_20150803_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
