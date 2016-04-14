# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import messages


from mptt.admin import MPTTModelAdmin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Category, Goods, GoodsVariation, Options, OptionsList, FileProcessing
from django.core.management import call_command


class CategoryAdmin(AdminImageMixin, MPTTModelAdmin):
    list_display = ('name',)
    sortable = 'order'
    prepopulated_fields = {'slug': ('name',)}


class GoodsVariationAdminInline(admin.StackedInline):
    model = GoodsVariation
    extra = 1


class AddOptionsinline(admin.StackedInline):
    model = Options
    verbose_name = u'Дополнительние опции товаров'
    extra = 1


class GoodsAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('article', 'category')
    list_filter = ('category',)
    inlines = (GoodsVariationAdminInline, AddOptionsinline)


class FileProcessingAdmin(admin.ModelAdmin):
    list_display = ('__name__',)

    def __name__(self, obj):
        return u'Импорт'

    def save_model(self, request, obj, form, change):
        obj.save()
        call_command('fileprocessing')
        messages.success(request, u'Импорт завершен')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(FileProcessing, FileProcessingAdmin)
admin.site.register(OptionsList)
