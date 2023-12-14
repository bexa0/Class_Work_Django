from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class StartPageView(TemplateView):
    template_name = 'app/start.html'

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)


class SignUpView(CreateView):
    template_name = 'app/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('start')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('start')

        return super().get(request, *args, **kwargs)


class UserLoginView(LoginView):
    template_name = 'app/log_in.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start')


class UserLogoutView(LogoutView):
    template_name = 'app/log_out.html'
    next_page = reverse_lazy('start')


# def test_page_view(request):
#     context = {'message': 'This page is only for staff'}
#     if request.user.is_staff:
#         context = {'message': 'You`re staff'}
#     return render(request, 'app/start.html', context=context)


