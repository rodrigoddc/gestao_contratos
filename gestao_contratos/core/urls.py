from django.urls import path

from gestao_contratos.core.views import home, atleta_cadastrar, LoginUser, LogoutUser

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("formulario/", atleta_cadastrar, name="formulario"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout-user/", LogoutUser.as_view(), name="logout"),
]
