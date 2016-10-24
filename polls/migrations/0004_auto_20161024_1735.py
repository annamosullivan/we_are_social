# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_poll_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
    ]
