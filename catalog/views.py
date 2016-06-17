# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Count, Min, Max, Q, FloatField
import pymorphy2

from .models import Category, Goods, GoodsVariation, ImageGallery


class CatalogView(ListView):
    template_name = 'catalog/catalog.html'

    def get_queryset(self):
        return Category.objects.filter(level=0)


class CategoryView(ListView):
    template_name = 'catalog/category.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Category, slug=slug)

    def get_queryset(self):
        return Category.objects.filter(parent=self.get_object())

    def get_context_data(self, **kwargs):
        ctx = super(CategoryView, self).get_context_data(**kwargs)
        ctx['object'] = self.get_object()
        slug = self.kwargs.get('slug')
        goods = Goods.objects.filter(category__slug=slug)
        if len(goods) > 0:
            ctx['goods'] = goods
            ctx['filter_price'] = goods.aggregate(min=Min('price'), max=Max('price'))
            morph = pymorphy2.MorphAnalyzer()
            goods_str = morph.parse(u'товар')[0]
            ctx['goods_count_str'] = u'%s %s' % (goods.count(), goods_str.make_agree_with_number(int(goods.count())).word)
        return ctx


class MenuView(TemplateView):
    template_name = 'include/menu.html'

    def get_context_data(self, **kwargs):
        ctx = super(MenuView, self).get_context_data(**kwargs)
        ctx['category'] = Category.objects.filter(activate=True)
        return ctx


class GoodsView(DetailView):
    template_name = 'catalog/goods.html'
    model = Goods

    def get_context_data(self, **kwargs):
        context = super(GoodsView, self).get_context_data(**kwargs)
        context['image_gallery'] = ImageGallery.objects.filter(goods=self.get_object())
        return context


class ResultsSearchView(ListView):
    template_name = 'catalog/search.html'

    def get_queryset(self, **kwargs):
        text = self.request.GET.get('text')
        goods = Goods.objects.filter(Q(article__icontains=text) | Q(name__icontains=text))
        return goods
