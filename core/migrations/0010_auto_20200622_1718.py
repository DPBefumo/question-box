# Generated by Django 3.0.7 on 2020-06-22 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200621_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='correct_marker',
            new_name='marked_correct',
        ),
    ]