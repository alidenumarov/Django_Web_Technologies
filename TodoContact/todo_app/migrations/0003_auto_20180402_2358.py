# Generated by Django 2.0.3 on 2018-04-02 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='todoTitle',
        ),
    ]
