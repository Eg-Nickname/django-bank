import django_filters

from exchange.models import ExchangeListing

class ExchangeListingFilter(django_filters.FilterSet):
    class Meta:
        model = ExchangeListing
        fields = ['exchange_from', 'exchange_to']
    def __init__(self, *args, **kwargs):
       super(ExchangeListingFilter, self).__init__(*args, **kwargs)
       self.filters['exchange_from'].label="Wymień na"
       self.filters['exchange_to'].label="Wymień z"


