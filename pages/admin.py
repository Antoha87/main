# -*- coding: utf-8 -*-
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Index, Banner, Page, Brand


class BannerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('head', 'activate', 'deactivate')
    list_filter = ('head', 'activate', 'deactivate')
    list_editable = ["activate"]


class BrandAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    list_filter = ('name',)


admin.site.register(Index)
admin.site.register(Page)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Brand, BrandAdmin)

