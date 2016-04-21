from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Index, Banner, Page, Brand
from django.utils import timezone
from django.shortcuts import get_object_or_404


class IndexView(TemplateView):
    template_name = 'all/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['index'] = Index.objects.first()
        context['banners'] = Banner.objects.filter(activate=True).filter(deactivate__gte=timezone.now())
        return context


class ServiceAndGarantyView(TemplateView):
    template_name = 'all/page.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceAndGarantyView, self).get_context_data(**kwargs)
        context['content'] = Page.objects.get(type=1)
        return context


class PayAndDeliveryView(TemplateView):
    template_name = 'all/page.html'

    def get_context_data(self, **kwargs):
        context = super(PayAndDeliveryView, self).get_context_data(**kwargs)
        context['content'] = Page.objects.get(type=2)
        return context


class DiscontView(TemplateView):
    template_name = 'all/page.html'

    def get_context_data(self, **kwargs):
        context = super(DiscontView, self).get_context_data(**kwargs)
        context['content'] = Page.objects.get(type=3)
        return context


class PartnerView(TemplateView):
    template_name = 'all/page.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerView, self).get_context_data(**kwargs)
        context['content'] = Page.objects.get(type=4)
        return context


class ContactView(TemplateView):
    template_name = 'all/page.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['content'] = Page.objects.get(type=5)
        return context


class BrandListView(ListView):
    template_name = 'brand/brand.html'

    def get_queryset(self):
        return Brand.objects.all()


class BrandDetailView(DetailView):
    template_name = 'brand/item.html'
    model = Brand

