# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import messages


from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Category, Goods, GoodsVariation, Options, OptionsList, FileProcessing, Location, ImageGallery
from django.core.management import call_command


class CategoryAdmin(AdminImageMixin, DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'activate',)
    list_editable = ["activate"]
    prepopulated_fields = {'slug': ('name',)}


class GoodsVariationAdminInline(admin.StackedInline):
    model = GoodsVariation
    extra = 1


class ImageInline(AdminImageMixin, admin.StackedInline):
    model = ImageGallery
    verbose_name = u'Галерея товара'
    extra = 1


class AddOptionsinline(admin.StackedInline):
    model = Options
    verbose_name = u'Дополнительние опции товаров'
    extra = 1


class GoodsAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ('article', 'name')
    list_display = ('article', 'name', 'get_category')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = (GoodsVariationAdminInline, ImageInline,  AddOptionsinline)

    def get_category(self, obj):
        return ",\n".join([c.name for c in obj.category.all()])


class FileProcessingAdmin(admin.ModelAdmin):
    list_display = ('__name__', 'date', 'status')
    exclude = ('status',)

    def __name__(self, obj):
        return u'Импорт'

    def save_model(self, request, obj, form, change):
        obj.save()
        call_command('fileprocessing')
        messages.success(request, u'Импорт завершен')
        obj.status = True
        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(FileProcessing, FileProcessingAdmin)
admin.site.register(OptionsList)
admin.site.register(Location)
