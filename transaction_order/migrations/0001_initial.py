# Generated by Django 4.0 on 2022-04-17 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_alter_account_discord_id_alter_account_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionOrder',
            fields=[
                ('transaction_order_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id Zlecenia Tranzakcji')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Kwota')),
                ('waluta', models.CharField(choices=[('CNY', 'Yuan'), ('RUB', 'Rubel'), ('LIR', 'Lira'), ('CLP', 'Peso chilijskie')], max_length=32, verbose_name='Waluta')),
                ('last_transaction', models.DateTimeField(auto_now_add=True, verbose_name='Ostatnia tranzakcja')),
                ('transaction_delay', models.IntegerField(choices=[(1, 'Codziennie'), (7, 'Co siedem dni.'), (30, 'Raz na 30 dni.'), (90, 'Raz na 90 dni.'), (365, 'Raz na 365 dni.')])),
                ('title', models.CharField(default='Tytuł Przelewu', max_length=100, verbose_name='Tytuł przelewu')),
                ('reciver_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OdbiorcaZleceniaTranzakcji', to='account.account', verbose_name='Odbiorca')),
                ('sender_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NadawcaZleceniaTranzakcji', to='account.account', verbose_name='Nadawca')),
            ],
        ),
    ]