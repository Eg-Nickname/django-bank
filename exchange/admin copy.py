from django.contrib import admin
from transactions.models import Transaction



class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'sender_id', 'reciver_id', 'kwota', 'waluta', 'data_transakcji', 'typ')
    search_fields = ('transaction_id', 'sender_id', 'reciver_id', 'waluta', 'data_transakcji', 'typ')
    readonly_fields = ('data_transakcji',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Transaction, TransactionAdmin)