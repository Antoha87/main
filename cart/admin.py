# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Order, OrderItem


class OrderItemAdminInline(admin.StackedInline):
    model = OrderItem

    def has_add_permission(self, request):
        return


class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'created')
    list_filter = ('status',)
    radio_fields = {'status': admin.HORIZONTAL}
    inlines = [OrderItemAdminInline]

    def has_add_permission(self, request):
        return

    def has_delete_permission(self, request, obj=None):
        return

admin.site.register(Order, OrderAdmin)
