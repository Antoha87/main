# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin


from .models import Client
from forms import UserCreationForm


class ClientAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', dict(fields=('date_of_birth',
                                       'first_name',
                                       'last_name',
                                       'phone_number'
                                       ))),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Client, ClientAdmin)
admin.site.unregister(Group)