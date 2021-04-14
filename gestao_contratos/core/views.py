from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView


def home(request):
    return render(request, "core/home.html")


def atleta_cadastrar(request):
    return render(request, "core/form_athlete.html")


class LoginUser(LoginView):
    template_name = 'core/login.html'


class LogoutUser(LogoutView):
    template_name = 'core/home.html'
