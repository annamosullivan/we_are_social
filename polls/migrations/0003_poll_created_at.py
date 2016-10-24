# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
