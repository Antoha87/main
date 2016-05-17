# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse

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
        return ctx


class GoodsView(DetailView):
    template_name = 'catalog/goods.html'
    model = Goods

    def get_context_data(self, **kwargs):
        context = super(GoodsView, self).get_context_data(**kwargs)
        context['image_gallery'] = ImageGallery.objects.filter(goods=self.get_object())
        return context


class ResultsSearchView(ListView):
    template_name = 'catalog/goods.html'

    def get_queryset(self):
        text = self.request.GET.get('text')
        return Goods.objects.filter(Q(article__icontains=text) |
                                    Q(description__icontains=text))
