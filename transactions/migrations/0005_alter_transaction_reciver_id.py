# Generated by Django 4.0 on 2022-01-05 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_discord_id_alter_account_email'),
        ('transactions', '0004_alter_transaction_reciver_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reciver_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reciver_id', to='account.account'),
        ),
    ]
