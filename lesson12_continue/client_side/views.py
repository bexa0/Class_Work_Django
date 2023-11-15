from django.shortcuts import render, redirect

from client_side.models import Comment
from shop_side.models import Product, Category


def product_view(request):
    context = {'product_list': Product.objects.all(), 'category_list': Category.objects.all()}

    return render(request, 'client_side/product_list.html', context)


# def category_list(request, category_l):
#     category = Product.objects.get(category=category_l)
#     context = {'category_list': Product.objects.filter(category=category)}
#
#     return render(request, 'client_side/category_list.html', context)


def product_detail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product, 'comment_list': Comment.objects.filter(product=product)}

    return render(request, 'client_side/product_detail.html', context)


def comment_create_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.method == 'POST':
        username = request.POST.get('username')
        body = request.POST.get('body')
        comment = Comment()
        comment.product = product
        comment.user_name = username
        comment.body = body

        comment.save()

    return redirect('product_detail', product.slug)

