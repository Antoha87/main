# -*- coding: utf-8 -*-
from django import forms
from client.models import Client
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ('total', 'status', 'created')


