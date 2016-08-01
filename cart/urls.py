from django.conf.urls import patterns, url
from .views import PersonalDataCheckout, DeliveryCheckout

urlpatterns = patterns('',
    url(r'^cart/$', 'cart.views.cart', name='cart'),
    url(r'^cart/add/$', 'cart.views.cart_add', name='cart_add'),
    url(r'^cart/delete/(?P<pk>\d+)/$', 'cart.views.cart_delete', name='cart_delete'),
    url(r'^checkout/personal-data/$', PersonalDataCheckout.as_view(), name='personal_data'),
    url(r'^checkout/delivery/$', DeliveryCheckout.as_view(), name='delivery_checkout'),
)
