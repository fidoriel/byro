# Generated by Django 3.2.10 on 2021-12-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0018_auto_20200820_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='currency_postfix',
            field=models.BooleanField(default=True, help_text='Controls whether the currency symbol comes before or after the monetary value', verbose_name='Show currency symbol after value'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='currency_symbol',
            field=models.CharField(default='€', help_text='E.g. €', max_length=8, verbose_name='Currency symbol'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='display_cents',
            field=models.BooleanField(default=True, help_text='When enabled, monetary values include two decimal fractional digits', verbose_name='Display cents'),
        ),
    ]
