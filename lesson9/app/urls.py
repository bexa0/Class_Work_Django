from django.urls import path, re_path
from app.views import *
from django.urls import register_converter


class YearConvertor:
    regex = '[0-9]{4}'

    def to_python(self, value: str):
        return int(value)

    def to_url(self, value):
        return value


register_converter(YearConvertor, 'year')


urlpatterns = [
    path('product_list/', product_list_view, name='p_list'),
    path('product_detail/<int:pk>/', product_detail_view, name='p_detail'),
    path('add_product/', product_add, name='p_add'),
    # path('view4', app_view4),
    # path('view5', app_view5),
    # re_path(r'^product_detail/(?P<pk>[0-9]{4})/', product_detail_view),
]