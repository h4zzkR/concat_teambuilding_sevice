# Generated by Django 2.2.7 on 2019-12-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20191217_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='public',
        ),
        migrations.AddField(
            model_name='project',
            name='is_public',
            field=models.BooleanField(default=0),
        ),
    ]
