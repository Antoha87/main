from pages.models import Brand


def brand_globals(request):
    brand_list = Brand.objects.all()
    return {'brand_list': brand_list}
