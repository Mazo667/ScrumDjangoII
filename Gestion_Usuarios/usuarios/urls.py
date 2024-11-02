from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "usuarios"

urlpatterns = [
    path("registro/",views.registro, name="registro"),
    path("acceder/",
         auth_views.LoginView.as_view(template_name="usuarios/login.html"),
         name="acceder"),
    path("cerrar-sesion/",auth_views.LogoutView.as_view(),name="cerrar-sesion"),
    path(
            "cambiar-clave/",
            auth_views.PasswordChangeView.as_view(
                success_url=reverse_lazy("usuarios:cambiar-clave-hecho"),
                template_name="usuarios/password_change.html"
            ),
            name="cambiar-clave"
        ),
    path("cambiar-clave/hecho/",
         auth_views.PasswordChangeDoneView.as_view(template_name="usuarios/password_change_done.html"),
         name="cambiar-clave-hecho")
]