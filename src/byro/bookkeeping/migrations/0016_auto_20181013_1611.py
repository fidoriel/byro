# Generated by Django 2.1.1 on 2018-10-13 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20181013_1611'),
        ('bookkeeping', '0015_auto_20180707_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTransactionLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Document')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeping.Transaction')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='documents',
            field=models.ManyToManyField(through='bookkeeping.DocumentTransactionLink', to='documents.Document'),
        ),
    ]
