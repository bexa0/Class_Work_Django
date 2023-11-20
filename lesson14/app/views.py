from django.shortcuts import render, redirect
from app.form import *
from app.models import *


def test_for_digit(str_):
    for ch in str_:
        if ch.isdigit():
            return False
    return True


def index_page_view(request):
    feedbacks = FeedBack.objects.all()
    context = {'feedback_list': feedbacks}

    return render(request, 'page_post.html', context)


def form_page_view(request):
    context = {}

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            print('Данные валидные')
            
            feedback = FeedBack()
            feedback.name = name
            feedback.email = email
            feedback.text = text
            feedback.save()

            return redirect('index')

        else:
            print('Данные не валидные')
            

        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # text = request.POST.get('text')
        #
        # context['reply'] = 'Error'
        #
        # if test_for_digit(name):
        #     context['reply'] = 'Success'

    form = FeedbackForm()
    context['form'] = form

    return render(request, 'form.html', context)
