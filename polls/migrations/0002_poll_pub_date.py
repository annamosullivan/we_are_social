# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 11, 21, 16, 38, 279000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
