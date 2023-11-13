from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from app.models import *


def first_view(request):
    # QuerySet.query
    # q_set = Human.objects.filter(pk__gte=2)
    # print(q_set.query)

    # get_or_create()
    # human = Human.objects.get_or_create(first_name='Alan', last_name='Wake')

    # update_or_create()
    # human, create_status = Human.objects.update_or_create(first_name='Alan', defaults={'last_name': 'new surname'})
    # print(human, create_status)

    # in_bulk()
    # human = Human.objects.in_bulk()
    # for key, value in human.items():
    #     print(key, '-', value)

    # F
    # humans = Human.objects.in_bulk()
    # for pk, human in humans.items():
    #     human.age += 1
    #     human.save()

    # Human.objects.all().update(age=F('age') + 1)

    context = {'human_list': Human.objects.all()}

    return render(request, 'index1.html', context)


def my_404_handler(request, exception):
    return render(request, '404_template.html')
    # return HttpResponse('Page not found! Get out here')


def second_view(request):
    return render(request, 'index2.html')


def third_view(request):
    return render(request, 'index3.html')


def forth_view(request, first, second, third):
    context = {
        'first': first,
        'second': second,
        'third': third,
    }

    return render(request, 'index4.html', context)


def fifth_view(request, first_name, last_name):
    human = Human.objects.get(first_name=first_name, last_name=last_name)
    context = {'human': human}

    return render(request, 'index5.html', context)

