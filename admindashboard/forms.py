from django import forms
from transactions.models import Transaction
from account.models import Account
from django.utils.translation import gettext as _



class Payment(forms.ModelForm):
    
    class Meta:
            model = Transaction
            fields = ['reciver_id', 'kwota', 'waluta']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['reciver_id'].label = "Nazwa odbiorcy"
        self.fields['reciver_id'].queryset = Account.objects.none()

        if 'reciver_id' in self.data:
            self.fields['reciver_id'].queryset = Account.objects.all()

        elif self.instance.pk:
            self.fields['reciver_id'].queryset = Account.objects.all().filter(pk=self.instance.reciver_id.pk)