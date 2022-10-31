from django.db import models
from account.models import Account

class Transaction(models.Model):
    WALUTY = (
        ('CNY', 'Yuan'),
        ('RUB', 'Rubel'),
        ('LIR', 'Lira'),
        ('CLP', 'Peso chilijskie'),
    )

    transaction_id      = models.BigAutoField(verbose_name="Id Tranzakcji", primary_key=True)
    sender_id           = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL, related_name='Nadawca', verbose_name="Nadawca")
    reciver_id          = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, related_name='Odbiorca', verbose_name="Odbiorca")
    kwota               = models.PositiveIntegerField(verbose_name="Kwota", blank=False, default=0)
    waluta              = models.CharField(verbose_name="Waluta", max_length=32, unique=False, choices=WALUTY)
    data_transakcji     = models.DateTimeField(verbose_name='Data Transakcji', auto_now_add=True)
    typ                 = models.PositiveIntegerField(verbose_name="Typ transakcji", default=0)
    # 0 - Przelew Zwykły
    # 1 - Wpłata na konto
    # 2 - Wypłata z konta
    # 3 - Wymiana walut
    title               = models.CharField(verbose_name="Tytuł przelewu", max_length=100, unique=False, default="Tytuł Przelewu")
    status              = models.PositiveIntegerField(verbose_name="Status transakcji", default=0)
    def __str__(self):
        return str(self.transaction_id)