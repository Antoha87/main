# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Manager
from django.utils import timezone
from django.conf import settings

from client.models import Client

from catalog.models import Goods

import random


class SelectedProduct(models.Model):
    name = models.CharField(u'Название', max_length=100, blank=True, null=True)
    price = models.IntegerField(u'Цена')
    quantity = models.IntegerField(u'Количество', default=0)
    total_price = models.IntegerField(u'Всего')

    class Meta:
        abstract = True


class CartManager(Manager):
    CART_ID_SESSION_KEY = 'cart_id'

    def from_request(self, request):
        if request.session.get(self.CART_ID_SESSION_KEY, '') == '':
            id = request.session[self.CART_ID_SESSION_KEY] = self._generate_cart_id()
        else:
            id = request.session[self.CART_ID_SESSION_KEY]

        cart, created = Cart.objects.get_or_create(cart_id=id)
        return cart

    def _generate_cart_id(self):
        cart_id = ''
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*() '
        cart_id_length = 50
        for y in range(cart_id_length):
            cart_id += characters[random.randint(0, len(characters) - 1)]
        return cart_id


class Item(SelectedProduct):
    product = models.ForeignKey(Goods)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id or self.quantity > 0:
            self.total_price = self.price * self.quantity
            super(Item, self).save(*args, **kwargs)
        else:
            self.delete()


class Cart(models.Model):
    cart_id = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)

    objects = CartManager()

    def has_items(self):
        return len(list(self.items.all())) > 0

    def total_quantity(self):
        return sum([item.quantity for item in self.items.all()])

    def total_price(self):
        return sum([item.total_price for item in self.items.all()])

    def add_item(self, variation, quantity):
        kwargs = {'product': variation,
                  'price': variation.price,
                  }

        item, created = self.items.get_or_create(**kwargs)
        item.quantity += int(quantity)
        item.save()


class CartItem(Item):
    cart = models.ForeignKey('Cart', verbose_name=u'Корзина', related_name='items')


class OrderManager(Manager):

    def get_for_user(self, order_id, request):
        lookup = {'id': order_id}
        lookup['key'] = request.session.session_key
        return self.get(**lookup)


class Order(models.Model):
    STATUS = (
        (1, u'Принят'),
        (2, u'Оплачен'),
        (3, u'Отправлен'),
        (4, u'Закрыт'),
    )
    session_key = models.CharField(max_length=100, editable=False)
    client = models.ForeignKey(Client, verbose_name=u'Клиент')
    delivery = models.TextField(u'Адрес доставки', max_length=250, blank=True)
    total = models.DecimalField(u'Итого', max_digits=10, decimal_places=2)
    status = models.IntegerField(u'Статус', choices=STATUS, default=1)
    created = models.DateTimeField(u'Создан', default=timezone.now)

    objects = OrderManager()

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'
        ordering = ('-created',)

    def total_quantity(self):
        return sum([item.quantity for item in self.orderitem_set.all()])

    def total_price(self):
        return sum([item.price for item in self.orderitem_set.all()])

    def __unicode__(self):
        return self.get_status_display()


class OrderItem(SelectedProduct):
    order = models.ForeignKey(Order, verbose_name=u'Заказ', related_name='items')

    class Meta:
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    def save(self, *args, **kwargs):
        if not self.id or self.quantity > 0:
            self.price = self.price * self.quantity
            super(OrderItem, self).save(*args, **kwargs)
        else:
            self.delete()

    def __unicode__(self):
        return u'#%s' % self.pk
