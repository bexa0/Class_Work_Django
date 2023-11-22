from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *


def course_list_view(request):
    context = {'course_list': Course.objects.all}

    return render(request, 'lesson15app/course_list.html', context)


def course_detail_view(request, pk):
    context = {'course': get_object_or_404(Course, pk=pk)}

    return render(request, 'lesson15app/course_detail.html', context)


# def course_create_view(request):
#     context = {'form': CourseCreateForm}
#
#     if request.method == 'POST':
#         form = CourseCreateForm(request.POST)
#         # Данные прошли валидацию
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             description = form.cleaned_data.get('description')
#             avg_time = form.cleaned_data.get('avg_time')
#
#             course = Course()
#             course.title = title
#             course.description = description
#             course.avg_time = avg_time
#             course.save()
#
#             # return redirect('course_list')
#             return redirect('course_detail', course.pk)
#
#         # данные не прошли валидацию
#         context['form'] = form
#
#     return render(request, 'lesson15app/course_create.html', context)


def course_create_view(request):
    form = CourseCreateModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CourseCreateModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('course_list')
        context['form'] = form

    return render(request, 'lesson15app/course_create.html', context)

