from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^cart/$', 'cart.views.cart', name='cart'),
    url(r'^cart/add/$', 'cart.views.cart_add', name='cart_add'),
    url(r'^cart/delete/(?P<pk>\d+)/$', 'cart.views.cart_delete', name='cart_delete'),
)
