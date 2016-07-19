# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CartItem, OrderItem, Cart, Order
from catalog.models import Goods


@csrf_exempt
def cart_add(request):
    data = {'success': False}
    items = {}
    if request.is_ajax and request.POST:

        for key, value in request.POST.items():
            items[key] = value

        for key, value in items.items():
            if key.startswith('count') and int(value) > 0:
                product = get_object_or_404(Goods, pk=key.replace('count', ''))
                request.cart.add_item(product, int(value))
        data = {'success': True,
                'total_quantity': request.cart.total_quantity()}
    return JsonResponse(data)


@login_required
def cart(request):
    # form = OrderForm(request.POST or None)

    if request.method == 'POST':
        p = Order()
        p.client = request.user.client
        p.total = request.cart.total_price()
        p.delivery = request.user.client.delivery
        p.save()

        for item in request.cart.items.all():
            i = OrderItem()
            i.name = item.product.name
            i.order = p
            i.total_price = item.total_price
            i.price = item.price
            i.quantity = item.quantity
            i.save()

        Cart.objects.get(cart_id=request.session['cart_id']).delete()
        messages.info(request, u'Ваш заказ сохранён. В ближайшее время с Вами свяжутся для уточнения заказа')

    return render(request, 'all/order.html')


def cart_delete(request, pk):
    obj = get_object_or_404(CartItem, pk=pk, cart__cart_id=request.session['cart_id'])
    obj.delete()
    return redirect(reverse('index'))
