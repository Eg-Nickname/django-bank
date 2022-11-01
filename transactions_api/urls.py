from django.urls import path
from transactions_api.views import TransactionList, TransactionDetails, SendTransaction

urlpatterns = [
    path('transactions_list/', TransactionList.as_view(), name='transactions_list'),
    path('transaction_details/<int:pk>', TransactionDetails.as_view(), name='transaction_details'),
    path('send_transaction/', SendTransaction.as_view(), name='transactions_send'),
]