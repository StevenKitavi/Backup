# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20170316_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(default=b'', max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(default=b'', max_length=120, null=True, blank=True),
        ),
    ]
