from django.http import JsonResponse
from django.shortcuts import render, redirect
from account.models import Account
from django.db.models import Q

from transaction_order.models import TransactionOrder
from transaction_order.forms import NewTransactionOrder
from transaction_order.filters import TransactionOrderFilter

from django.contrib import messages


def transaction_order_viev(request):
    

    if not request.user.is_authenticated:
        return redirect("login")

    transaction_orders = TransactionOrder.objects.filter(Q(sender_fk  = request.user.id)).order_by('-transaction_delay')
    transaction_orders_filter = TransactionOrderFilter(request.GET, queryset=transaction_orders)
    transaction_orders = transaction_orders_filter
    transaction_order_form = NewTransactionOrder(auto_id="NewTransactionOrder_%s")

    
    context = {
            'transaction_orders' : transaction_orders,
            'transaction_order_form' : transaction_order_form,
            'transaction_orders_filter' : transaction_orders_filter,
        }
    
    # Wyszukiwanie konta 
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        term = request.GET['q']
        reciver_fk = Account.objects.all().filter(username__icontains=term)
        return JsonResponse(list(reciver_fk.values()), safe=False)    

    # Zlecenie tranzakcji
    if request.POST and 'transaction' in request.POST:
        transaction_order_form = NewTransactionOrder(request.POST)
        if transaction_order_form.is_valid():
            trans = transaction_order_form.save(commit=False)
            trans.sender_fk = request.user

            sender = Account.objects.get(id=request.user.id)
            reciver = Account.objects.get(id=trans.reciver_fk.id)

            if sender == reciver:
                messages.info(request, 'Nie możesz stworzyć zlecenia do samego siebie.')
            else:
                if trans.amount == 0:
                    messages.info(request, 'Kwota przelewu musi być większa niż 0')
                else:
                    trans = trans.save()
                    return redirect('transactions')
    return render(request, 'transaction_order/transaction_order.html', context)