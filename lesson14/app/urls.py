from django.urls import path
from app.views import *

urlpatterns = [
    path('', index_page_view, name='index'),
    path('form/', form_page_view, name='form'),
]