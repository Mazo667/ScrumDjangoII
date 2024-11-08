from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "accounts"

urlpatterns = [
    path("register/",views.register, name="register"),
    path("login/",
         auth_views.LoginView.as_view(template_name="accounts/login.html"),
         name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("password_change/",
            auth_views.PasswordChangeView.as_view(
                success_url=reverse_lazy("accounts:password_change_done"),
                template_name="accounts/password_change.html"
            ),
            name="password_change"
        ),
    path("password_change/done/",
         auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"),
         name="password_change_done")
]