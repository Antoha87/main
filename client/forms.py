# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from smart_selects.form_fields import ChainedModelChoiceField
from django_geoip.models import Country

User = get_user_model()


class ClientForm(forms.Form):
    country = forms.ModelChoiceField(label=u'Страна', queryset=Country.objects.all(), required=True)
    #region = ChainedModelChoiceField(label=u'Регион', app_name='django_geoip', model_name='Region', chain_field='country', model_field='country', show_all=False, auto_choose=True)
    #city = ChainedModelChoiceField(label=u'Город', app_name='django_geoip', model_name='City', chain_field='region', model_field='region', show_all=False, auto_choose=True)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label=u'Повторите пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(RegistrationForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("Данный почтовый ящик уже используется. Пожалуйста, укажите свой адрес электронной почты.")
        return self.cleaned_data['email']

    def create_user(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        new_user = User.objects.create_user(email, password)
        new_user.save()

        self.user_cache = authenticate(email=email, password=password)
        if self.user_cache is None:
            return
        if self.user_cache is not None and not self.user_cache.is_active:
            return
        login(self.request, self.user_cache)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=u'Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label=u'Подтверждение',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(u'Пароль и подтверждение не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email',)


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        widget=forms.PasswordInput,
        required=False
    )

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['email', ]


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()