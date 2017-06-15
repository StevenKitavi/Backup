# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_auto_20170331_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=50),
        ),
    ]
