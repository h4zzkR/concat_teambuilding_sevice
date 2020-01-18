# Generated by Django 2.2.7 on 2020-01-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(related_name='collabs', to='project.Collaborator'),
        ),
    ]
