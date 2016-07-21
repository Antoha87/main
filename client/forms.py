# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from smart_selects.form_fields import ChainedModelChoiceField
from django_geoip.models import Country


class ClientForm(forms.Form):
    country = forms.ModelChoiceField(label=u'Страна', queryset=Country.objects.all(), required=True)
    #region = ChainedModelChoiceField(label=u'Регион', app_name='django_geoip', model_name='Region', chain_field='country', model_field='country', show_all=False, auto_choose=True)
    #city = ChainedModelChoiceField(label=u'Город', app_name='django_geoip', model_name='City', chain_field='region', model_field='region', show_all=False, auto_choose=True)


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