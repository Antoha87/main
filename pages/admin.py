# -*- coding: utf-8 -*-
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Index, Banner, Page, Brand


class BannerInline(AdminImageMixin, admin.StackedInline):
    model = Banner
    extra = 1


class IndexAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = (BannerInline,)


class BrandAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


admin.site.register(Index, IndexAdmin)
admin.site.register(Page)
admin.site.register(Brand, BrandAdmin)

