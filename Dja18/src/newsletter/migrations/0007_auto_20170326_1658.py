# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(default=b'Nai Hustle'),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=b'watch what you wear'),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.TextField(default=b'Moi avenue Imax Building floor 4 stall 23', max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=b'The best watch Company'),
        ),
    ]
