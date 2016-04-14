# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField



TYPE = (
        (1, u'О магазине'),
        (2, u'Оплата'),
        (3, u'Доставка'),
        (4, u'Контакты'),
    )


class AbstractPage(models.Model):
    type = models.IntegerField(u'Тип страници', choices=TYPE, unique=True)

    class Meta:
        abstract = True


class Index(models.Model):
    seo = RichTextField(u'СЕО текст главной страници')

    class Meta:
        verbose_name = u'Главная страница'
        verbose_name_plural = u'Главная страница'

    def __unicode__(self):
        return u'Главная страница'


class Banner(models.Model):
    index = models.ForeignKey(Index, verbose_name=u'Баннер', help_text=u'Баннер')
    head = RichTextField(u'Заголовок',  help_text=u'Редактируемый заголовок баннера')
    text = RichTextField(u'Текст баннера', help_text=u'Редактируемый текст баннера')
    url = models.URLField(u'URL баннера', null=True, blank=True)
    activate = models.BooleanField(u'Активация', default=False, help_text=u'Активация баннера')
    deactivate = models.DateTimeField(u'Дективация баннера', help_text=u'Время деактивации баннера')
    img = ImageField(u'Логотип баннера', upload_to='uploads', help_text=u'Логотип баннера')

    class Meta:
        verbose_name = u'Баннер'
        verbose_name_plural = u'Баннера'

    def __unicode__(self):
        return self.head


class Page(AbstractPage):
    text = RichTextField(u'Текст', help_text=u'текст страници')

    class Meta:
        verbose_name = u'Статическая страница'
        verbose_name_plural = u'Статические страници'

    def __unicode__(self):
        return self.get_type_display()


class Brand(models.Model):
    name = models.CharField(u'Имя бренда',  help_text=u'Имя бренда', max_length=100)
    img = ImageField(u'Логотип бренда', upload_to='brand/uploads', help_text=u'Логотип бренда')
    text = RichTextField(u'Текст бренда', help_text=u'Редактируемый текст бренда')

    class Meta:
        verbose_name = u'Производитель'
        verbose_name_plural = u'Производители'

    def __unicode__(self):
        return self.name

