from dataclasses import field
import django_filters
from django_filters import DateRangeFilter
from transactions.models import Transaction

class TransacionFilter(django_filters.FilterSet):
    daterange = DateRangeFilter(field_name="data_transakcji")
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['typ', 'title', 'data_transakcji', 'kwota']
