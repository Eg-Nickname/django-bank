from django.db import models
from account.models import Account
from django.utils import timezone
class TransactionOrder(models.Model):
    WALUTY = (
        ('CNY', 'Yuan'),
        ('RUB', 'Rubel'),
        ('LIR', 'Lira'),
        ('CLP', 'Peso chilijskie'),
    )

    TIME_DIFFERENCES = (
        (1, 'Codziennie'),
        (7, 'Co siedem dni'),
        (30, 'Raz na 30 dni'),
        (90, 'Raz na 90 dni'),
        (365, 'Raz na 365 dni'),
    )


    transaction_order_id    = models.BigAutoField(verbose_name="Id Zlecenia Tranzakcji", primary_key=True)
    sender_fk               = models.ForeignKey(Account, blank=False, on_delete=models.CASCADE, related_name='NadawcaZleceniaTranzakcji', verbose_name="Nadawca")
    reciver_fk              = models.ForeignKey(Account, blank=False, on_delete=models.CASCADE, related_name='OdbiorcaZleceniaTranzakcji', verbose_name="Odbiorca")
    amount                  = models.PositiveIntegerField(verbose_name="Kwota", blank=False, default=0)
    waluta                  = models.CharField(verbose_name="Waluta", max_length=32, unique=False, choices=WALUTY)
    last_transaction        = models.DateTimeField(verbose_name='Ostatnia tranzakcja', auto_now_add=True)
    transaction_delay       = models.IntegerField(unique=False, blank=False, choices=TIME_DIFFERENCES, verbose_name="Cykliczność")
    title                   = models.CharField(verbose_name="Tytuł przelewu", max_length=100, unique=False, default="Tytuł Przelewu")

    def save(self, *args, **kwargs):
        self.last_transaction = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.transaction_order_id)