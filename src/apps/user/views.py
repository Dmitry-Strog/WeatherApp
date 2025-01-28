from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from apps.user.forms import LoginForm, RegisterForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('weather:home')

    def form_valid(self, form):
        username = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Неверный логин или пароль")
            return super().form_invalid(form)


def logouts(request):
    logout(request)
    return HttpResponseRedirect(reverse('weather:home'))


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('weather:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('weather:home')
