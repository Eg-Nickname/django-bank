import django_filters

from exchange.models import ExchangeListing

class ExchangeListingFilter(django_filters.FilterSet):
    class Meta:
        model = ExchangeListing
        fields = ['exchange_from', 'exchange_to']

