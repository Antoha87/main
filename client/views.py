from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Client
from django.core.urlresolvers import reverse
from cart.models import Order
from django_geoip.models import Country
from datetime import datetime
from client.forms import ClientForm
from django.http import HttpResponseRedirect


class ProfileView(TemplateView):
    template_name = 'all/personal_room.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        client = self.request.user
        if client is None:
            country = u'UA'
            region = ''
            city = ''
        else:
            country = client.country
            region = client.region
            city = client.city
        client_form = ClientForm(
            initial={
                'country': country,
                'region': region,
                'city': city,
            }
        )
        context['form'] = client_form
        context['order'] = Order.objects.filter(client=client)
        context['a'] = self.request.user
        return context

    def post(self, request):
        if request.method == 'POST':
            client = self.request.user

            client.date_of_birth = datetime.strptime(request.POST['date_birth'], '%d-%m-%Y')
            client.country = Country.objects.get(code=request.POST['country'])
            client.region_id = request.POST['region']
            client.city_id = request.POST['city']
            client.phone_number = request.POST['phone']

            client.delivery = request.POST['delivery']

            client.email = request.POST['email']
            client.first_name = request.POST['first_name']
            client.last_name = request.POST['last_name']

            client.save()
            return HttpResponseRedirect(reverse('profile'))
