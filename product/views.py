from django.shortcuts import render
from product.models import Product


def products(request):
    template_name = 'product/products.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name=template_name, context=context)
