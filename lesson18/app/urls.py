from django.urls import path
from app.views import *

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('product/<slug:slug>', ProductDetailView.as_view(), name="product_detail"),
    path('create/', ProductCreateView.as_view(), name="product_create"),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name="product_update"),
    path('product/<slug:slug>/delete/', ProductDeleteView.as_view(), name="product_delete"),
]


