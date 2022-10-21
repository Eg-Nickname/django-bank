from django.dispatch import receiver
from django.http import JsonResponse
from django.shortcuts import render, redirect

from account.models import Account
from django.db.models import Q

from transactions.models import Transaction
from admindashboard.forms import Payment

from django.contrib import messages


def admindashboard_viev(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_superuser:
        return redirect("login")

    withdraw_transactions = Transaction.objects.filter(Q(typ = 2)).order_by('data_transakcji')
    payment_form = Payment()
    context = {
            'withdraw_transactions' : reversed(withdraw_transactions),
            'payment_form' : payment_form
        }

    # Formularz wyszukiwanie konta
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        term = request.GET['q']
        reciver_id = Account.objects.all().filter(username__icontains=term)
        return JsonResponse(list(reciver_id.values()), safe=False)    

        # Wypłacanie  
    if request.POST and 'payment' in request.POST:
        payment_form = Payment(request.POST)
 
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            reciver = Account.objects.get(id=payment.reciver_id.id)

            payment.sender_id  = None
            payment.reciver_id = reciver
            payment.typ = 1
            if payment.kwota == 0:
                    messages.warning(request, 'Kwota wpłaty musi być większa niż 0')
            else:
                setattr(reciver, payment.waluta.lower(), getattr(reciver, payment.waluta.lower()) + payment.kwota)
                
                messages.success(request, f"Pomyślnie dodano {payment.kwota} {payment.waluta} użytkownikowi {payment.reciver_id.username}")
                payment = payment.save()
            
                reciver.save()
                return redirect('admindashboard')

    return render(request, 'admindashboard/admindashboard.html', context)


