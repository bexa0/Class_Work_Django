from django.urls import path
from app2.views import *

urlpatterns = [
    path('view1', app2_view1),
    path('view2', app2_view2),
    path('view3', app2_view3),
    path('view4', app2_view4),
    path('view5', app2_view5),
]