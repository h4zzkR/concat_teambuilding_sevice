# Generated by Django 2.2.7 on 2019-12-17 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20191217_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremailconfirmation',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 18, 14, 2, 8, 63094, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpasswordrecovery',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 18, 14, 2, 8, 63094, tzinfo=utc)),
        ),
    ]
