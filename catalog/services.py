from django.core.cache import cache
from .models import Product

def get_all_products_cached(timeout=60):
    products = cache.get('all_products')

    if not products:
        products = Product.objects.filter(is_published=True).select_related('category', 'owner')
        cache.set('all_products', products, timeout)

    return products
