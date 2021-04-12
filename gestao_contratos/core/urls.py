from django.urls import path

from gestao_contratos.core.views import home, atleta_cadastrar, login

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("formulario/", atleta_cadastrar, name="formulario"),
    path("login/", login, name="login"),
]
