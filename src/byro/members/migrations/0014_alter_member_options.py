# Generated by Django 3.2.16 on 2022-10-26 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_auto_20200820_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('direct_address_name', 'name')},
        ),
    ]
