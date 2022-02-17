# Generated by Django 3.2 on 2022-02-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operations', models.IntegerField(verbose_name='Numero de operaciones')),
                ('win_rate', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Win rate')),
                ('total_profit_loss', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Profit/Loss')),
                ('profit_loss', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Profit/Loss')),
                ('max_profit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Max Profit')),
                ('max_loss', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Max Loss')),
            ],
        ),
    ]
