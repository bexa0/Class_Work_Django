from django.shortcuts import render
from app.models import *

# Create your views here.


def start_page(request):
    human = Human.objects.all()
    context = {'human_list': human}
    return render(request, 'index.html', context=context)