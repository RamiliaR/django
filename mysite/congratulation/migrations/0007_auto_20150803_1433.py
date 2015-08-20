# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congratulation', '0006_customer_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_id',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]
