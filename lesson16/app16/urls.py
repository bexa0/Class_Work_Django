from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('create/', post_create_view, name='post_create'),
    path('detail/<slug:post_slug>/', post_detail_view, name='post_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)