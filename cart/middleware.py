from .models import Cart


class ShopMiddleware(object):
    def process_request(self, request):
        request.cart = Cart.objects.from_request(request)
