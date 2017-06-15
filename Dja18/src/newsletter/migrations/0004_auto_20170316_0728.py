# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='updated',
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default=b'', max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='password_again',
            field=models.CharField(default=b'', max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=120),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=120),
        ),
    ]
