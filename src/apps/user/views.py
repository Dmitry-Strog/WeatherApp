from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.user.forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('weather:home'))
            else:
                form.add_error(None, "Неверный логин или пароль.")
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('weather:home'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('weather:home'))
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, "register.html", context)