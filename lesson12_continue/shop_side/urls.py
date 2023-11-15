from django.urls import path
from .views import *

urlpatterns = [
    path('product-create/', product_create_view, name='product_create'),
    path('product-delete/<slug:product_slug>/', product_delete, name='product_delete'),
    path('product-update/<slug:product_slug>/', product_update, name='product_update'),
]