from django import forms
from transactions.models import Transaction
from account.models import Account
from django.utils.translation import gettext as _



class NewTransaction(forms.ModelForm):
    
    class Meta:
            model = Transaction
            fields = ['title', 'reciver_id', 'kwota', 'waluta']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['reciver_id'].label = "Nazwa odbiorcy"
        self.fields['reciver_id'].queryset = Account.objects.none()

        if 'reciver_id' in self.data:
            self.fields['reciver_id'].queryset = Account.objects.all()

        elif self.instance.pk:
            self.fields['reciver_id'].queryset = Account.objects.all().filter(pk=self.instance.reciver_id.pk)


class Withdraw(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True, help_text="Wprowadź nick z serwera na jaki mają zostać wypłacone środki", label=_("Nazwa użytkownika"), widget=forms.TextInput(attrs={'placeholder': 'Wprowadz nazwe użytkownika'}))

    class Meta:
            model = Transaction
            fields = ['title', 'kwota', 'waluta']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['waluta'].widget.attrs['id'] = 'id_waluta2'