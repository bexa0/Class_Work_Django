from django.urls import path
from .views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='start'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='log_in'),
    path('logout/', UserLogoutView.as_view(), name='log_out'),
    # path('test/', test_page_view, name='test')
]