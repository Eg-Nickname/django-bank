# Generated by Django 4.0 on 2022-01-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_reciver_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reciver_id',
            field=models.PositiveIntegerField(verbose_name='Id odbiorcy'),
        ),
    ]
