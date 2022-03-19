from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.http import request

from django.utils.translation import gettext as _

from account.models import Account

class RegistrationForm(UserCreationForm):
    # discord_id = forms.CharField(max_length=32, required=False, help_text="Opcjonalne. Potrzebne do korzystania z usług przyszłego bot'a na discord. Przykładowe id: 258298241433600002. Jeśli nie wiesz skąd je wziąść pozostaw puste pole.", label=_("Discord ID"))
    username = forms.CharField(max_length=32, required=True, help_text="Wprowadź swój nick z serwera jako nazwę użytkownika", label=_("login"), widget=forms.TextInput(attrs={'placeholder': 'Nazwa Użytkownika'}))
    class Meta:
        model = Account
        fields = ("username", "password1", "password2")     # "discord_id",
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password2'].widget.attrs['placeholder'] = 'Powtórz hasło'

class AccountAuthenticationForm(forms.ModelForm):
    username = forms.CharField(help_text="Nick z serwera", label=_("login"), widget=forms.TextInput(attrs={'placeholder': 'Nazwa Użytkownika'}) ) 
    password = forms.CharField(label='haslo', widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}) )

    class Meta:
        model = Account
        fields = ('username', 'password')


    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Błędny login lub hasło")

class AccountUpdateForm(forms.ModelForm):
    # discord_id = forms.CharField(max_length=32, required=False, help_text="Opcjonalne. Potrzebne do korzystania z usług przyszłego bot'a na discord. Przykładowe id: 258298241433600002. Jeśli nie wiesz skąd je wziąć skontaktuj się z @E.g Nickname#8717 na discord.", label=_("Discord ID"))
    username = forms.CharField(max_length=32, required=True, help_text="Wprowadź swój nick z serwera jako nazwę użytkownika.", label=_("login"), widget=forms.TextInput(attrs={'placeholder': 'Nazwa Użytkownika'}))
    email = forms.EmailField(max_length=100, required=False, help_text="Całkowicie opcjonalne.", label=_("Email"), widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))

    class Meta:
        model = Account
        fields = ('username', 'email') #, 'discord_id'

        def clean_username(self):
            if self.is_valid():
                username = self.clened_data['username']
                try:
                    account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
                except Account.DoesNotExist:
                    return username
                raise forms.ValidationError('Nazwa użytkonika "%s" jest już zajęta.' % username)

        # def clean_discord_id(self):
        #     if self.is_valid():
        #         discord_id = self.clened_data['discord_id']
        #         try:
        #             account = Account.objects.exclude(pk=self.instance.pk).get(discord_id=discord_id)
        #         except Account.DoesNotExist:
        #             return discord_id
        #         raise forms.ValidationError('Discord ID "%s" jest już używane przez innego użytkownika.' % discord_id)

        def clean_email(self):
            if self.is_valid():
                email = self.clened_data['email']
                try:
                    account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
                except Account.DoesNotExist:
                    return email
                #raise forms.ValidationError('Email "%s" jest już używany.' % email)