# Generated by Django 3.2.18 on 2023-05-12 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='end_date',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='start_date',
            new_name='start',
        ),
    ]