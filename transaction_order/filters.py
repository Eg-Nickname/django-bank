import django_filters
from transaction_order.models import TransactionOrder

class TransactionOrderFilter(django_filters.FilterSet):
    class Meta:
        model = TransactionOrder
        fields = '__all__'
        exclude = ['transaction_order_id', 'sender_fk', 'amount', 'last_transaction', 'title']
