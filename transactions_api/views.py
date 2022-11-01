from rest_framework import generics
from rest_framework import permissions

from django.db.models import Q

from transactions.models import Transaction
from transactions_api.serializers import TransactionSerializer, SendTransactionSerializer


class TransactionViewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.reciver_id  == request.user


class TransactionList(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        transactions = Transaction.objects.filter((Q(sender_id  = user) | Q(reciver_id = user)))
        return transactions.filter(typ=0)

    serializer_class = TransactionSerializer

class TransactionDetails(generics.RetrieveAPIView):
    permission_classes = [TransactionViewPermission]
    
    queryset = Transaction.objects.filter(typ=0)

    serializer_class = TransactionSerializer

class SendTransaction(generics.CreateAPIView):
    serializer_class = SendTransactionSerializer