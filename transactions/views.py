from django.http import JsonResponse
from django.shortcuts import render, redirect
from account.models import Account
from django.db.models import Q

from transactions.models import Transaction
from transactions.forms import NewTransaction, Withdraw

from django.contrib import messages


def transactions_viev(request):
    

    if not request.user.is_authenticated:
        return redirect("login")

    sent_transactions = Transaction.objects.filter(Q(sender_id  = request.user.id) | Q(reciver_id = request.user.id)).order_by('data_transakcji')
    form = NewTransaction()
    withdraw_form = Withdraw()
    context = {
            'sent_transactions' : reversed(sent_transactions),
            'transaction_form' : form,
            'withdraw_form' : withdraw_form
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
            trans            = form.save(commit=False)
            trans.sender_id  = request.user

            sender  = Account.objects.get(id=request.user.id)
            reciver =  Account.objects.get(id=trans.reciver_id.id)
   

            if sender == reciver:
                messages.info(request, 'Nie możesz wysłać przelewu do samego siebie.')
            else:
                if trans.kwota == 0:
                    messages.info(request, 'Kwota przelewu musi być większa niż 0')
                else:
                    if trans.waluta == "CNY":
                        if trans.sender_id.cny-trans.kwota >= 0:
                            sender.cny  -= trans.kwota
                            reciver.cny += trans.kwota
                            sender.save()
                            reciver.save()                            
                            trans = trans.save()
                            return redirect('transactions')
                        else:
                            messages.info(request, 'Brak wystarczajacej liczby Yuanów.')
                    
                    elif trans.waluta == "RUB":
                        if trans.sender_id.rub-trans.kwota >= 0:
                            sender.rub  -= trans.kwota
                            reciver.rub += trans.kwota
                            sender.save()
                            reciver.save()                            
                            trans = trans.save()
                            return redirect('transactions')
                        else:
                            messages.info(request, 'Brak wystarczajacej liczby Rubli.')

                    elif trans.waluta == "LIR":
                        if trans.sender_id.lir-trans.kwota >= 0:
                            sender.lir  -= trans.kwota
                            reciver.lir += trans.kwota
                            sender.save()
                            reciver.save()                            
                            trans = trans.save()
                            return redirect('transactions')
                        else:
                            messages.info(request, 'Brak wystarczajacej liczby Lir.')

                    elif trans.waluta == "CLP":
                        if trans.sender_id.clp-trans.kwota >= 0:
                            sender.clp  -= trans.kwota
                            reciver.clp += trans.kwota
                            sender.save()
                            reciver.save()
                            trans = trans.save()
                            return redirect('transactions')
                        else:
                            messages.info(request, 'Brak wystarczajacej liczby Pesos chilijskich.')
                            

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
                if withdraw.waluta == "CNY":
                    if withdraw.sender_id.cny-withdraw.kwota >= 0:
                        sender.cny -= withdraw.kwota
                        withdraw    = withdraw.save()                       
                    else:
                        messages.info(request, 'Brak wystarczajacej liczby Yuanów.')
                elif withdraw.waluta == "RUB":
                    if withdraw.sender_id.rub-withdraw.kwota >= 0:
                        sender.rub -= withdraw.kwota
                        withdraw    = withdraw.save()                        
                    else:
                        messages.info(request, 'Brak wystarczajacej liczby Rubli.')

                elif withdraw.waluta == "LIR":
                    if withdraw.sender_id.lir-withdraw.kwota >= 0:
                        sender.lir -= withdraw.kwota
                        withdraw    = withdraw.save()
                    else:
                        messages.info(request, 'Brak wystarczajacej liczby Lir.')

                elif withdraw.waluta == "CLP":
                    if withdraw.sender_id.clp-withdraw.kwota >= 0:
                        sender.clp -= withdraw.kwota
                        withdraw    = withdraw.save()
                    else:
                        messages.info(request, 'Brak wystarczajacej liczby Pesos chilijskich.')

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
        sent_transactions = Transaction.objects.filter(Q(sender_id  = request.user.id) | Q(reciver_id = request.user.id)).order_by('data_transakcji')
        form = NewTransaction()
        withdraw_form = Withdraw()
    
        context = {
            'selected_transaction' : transaction,
            'sent_transactions' : reversed(sent_transactions),
            'transaction_form' : form,
            'withdraw_form' : withdraw_form
        }
        return render(request, 'transactions/transactions.html', context)
