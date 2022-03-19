from django import forms
from exchange.models import ExchangeListing

class NewExchaneListing(forms.ModelForm):
    
    class Meta:
        model = ExchangeListing
        fields = ['exchange_from', 'amount_owned', 'exchange_to', 'amount_wanted']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['exchange_from'].label  = "Waluta z której chcesz wymienić"
        self.fields['exchange_to'].label    = "Waluta na którą chcesz wymienić"
        self.fields['amount_owned'].label = "Kwota, która chcemy wymienić"
        self.fields['amount_wanted'].label = "Kwota, która otrzymasz"


class ExchangeMoneyForm(forms.Form):
    amount_exchanged = forms.IntegerField(min_value=0, required=True)
    amount_recived = forms.IntegerField(min_value=1, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount_recived'].widget.attrs['readonly'] = True
        self.fields['amount_exchanged'].label = "Kwota, która chcesz wymienić"
        self.fields['amount_recived'].label = "Kwota, która otrzymasz"