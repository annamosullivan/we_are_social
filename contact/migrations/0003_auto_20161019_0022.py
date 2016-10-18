# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_feedback_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='sender',
            new_name='name',
        ),
    ]
