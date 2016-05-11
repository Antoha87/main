# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.db.models import Avg, Sum

from ckeditor.fields import RichTextField
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

LOC = (
        ('Украина', u'Украина'),
        ('Киев', u'Киев'),
        ('Днепропетровск', u'Днепропетровск'),
        ('Запорожье', u'Запорожье'),
    )


class Category(MPTTModel):
    name = models.CharField(u'Название', max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='каталог-родитель')
    image = ImageField(u'Фото', upload_to=image_path, blank=False, null=True)
    slug = models.SlugField(u'ЧПУ', max_length=100, unique=True)
    description = models.TextField(u'Сообщение о категории', blank=True, null=True)
    options = models.BooleanField(u'Товар имеет больше 1-го артикулa', default=False)

    order = models.PositiveIntegerField(default=0)
    activate = models.BooleanField(u'Активация категории')

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


class Location(models.Model):
    location = models.CharField(u'Локация товара', choices=LOC, max_length=100, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = u'Локация'
        verbose_name_plural = u'Локации'

    def __unicode__(self):
        return self.get_location_display()


class Goods(models.Model):
    article = models.CharField(u'Артикул', max_length=100, blank=True, null=True)
    kod = models.CharField(u'Код товара', max_length=100, blank=True, null=True)
    model = models.CharField(u'Модель товара', max_length=255, blank=True, null=True)
    name = models.CharField(u'Название товара', max_length=255, blank=False, null=True)
    post = models.CharField(u'Поставщик', max_length=100, blank=False, null=True)
    currence = models.CharField(u'Валюта товара', max_length=255, blank=False, null=True)
    price = models.DecimalField(u'Цена в грн.', decimal_places=2, max_digits=11, blank=True, null=True)
    stock = models.CharField(u'Остаток на складе', max_length=100, blank=True, null=True)
    location = models.ManyToManyField(Location, verbose_name=u'Местонахождение товара')
    brand = models.ForeignKey(Brand, verbose_name=u'Производитель')
    torg = models.CharField(u'Торговое предложение', max_length=100, blank=True, null=True)
    image = ImageField(u'Фото', upload_to=image_path, blank=True, null=True)
    category = models.ManyToManyField(Category, verbose_name=u'Категория', limit_choices_to={'parent__isnull': False})
    description = RichTextField(u'Описание', blank=True, null=True)
    collection = models.CharField(u'Коллекция', max_length=100, blank=True, null=True)
    special_offer = models.BooleanField(u'Специальное предложение', default=False)
    diskont = models.IntegerField(u'Скидка в процентах', default=0)
    garanty = models.IntegerField(u'Гарантия в месяцах', blank=True, null=True)
    youtube_url = models.URLField(u'Ссылка на youtube.com', blank=True, null=True)
    soput = models.TextField(u'Сопутствующие товары', blank=True, null=True,
                             help_text='Перечисляем категории для рандомных товаров.')
    krat = models.CharField(u'Кратность', max_length=100, blank=True, null=True)
    izm = models.CharField(u'За сколько указана цена', max_length=100, blank=True, null=True)
    gab = models.CharField(u'Габариты', max_length=100, blank=True, null=True)
    ves = models.CharField(u'Вес', max_length=100, blank=True, null=True)
    type = models.CharField(u'Тип', max_length=100, blank=True, null=True)
    color = models.CharField(u'Цвет', max_length=100, blank=True, null=True)
    vid = models.CharField(u'Вид', max_length=100, blank=True, null=True)


    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    # Пока не дописал
    def get_stock(self):
        res = self.stock
        return res

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


class ImageGalery(models.Model):
    goods = models.ForeignKey(Goods, verbose_name=u'Фото галерея')
    image = ImageField(u'Фото', upload_to=image_path)

    class Meta:
        verbose_name = u'Фото'
        verbose_name_plural = u'Фото'

    def __unicode__(self):
        return '#%s' % self.pk


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
    date = models.DateTimeField(u'Дата импорта', auto_now=True)
    status = models.BooleanField(u'Статус', default=False)

    class Meta:
        verbose_name = verbose_name_plural = u'Импорт'

    def __unicode__(self):
        return str(self.pk)
