from django.dispatch import receiver
from django.shortcuts import get_object_or_404, render, redirect

from exchange.forms import NewExchaneListing, ExchangeMoneyForm
from exchange.models import ExchangeListing
from exchange.filters import ExchangeListingFilter
from exchange.nwd import NWD

from transactions.models import Transaction



from django.contrib import messages

def exchange_viev(request):
    if not request.user.is_authenticated:
        return redirect("login")
    exchange_listings = ExchangeListing.objects.all()
    exchangelisting_filter = ExchangeListingFilter(request.GET, queryset=exchange_listings)
    exchange_listings = exchangelisting_filter

    exchange_form = NewExchaneListing(auto_id="NewExchaneListing_%s")
    context = {
        'exchange_listings' : exchange_listings,
        'exchange_form' : exchange_form,
        'exchangelisting_filter' : exchangelisting_filter,
    }

    if request.POST and 'new-exchange-listing' in request.POST:
        
        exchange_form = NewExchaneListing(request.POST)
        if exchange_form.is_valid():
            exchange_listing = exchange_form.save(commit=False)
            exchange_listing.owner = request.user

            exchange_creator = request.user

            if exchange_listing.exchange_from == exchange_listing.exchange_to:
                messages.info(request, 'Nie możesz wymienić waluty na ta sama')
            elif exchange_listing.amount_owned == 0 or exchange_listing.amount_wanted == 0:
                messages.info(request, 'Wartość musi być wyższa niż zero')
            else:
                nwd = NWD(exchange_listing.amount_owned, exchange_listing.amount_wanted)
                exchange_listing.ratio_from = (exchange_listing.amount_owned/nwd)
                exchange_listing.ratio_to = (exchange_listing.amount_wanted/nwd)

                if getattr(exchange_creator, exchange_listing.exchange_from.lower()) - exchange_listing.amount_owned >= 0:
                    setattr(exchange_creator, exchange_listing.exchange_from.lower(), getattr(exchange_creator, exchange_listing.exchange_from.lower()) - exchange_listing.amount_owned)
                    exchange_creator.save()
                    exchange_listing.save()
                    messages.info(request, 'Pomyślnie umieszczono oferte wymiany')
                else:
                    messages.info(request, 'Brak wystarczajacej liczby środków.')
            return redirect('exchange')
    return render(request, 'exchange/exchange.html', context)




def remove_lising_viev(request, id):
    exchange_listing=get_object_or_404(ExchangeListing, pk=id)
    if request.user == exchange_listing.owner:
        exchange_creator = exchange_listing.owner

        setattr(exchange_creator, exchange_listing.exchange_from.lower(), getattr(exchange_creator, exchange_listing.exchange_from.lower()) + exchange_listing.amount_owned)  

        exchange_creator.save()
        exchange_listing.delete()
        return redirect("/wymiana_walut/")
    else:
        return redirect("/")

def exchange_money_viev(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    exchange_listings = ExchangeListing.objects.all()
    exchange_money_form = ExchangeMoneyForm()

    exchange_listings = ExchangeListing.objects.all()
    exchangelisting_filter = ExchangeListingFilter(request.GET, queryset=exchange_listings)
    exchange_listings = exchangelisting_filter

    exchange_form = NewExchaneListing(auto_id="NewExchaneListing_%s")

    selected_exchange_listing = get_object_or_404(ExchangeListing, pk=id)

    context = {
        'exchange_listings' : exchange_listings,
        'exchange_form' : exchange_form,
        'exchange_money_form' : exchange_money_form,
        'exchangelisting_filter' : exchangelisting_filter,
        'selected_exchange_listing' : selected_exchange_listing,
    }
    
    if request.POST and 'new-exchange-listing' in request.POST:
        exchange_viev(request)
        return redirect("/wymiana_walut/")
    elif request.POST and 'exchange-money' in request.POST:
        exchange_money_form = ExchangeMoneyForm(request.POST)
        if exchange_money_form.is_valid():
            cd = exchange_money_form.cleaned_data
            amount_exchanged = cd.get('amount_exchanged')
            amount_recived = cd.get('amount_recived')

            if selected_exchange_listing.amount_wanted - amount_exchanged >= 0:
                if getattr(request.user, selected_exchange_listing.exchange_to.lower()) - amount_exchanged >= 0:
                    setattr(request.user, selected_exchange_listing.exchange_to.lower(), getattr(request.user, selected_exchange_listing.exchange_to.lower()) - amount_exchanged)
                    setattr(request.user, selected_exchange_listing.exchange_from.lower(), getattr(request.user, selected_exchange_listing.exchange_from.lower()) + amount_recived)
                    setattr(selected_exchange_listing.owner, selected_exchange_listing.exchange_to.lower(), getattr(selected_exchange_listing.owner, selected_exchange_listing.exchange_to.lower()) + amount_exchanged)
                else:
                    messages.info(request, 'Brak wystarczajacej liczby środków.')


                selected_exchange_listing.amount_wanted -= amount_exchanged
                selected_exchange_listing.amount_owned -= amount_recived

                amount_exchanged_transaction = Transaction(sender_id=selected_exchange_listing.owner, reciver_id=request.user, waluta=selected_exchange_listing.exchange_from, kwota=amount_recived, typ=3, title="")
                amount_exchanged_transaction.save()
                amount_recived_transaction = Transaction(sender_id=request.user, reciver_id=selected_exchange_listing.owner, waluta=selected_exchange_listing.exchange_to, kwota=amount_exchanged, typ=3, title="") 
                amount_recived_transaction.save()

                request.user.save()
                selected_exchange_listing.owner.save()
                selected_exchange_listing.save()

                if selected_exchange_listing.amount_wanted == 0 and not selected_exchange_listing.is_fixed or selected_exchange_listing.amount_wanted == 0 and not selected_exchange_listing.is_fixed:
                    selected_exchange_listing.delete()

                succes_msg = str('Pomyślnie wymieniono '+str(amount_exchanged)+str(selected_exchange_listing.exchange_to)+' na '+str(amount_recived)+str(selected_exchange_listing.exchange_from))
                messages.info(request, succes_msg)

        return redirect("/wymiana_walut/")

    return render(request, 'exchange/exchange.html', context)