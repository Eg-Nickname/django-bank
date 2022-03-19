from django.contrib import admin
from exchange.models import ExchangeListing



class ExchangeListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'amount_owned', 'exchange_from', 'amount_wanted',  'exchange_to',)
    # search_fields = ('',)
    # readonly_fields = ('',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ExchangeListing, ExchangeListingAdmin)