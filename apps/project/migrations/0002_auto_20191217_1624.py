# Generated by Django 2.2.7 on 2019-12-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='discord',
        ),
        migrations.RemoveField(
            model_name='project',
            name='github',
        ),
        migrations.AddField(
            model_name='project',
            name='callback',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='technical_spec_url',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='vcs',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='trello',
            field=models.TextField(blank=True, default=''),
        ),
    ]
