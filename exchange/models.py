from django.db import models
from account.models import Account

class ExchangeListing(models.Model):
    WALUTY = (
        ('CNY', 'Yuan'),
        ('RUB', 'Rubel'),
        ('LIR', 'Lira'),
        ('CLP', 'Peso chilijskie'),
    )

    owner               = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    exchange_from       = models.CharField(verbose_name="Wymiana z", max_length=32, unique=False, choices=WALUTY)
    exchange_to         = models.CharField(verbose_name="Wymiana na", max_length=32, unique=False, choices=WALUTY)
    amount_owned        = models.PositiveIntegerField(verbose_name="Kwota1", blank=False, default=0)
    amount_wanted       = models.PositiveIntegerField(verbose_name="Kwota2", blank=False, default=0)
    ratio_from          = models.PositiveIntegerField(verbose_name="Ratio Góra", blank=False, default=1)
    ratio_to            = models.PositiveIntegerField(verbose_name="Ratio Dół", blank=False, default=1)
    is_fixed            = models.BooleanField(default=False)




    def __str__(self):
        return str(self.id)