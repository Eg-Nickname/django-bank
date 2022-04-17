from django.core.management.base import BaseCommand
from django.utils import timezone

# from account.models import Account
from transaction_order.models import TransactionOrder
from transactions.models import Transaction 


from datetime import timedelta

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        transaction_orders = TransactionOrder.objects.all()

        start_time = timezone.now()

        for transaction_order in transaction_orders:
            next_transaction = transaction_order.last_transaction + timedelta(days=transaction_order.transaction_delay)

            sender = transaction_order.sender_fk
            reciver = transaction_order.reciver_fk

            if next_transaction < start_time:
                if getattr(sender, transaction_order.waluta.lower()) - transaction_order.amount >= 0:
                    setattr(sender, transaction_order.waluta.lower(), getattr(sender, transaction_order.waluta.lower()) - transaction_order.amount)
                    setattr(reciver, transaction_order.waluta.lower(), getattr(reciver, transaction_order.waluta.lower()) + transaction_order.amount)

                    transaction_order_transaction = Transaction(sender_id=sender, reciver_id=reciver, waluta=transaction_order.waluta, kwota=transaction_order.amount, typ=0, title=transaction_order.title)
                    transaction_order_transaction.save()

                    sender.save()
                    reciver.save() 
                    transaction_order.last_transaction = timezone.now()
                    transaction_order = transaction_order.save()


                    

