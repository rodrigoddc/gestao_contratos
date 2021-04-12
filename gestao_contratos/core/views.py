from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def atleta_cadastrar(request):
    return render(request, "core/form_athlete.html")


def login(LoginView):
    pass
