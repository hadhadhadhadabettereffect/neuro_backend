from django.http import JsonResponse

from .models import Product

def product_data(request):
    products = [
        dict(name=p.name,
        type=p.clothing_type,
        id=p.id,
        description=p.description or "",
        materials=p.materials or "")
     for p in Product.objects.all() ]
    return JsonResponse(products, safe=False)
