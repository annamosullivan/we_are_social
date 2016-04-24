# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default=datetime.datetime(2016, 4, 24, 11, 37, 53, 773000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
