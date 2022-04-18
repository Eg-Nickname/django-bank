from django import forms
from transaction_order.models import TransactionOrder
from account.models import Account




class NewTransactionOrder(forms.ModelForm):
    
    class Meta:
            model = TransactionOrder
            fields = ['title', 'reciver_fk', 'amount', 'waluta', 'transaction_delay']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['reciver_fk'].label = "Nazwa odbiorcy"
        self.fields['reciver_fk'].queryset = Account.objects.none()

        if 'reciver_fk' in self.data:
            self.fields['reciver_fk'].queryset = Account.objects.all()

        elif self.instance.pk:
            self.fields['reciver_fk'].queryset = Account.objects.all().filter(pk=self.instance.reciver_fk.pk)