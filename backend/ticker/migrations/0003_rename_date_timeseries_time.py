# Generated by Django 3.2 on 2022-03-12 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0002_timeseries'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeseries',
            old_name='date',
            new_name='time',
        ),
    ]
