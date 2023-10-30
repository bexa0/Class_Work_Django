from django.http import HttpResponse
from django.shortcuts import render
from app.models import Product

# Create your views here.


def product_list_view(request):
    product = Product.objects.all()
    context = {'product_list': product}

    return render(request, 'product_list.html', context=context)


def product_detail_view(request, pk):
    context = {'product': Product.objects.get(pk=pk)}

    return render(request, 'product_detail.html', context=context)
    # return HttpResponse(f'Product Detail View - {pk}')


def product_add(request):
    return HttpResponse('Product Add')


# def app_view4(request):
#     return HttpResponse('app_view4')
#
#
# def app_view5(request):
#     return HttpResponse('app_view5')