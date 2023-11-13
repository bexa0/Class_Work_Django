from django.shortcuts import render
from shop_side.models import *


def product_create_view(request):
    context = {'category_list': Category.objects.all()}

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')

        product = Product()
        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = Category.objects.get(pk=category)
        product.save()

    return render(request, 'shop_side/product_create.html', context)
