# Generated by Django 2.2.7 on 2020-01-18 09:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20200118_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremailconfirmation',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 9, 28, 29, 781217, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpasswordrecovery',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 9, 28, 29, 781217, tzinfo=utc)),
        ),
    ]
