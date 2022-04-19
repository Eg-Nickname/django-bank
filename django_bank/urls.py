"""django_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from account.views import (
    registration_viev,
    logout_viev,
    login_viev,
    account_viev,
    change_password,
)

from transactions.views import (
    transactions_viev,
    transactions_inspection_viev,
)

from exchange.views import (
    exchange_viev,
    remove_lising_viev,
    exchange_money_viev,
)

from admindashboard.views import (
    admindashboard_viev,
)
from transaction_order.views import (
    transaction_order_viev,
    remove_transaction_order_viev,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("main.urls")),
    path('register/', registration_viev, name="register"),
    path('logout/', logout_viev, name="logout"),
    path('login/', login_viev, name="login"),
    path('account/', account_viev, name="account"),
    path('account/change_password', change_password, name="change_password"),
    path('saldo/', transactions_viev, name="transactions"),
    path('wymiana_walut/', exchange_viev, name="exchange"),
    path('removelisting/<int:id>', remove_lising_viev, name="remove-listing"),
    path('wymiana_walut/<int:id>', exchange_money_viev, name="exchange-money"),
    path('saldo/<int:id>', transactions_inspection_viev, name="inspect-transaction"),
    path('admindashboard/', admindashboard_viev, name="admindashboard"),
    path('zlecenia_transakcji/', transaction_order_viev, name="zlecenia_transakcji"),
    path('zlecenia_transakcji/<int:id>', remove_transaction_order_viev, name="remove_zlecenia_transakcji"),
]
