# Generated by Django 4.0.4 on 2022-10-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_alter_transaction_reciver_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.PositiveIntegerField(default=0, verbose_name='Status transakcji'),
        ),
    ]