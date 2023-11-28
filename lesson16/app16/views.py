from django.shortcuts import render
from app16.models import *


def post_list_view(request):
    context = {'post_list': Post.objects.all()}

    return render(request, 'app16/post_list.html', context)


def post_create_view(request):
    return render(request, 'app16/post_create.html')


def post_detail_view(request, post_slug):
    slug_post = Post.objects.get(slug=post_slug)
    context = {'post_slug': slug_post}

    return render(request, 'app16/post_detail.html', context)
