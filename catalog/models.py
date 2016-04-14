# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.db.models import Avg, Sum

from sorl.thumbnail import ImageField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django_geoip.models import City, Region
from smart_selects.db_fields import ChainedForeignKey

from pages.models import Brand

from datetime import date, datetime
from hashlib import md5


def image_path(instance, filename):
    ext = filename.rsplit('.')[-1].lower()
    hash = md5(slugify(filename) + '%s' % datetime.now())
    new_filename = "%s.%s" % (hash.hexdigest()[3:10], ext)
    return u"upload/%s/%d/%d/%s" % (date.today().year, date.today().month, date.today().day, new_filename)


class Category(MPTTModel):
    name = models.CharField(u'Название', max_length=64)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='каталог-родитель')
    image = ImageField(u'Фото', upload_to=image_path)
    slug = models.SlugField(u'ЧПУ', max_length=100, unique=True)
    description = models.TextField(u'Сообщение о категории', blank=True, null=True)
    options = models.BooleanField(u'Товар имеет больше 1-го артикулa', default=False)

    order = models.PositiveIntegerField(default=0)
    category_img = ImageField(u'Фон Категории', upload_to='category_img', blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['order']

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        Category.objects.rebuild()

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    def get_absolute_goods_url(self):
        if not self.options:
            return reverse('goods', args=[self.slug])
        else:
            return reverse('goodstable', args=[self.slug])

    def __unicode__(self):
        return self.name


class Goods(models.Model):
    article = models.CharField(u'Артикул', max_length=100, blank=True, null=True)
    #region = models.ForeignKey(Region, verbose_name=u'Регион')
    #city = ChainedForeignKey(City, verbose_name=u'Город', chained_field="region", chained_model_field="region", related_name='city_ads')
    brand = models.ForeignKey(Brand, verbose_name=u'Производитель')
    image = ImageField(u'Фото', upload_to=image_path, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=u'Категория', limit_choices_to={'parent__isnull': False})
    description = models.TextField(u'Описание', blank=True, null=True)
    special_offer = models.BooleanField(u'Специальное предложение', default=False)

    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    def get_warehouse(self):
        res = GoodsVariation.objects.filter(goods=self)\
                                    .aggregate(Sum('warehouse'))
        if res['warehouse__sum'] > 0:
            return u'На складе: %s' % res['warehouse__sum']
        return u'Под заказ'

    def get_variations(self):
        result = GoodsVariation.objects.filter(goods=self)
        return result

    def __unicode__(self):
        return self.article or str(self.pk)


class GoodsVariation(models.Model):
    article = models.CharField(u'Артикул', max_length=100, blank=True, null=True)
    goods = models.ForeignKey(Goods, verbose_name=u'Товар', related_name='variations')

    warehouse = models.IntegerField(u'Склад', default=0)

    class Meta:
        verbose_name = u'Вариант'
        verbose_name_plural = u'Варианты'
        ordering = ('article',)

    def get_warehouse(self):
        if self.warehouse == 0:
            return u'Под заказ'
        return self.warehouse

    def __unicode__(self):
        return self.article or str(self.pk)


class OptionsList(models.Model):
    name = models.CharField(u'Имя характеристики', max_length=100)

    class Meta:
        verbose_name = u'Дополнительние опции товаров'
        verbose_name_plural = u'Дополнительная опция товара'

    def __unicode__(self):
        return self.name


class Options(models.Model):
    goods = models.ForeignKey(Goods, verbose_name=u'Дополнительние опции товаров')
    name = models.ForeignKey(OptionsList, verbose_name=u'Опция')
    value = models.CharField(u'Значение', max_length=100)

    class Meta:
        verbose_name = u'Опцию'
        verbose_name_plural = u'Дополнительние опции'

    def __unicode__(self):
        return '#%s' % self.pk


class FileProcessing(models.Model):
    fileprocessing = models.FileField(u'Файл', upload_to=image_path, max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = u'Импорт'

    def __unicode__(self):
        return str(self.pk)
