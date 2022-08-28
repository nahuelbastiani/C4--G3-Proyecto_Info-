from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from . import views
from django.conf.urls.static      import static 

app_name = 'usuario'
urlpatterns =[
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name="usuario/login.html"), name='login'),
    path('', views.inicio),
   # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)   
