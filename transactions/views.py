from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from account.models import Account
from django.db.models import Q

from transactions.models import Transaction
from transactions.forms import NewTransaction, Withdraw
from transactions.filters import TransacionFilter

from exchange.models import ExchangeListing

from django.contrib import messages


def transactions_viev(request):
    

    if not request.user.is_authenticated:
        return redirect("login")

    sent_transactions = Transaction.objects.filter(Q(sender_id  = request.user.id) | Q(reciver_id = request.user.id)).order_by('-data_transakcji')
    transactions_filter = TransacionFilter(request.GET, queryset=sent_transactions)
    sent_transactions = transactions_filter
    

    form = NewTransaction(auto_id="NewTransaction_%s")
    withdraw_form = Withdraw()
    context = {
            'sent_transactions' : sent_transactions,
            'transaction_form' : form,
            'withdraw_form' : withdraw_form,
            'transactions_filter' : transactions_filter,
        }
    
    # Formularz przelewu wyszukiwanie konta 
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        term = request.GET['q']
        reciver_id = Account.objects.all().filter(username__icontains=term)
        return JsonResponse(list(reciver_id.values()), safe=False)    

    # Przelewy
    if request.POST and 'transaction' in request.POST:
        form = NewTransaction(request.POST)
        if form.is_valid():
            trans   = form.save(commit=False)
            trans.sender_id = request.user

            sender = Account.objects.get(id=request.user.id)
            reciver = Account.objects.get(id=trans.reciver_id.id)

            if sender == reciver:
                messages.info(request, 'Nie możesz wysłać przelewu do samego siebie.')
            else:
                if trans.kwota == 0:
                    messages.info(request, 'Kwota przelewu musi być większa niż 0')
                else:
                    if getattr(sender, trans.waluta.lower()) - trans.kwota >= 0:
                        setattr(sender, trans.waluta.lower(), getattr(sender, trans.waluta.lower()) - trans.kwota)
                        setattr(reciver, trans.waluta.lower(), getattr(reciver, trans.waluta.lower()) + trans.kwota)
                        sender.save()
                        reciver.save() 
                        trans = trans.save()
                        return redirect('transactions')
                    else:
                        messages.info(request, 'Brak wystarczajacej liczby środków.')
 
                            

    # Wypłacanie  
    elif request.POST and 'withdraw' in request.POST:
        withdraw_form = Withdraw(request.POST)

        sender = Account.objects.get(id=request.user.id)
        reciver =  None
 
        if withdraw_form.is_valid():
            withdraw = withdraw_form.save(commit=False)
            withdraw.sender_id  = sender
            withdraw.reciver_id = reciver
            withdraw.typ = 2
            if withdraw.kwota == 0:
                    messages.info(request, 'Kwota wypłaty musi być większa niż 0')
            else:
                if getattr(sender, withdraw.waluta.lower())-withdraw.kwota >= 0:
                    setattr(sender, withdraw.waluta.lower(), getattr(sender, withdraw.waluta.lower()) - withdraw.kwota)
                    withdraw = withdraw.save()                       
                else:
                    messages.info(request, 'Brak wystarczajacej liczby środków.')

                sender.save()
                return redirect('transactions')
    return render(request, 'transactions/transactions.html', context)

def transactions_inspection_viev(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.POST and 'withdraw' in request.POST:
        transactions_viev(request)
        return redirect("/saldo/")
    elif request.POST and 'transaction' in request.POST:
        transactions_viev(request)
        return redirect("/saldo/")  
    else:

        transaction = Transaction.objects.get(pk=id)
        if transaction.sender_id == request.user or transaction.reciver_id == request.user:
            transaction = transaction
        else:
            return redirect("/saldo/")
        sent_transactions = Transaction.objects.filter(Q(sender_id  = request.user.id) | Q(reciver_id = request.user.id)).order_by('-data_transakcji')
        transactions_filter = TransacionFilter(request.GET, queryset=sent_transactions)
        sent_transactions = transactions_filter
        form = NewTransaction(auto_id="NewTransaction_%s")
        withdraw_form = Withdraw()

        context = {
                'selected_transaction' : transaction,
                'sent_transactions' : sent_transactions,
                'transaction_form' : form,
                'withdraw_form' : withdraw_form,
                'transactions_filter' : transactions_filter,
            }
        return render(request, 'transactions/transactions.html', context)

def remove_transaction_order_viev(request, id):
    transaction_order=get_object_or_404(ExchangeListing, pk=id)
    if request.user == transaction_order.owner:
        transaction_order.delete()
        return redirect("/zlecenia_transakcji/")
    else:
        return redirect("/")