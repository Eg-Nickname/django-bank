from django.contrib import admin
from transaction_order.models import TransactionOrder



class TransactionOrderAdmin(admin.ModelAdmin):
    list_display = ('transaction_order_id', 'sender_fk', 'reciver_fk', 'amount', 'waluta', 'last_transaction', 'transaction_delay')
    # search_fields = ('',)
    # readonly_fields = ('',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(TransactionOrder, TransactionOrderAdmin)