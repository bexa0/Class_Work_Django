from django.urls import path
from app.views import *


urlpatterns = [
    path('', first_view, name='first'),
    path('second/', second_view, name='second'),
    path('third/', third_view, name='third'),
    path('forth/<str:first>/<int:second>/<slug:third>/', forth_view, name='forth'),
    path('human/<str:first_name>/<str:last_name>/', fifth_view, name='fifth'),
]
