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
        client = Client.get_client(self.request)
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
        return context

    def post(self, request):
        if request.method == 'POST':
            client = Client.get_client(self.request)
            if client is None:
                client = Client.objects.create(user=self.request.user)
            client.middlename = request.POST['father']
            client.date_birthday = datetime.strptime(request.POST['date_birth'], '%d-%m-%Y')
            client.country = Country.objects.get(code=request.POST['country'])
            client.region_id = request.POST['region']
            client.city_id = request.POST['city']
            client.number = request.POST['phone']
            client.avatar = request.POST['avatar']
            client.delivery = request.POST['delivery']
            client.save()
            user = Client.objects.get(username=self.request.user)
            user.email = request.POST['email']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']

            user.save()
            return HttpResponseRedirect(reverse('profile'))
