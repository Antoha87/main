"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from pages.views import IndexView, ContactView, ServiceAndGarantyView, PayAndDeliveryView, DiscontView, PartnerView, BrandDetailView, BrandListView
from catalog.views import CategoryView, CatalogView, GoodsView, ResultsSearchView, CompareView
from client.views import ProfileView


urlpatterns = [
    url(r'', include('cart.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^geoip/', include('django_geoip.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^wishlist/', include('wishlist.urls')),
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'garantiya-servise/', ServiceAndGarantyView.as_view(), name='garantiya'),
    url(r'delivery/', PayAndDeliveryView.as_view(), name='delivery'),
    url(r'diskontnaia-programma/', DiscontView.as_view(), name='diskont'),
    url(r'sotrudnichestvo/', PartnerView.as_view(), name='partner'),
    url(r'contacts/', ContactView.as_view(), name='contacts'),

    url(r'^brand/$', BrandListView.as_view(), name='brand_list'),
    url(r'brand/(?P<slug>[\-\w]+)/$', BrandDetailView.as_view(), name='brand'),
    url(r'^catalog/$', CatalogView.as_view(), name='catalog'),
    url(r'^category/(?P<slug>[\-\w]+)/$', CategoryView.as_view(), name='category'),
    url(r'^goods/(?P<slug>[\-\w]+)/$', GoodsView.as_view(), name='goods'),
    url(r'^search/$', ResultsSearchView.as_view(), name='search'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),

    url(r'^compare', CompareView.as_view(), name='compare'),
    url(r'^del_compare/(?P<pk>\d+)/$', 'catalog.views.del_compare', name='del_compare'),
    url(r'^ajax/add_simile', 'catalog.views.add_simile', name='add_simile'),
    url(r'^ajax/del_simile', 'catalog.views.del_simile', name='del_simile'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)