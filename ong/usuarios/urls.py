from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate, logout


app_name = "usuarios"   


urlpatterns = [
    path("registro/", views.register_request, name="registro"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/",auth_views.logout_then_login, name="logout"),
]