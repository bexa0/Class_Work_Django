from django.shortcuts import render
from app1.models import Product


def index_page(request):
    products = Product.objects.all()
    context = {'products_list': products}

    return render(request, 'index.html', context=context)


def add_product(request):
    if request.method == 'POST':
        # request.POST = {'input_name' : input_value}
        # request.GET = {'input_name' : input_value}
        title = request.POST.get('title')
        category = request.POST.get('category')
        price = request.POST.get('price')

        Product.objects.create(title=title, category=category, price=price)

    return render(request, 'add_product.html')


def delete_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Product.objects.get(title=title).delete()

    products = Product.objects.all()
    context = {'product_list': products}

    return render(request, 'delete.html', context=context)
