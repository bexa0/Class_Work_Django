from django.urls import path
from .views import *

urlpatterns = [
    path('', course_list_view, name='course_list'),
    path('course/<int:pk>/', course_detail_view, name='course_detail'),
    path('course/create/', course_create_view, name='course_create'),
    path('course/create/module/', course_create_view, name='module_create'),
]
