from django.urls import path
from client_side.views import *

urlpatterns = [
    path('', product_view, name='product_list'),
    path('product/<slug:product_slug>/', product_detail, name='product_detail'),
    path('product/<slug:product_slug>/comment_create/', comment_create_view, name='comment_create'),
    # path('product/category-list/', category_list, name='category_list')
]