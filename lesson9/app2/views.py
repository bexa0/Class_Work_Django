from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def app2_view1(request):
    return HttpResponse('app2_view1')


def app2_view2(request):
    return HttpResponse('app2_view2')


def app2_view3(request):
    return HttpResponse('app2_view3')


def app2_view4(request):
    return HttpResponse('app2_view4')


def app2_view5(request):
    return HttpResponse('app2_view5')