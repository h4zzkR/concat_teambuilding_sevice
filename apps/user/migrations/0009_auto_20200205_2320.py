# Generated by Django 3.0.2 on 2020-02-05 20:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200205_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremailconfirmation',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 6, 20, 20, 23, 785234, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpasswordrecovery',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 6, 20, 20, 23, 784236, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='confirmed',
            field=models.BooleanField(default=True),
        ),
    ]
